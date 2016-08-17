from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

# Validator contributed by Matt Jegan (https://github.com/mattjegan)
def validate_url(url):
	RESTRICTED_URLS = [
		'base',
		'shows',
		'login',
	]
	if str(url).lower() in RESTRICTED_URLS:
		raise ValidationError('Urls starting with {} are not allowed'.format(url))

# Create your models here.
class Page(models.Model):
	pageTitle = models.CharField(max_length=20, verbose_name='Page Title (Will be displayed on site')
	pageURL = models.CharField(max_length=50, verbose_name='Page URL (http://kvrx.org/PAGEURL)', unique=True, validators=[validate_url])
	pageContent = models.TextField(verbose_name='Page Content (HTML). Will be placed inside the standard KVRX template')
	showOnHomepage = models.BooleanField(verbose_name='Show on home page?')
	def __unicode__(self):
		return self.pageTitle

