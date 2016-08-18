from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

# Validator contributed by Matt Jegan (https://github.com/mattjegan)
def validate_url(url):
	restricted_urls = [
		'base',
		'shows',
		'login',
		'admin',
	]
	if str(url).lower() in restricted_urls:
		raise ValidationError('The URL "{}" is already a custom page.'.format(url))

# Create your models here.
class Page(models.Model):
	page_title = models.CharField(max_length=20, verbose_name='Page Title (Will be displayed on site')
	page_url = models.CharField(max_length=50, verbose_name='Page URL (http://kvrx.org/PAGEURL)', unique=True, validators=[validate_url])
	page_content = models.TextField(verbose_name='Page Content (HTML). Will be placed inside the standard KVRX template')
	show_on_homepage = models.BooleanField(verbose_name='Show on home page?')
	def __unicode__(self):
		return self.page_title

