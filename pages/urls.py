"""KVRX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #Index
    url(r'^$', views.index, name="index"),
    #Hardcoded pages
    url(r'^base', views.base, name="base"), #REMOVE IN PRODUCTION
    url(r'^shows', views.shows, name="shows"),
    url(r'^login', views.login, name="login"),
    #Keyword pages
    url(r'^dj/(?P<dj_name>.+)/$', views.dj_detail, name="dj_detail"),
    url(r'^show/(?P<show_name>.+)/$', views.show_detail, name="show_detail"),
    #User created pages (CMS)
    url(r'^(?P<page>.+)/$', views.custom_page, name="custom_page"),
]

admin.site.site_header = 'KVRX Admin'
admin.site.site_title = 'KVRX Admin'