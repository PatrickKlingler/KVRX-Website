from django.shortcuts import render, get_object_or_404
from .models import Page
from shows.models import Deejay, Show, Playlist, Song

# Page rendering methods here

#THIS IS A CONTEXT PROCESSOR
#DOCUMENTATION INCOMING
#FUCK YEAH I DID IT
def get_base_info(request):
	all_pages = Page.objects.filter(show_on_homepage=True)
	curr_track = Song.objects.get(current_track=True)
	primary_pages = all_pages[:5]
	secondary_pages = all_pages[5:]
	return {'p':primary_pages, 'p2':secondary_pages, 'curr_track':curr_track}

# Create your views here.

def base(request):
	return render(request, 'pages/base.html', {})

def index(request):
	return render(request, 'pages/index.html', {})

def custom_page(request, page):
	user_page = get_object_or_404(Page, page_url=page)
	return render(request, 'pages/details/page_detail.html', {'content': user_page})

def login(request):
	return render(request, 'pages/login.html', {})

def dj_detail(request, dj_name):
	dj_object = get_object_or_404(Deejay.objects.filter(dj__iexact=dj_name))
	show_objects = Show.objects.filter(dj=dj_object)
	return render(request, 'pages/details/dj_detail.html', {'dj':dj_object, 'shows':show_objects})

def show_detail(request, show_name):
	show_object = get_object_or_404(Show.objects.filter(show_name__iexact=show_name))
	playlists = Playlist.objects.filter(show=show_object)
	return render(request, 'pages/details/show_detail.html', {'show':show_object, 'playlists':playlists})

def shows(request):
	djs = Deejay.objects.all()
	shows = Show.objects.all()
	return render(request, 'pages/show_list.html', {'djs':djs, 'shows':shows})