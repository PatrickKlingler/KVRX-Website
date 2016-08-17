from django.shortcuts import render, get_object_or_404
from .models import Page
from shows.models import Deejay, Show, Playlist, Song

# Page rendering methods here

#THIS IS A CONTEXT PROCESSOR
#DOCUMENTATION INCOMING
#FUCK YEAH I DID IT
def getBaseInfo(request):
	allPages = Page.objects.all()
	currentTrack = Song.objects.get(currentTrack=True)
	primaryPages = allPages[:5]
	secondaryPages = allPages[5:]
	return {'p':primaryPages, 'p2':secondaryPages, 'currentTrack':currentTrack}

# Create your views here.

def base(request):
	return render(request, 'pages/base.html', {})

def index(request):
	return render(request, 'pages/index.html', {})

def custom_page(request, p):
	userPage = get_object_or_404(Page, pageURL=p)
	return render(request, 'pages/details/page_detail.html', {'content': userPage})

def login(request):
	return render(request, 'pages/login.html', {})

def dj_detail(request, djName):
	djObject = get_object_or_404(Deejay.objects.filter(dj__iexact=djName))
	shows = Show.objects.filter(dj=djObject)
	return render(request, 'pages/details/dj_detail.html', {'dj':djObject, 'shows':shows})

def show_detail(request, namegiven):
	showObject = get_object_or_404(Show.objects.filter(showname__iexact=namegiven))
	playlists = Playlist.objects.filter(show=showObject)
	return render(request, 'pages/details/show_detail.html', {'show':showObject, 'playlists':playlists})

def shows(request):
	djs = Deejay.objects.all()
	shows = Show.objects.all()
	return render(request, 'pages/show_list.html', {'djs':djs, 'shows':shows})