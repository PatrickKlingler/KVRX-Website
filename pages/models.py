from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Page(models.Model):
	pageTitle = models.CharField(max_length=20, verbose_name='Page Title (Will be displayed on site')
	pageURL = models.CharField(max_length=50, verbose_name='Page URL (http://kvrx.org/PAGEURL)', unique=True)
	pageContent = models.TextField(verbose_name='Page Content (HTML). Will be placed inside the standard KVRX template')
	showOnHomepage = models.BooleanField(verbose_name='Show on home page?')
	def __unicode__(self):
		return self.pageTitle

