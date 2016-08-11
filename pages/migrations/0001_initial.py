# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageTitle', models.CharField(max_length=20, verbose_name='Page Title (Will be displayed on site')),
                ('pageURL', models.CharField(max_length=50, verbose_name='Page URL (http://kvrx.org/PAGEURL)')),
                ('pageContent', models.TextField(verbose_name='Page Content (HTML). Will be placed inside the standard KVRX template')),
                ('showOnHomepage', models.BooleanField(verbose_name='Show on home page?')),
            ],
        ),
    ]
