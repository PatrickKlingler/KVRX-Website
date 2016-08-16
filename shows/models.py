from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Deejay(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dj = models.CharField(max_length=50, verbose_name='DJ Name')
	pic = models.ImageField(blank=True, null=True)
	role = models.CharField(max_length=50, verbose_name='Job title', default="DJ")
	bio = models.TextField(verbose_name='Bio')
	phone = models.CharField(max_length=15, verbose_name='Phone number') #kind of a hack. allows you to enter 15 characters. here's the fix: http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
	def __unicode__(self):
		return "%s %s - %s" % (self.user.first_name, self.user.last_name, self.dj)
	def has_image(self):
		try:
			return self.pic.url
		except:
			return False

class Show(models.Model):
	showname = models.CharField(max_length=200, verbose_name='Show name')
	dj = models.ForeignKey(Deejay, verbose_name='DJ')
	dateChoices = (
		('M', 'Monday'),
		('T', 'Tuesday'),
		('W', 'Wednesday'),
		('TH', 'Thursday'),
		('F', 'Friday'),
		('SA', 'Saturday'),
		('SU', 'Sunday'),
	)
	showDate = models.CharField(choices=dateChoices, max_length=50, verbose_name='Show day')
	startTime = models.TimeField(auto_now=False, verbose_name='Start time')
	endTime = models.TimeField(auto_now=False, verbose_name='End time')
	description = models.TextField(verbose_name='Show description')
	def __unicode__(self):
		return "%s - %s" % (self.showname, self.dj.dj)

class Playlist(models.Model):
	show = models.ForeignKey('Show')
	date = models.DateField(auto_now_add=False, verbose_name='Playlist date')
	description = models.TextField(verbose_name='Playlist description')
	songs = models.ManyToManyField('Song', blank=True, verbose_name='Songs')
	def __unicode__(self):
		return "%s - %s" % (self.show.showname, str(self.date))

class Song(models.Model):
	albumID = models.CharField(max_length=50, null=True, blank=True, verbose_name='Album ID')
	title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Song')
	artist = models.CharField(max_length=50, null=True, blank=True, verbose_name='Artist')
	album = models.CharField(max_length=50, null=True, blank=True)
	genre = models.CharField(max_length=50, null=True, blank=True)
	label = models.CharField(max_length=50, null=True, blank=True)
	txArtist = models.BooleanField(verbose_name='Texas artist?')
	currentTrack = models.BooleanField(verbose_name='Current track?')
	def __unicode__(self):
		return "%s by %s" % (self.title, self.artist)
	def save(self, *args, **kwargs):
		if self.currentTrack:
			try:
				temp = Song.objects.get(currentTrack=True)
				if self != temp:
					temp.currentTrack = False
					temp.save()
			except Song.DoesNotExist:
				pass
		super(Song, self).save(*args, **kwargs)
