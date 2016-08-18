from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Deejay(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	dj = models.CharField(max_length=50, verbose_name='DJ Name', unique=True)
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
	show_name = models.CharField(max_length=200, verbose_name='Show name')
	dj = models.ForeignKey(Deejay, verbose_name='DJ')
	date_choices = (
		('M', 'Monday'),
		('T', 'Tuesday'),
		('W', 'Wednesday'),
		('TH', 'Thursday'),
		('F', 'Friday'),
		('SA', 'Saturday'),
		('SU', 'Sunday'),
	)
	show_date = models.CharField(choices=date_choices, max_length=50, verbose_name='Show day')
	start_time = models.TimeField(auto_now=False, verbose_name='Start time')
	end_time = models.TimeField(auto_now=False, verbose_name='End time')
	description = models.TextField(verbose_name='Show description')
	def __unicode__(self):
		return "%s - %s" % (self.show_name, self.dj.dj)

class Playlist(models.Model):
	show = models.ForeignKey('Show')
	date = models.DateField(auto_now_add=False, verbose_name='Playlist date')
	description = models.TextField(verbose_name='Playlist description')
	songs = models.ManyToManyField('Song', blank=True, verbose_name='Songs')
	def __unicode__(self):
		return "%s - %s" % (self.show.show_name, str(self.date))

class Song(models.Model):
	album_ID = models.CharField(max_length=50, null=True, blank=True, verbose_name='Album ID')
	title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Song')
	artist = models.CharField(max_length=50, null=True, blank=True, verbose_name='Artist')
	album = models.CharField(max_length=50, null=True, blank=True)
	genre = models.CharField(max_length=50, null=True, blank=True)
	label = models.CharField(max_length=50, null=True, blank=True)
	tx_artist = models.BooleanField(verbose_name='Texas artist?')
	current_track = models.BooleanField(verbose_name='Current track?')
	def __unicode__(self):
		return "%s by %s" % (self.title, self.artist)
	def save(self, *args, **kwargs):
		if self.current_track:
			try:
				temp = Song.objects.get(current_track=True)
				if self != temp:
					temp.current_track = False
					temp.save()
			except Song.DoesNotExist:
				pass
		super(Song, self).save(*args, **kwargs)
