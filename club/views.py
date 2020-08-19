from django.shortcuts import render

from club_media.models import Photo, Video 
from team.models import Player



def home(request):
	section = 'home'

	photos  = Photo.objects.all()[:8]
	players = Player.objects.filter(
		status__iexact='Active')[:4]

	return render(
		request,
		'club/home.html',
		locals())


def shop(request):
	section = 'shop'

	return render(
		request,
		'club/shop.html',
		locals())

def contact(request):
	section = 'contact'

	return render(
		request,
		'club/contact.html',
		locals())

def videos(request):
	section = 'videos'

	videos = Video.objects.all()

	return render(
		request,
		'club/videos.html',
		locals())

def gallery(request):
	section = 'gallery'

	photos  = Photo.objects.all()

	return render(
		request,
		'club/gallery.html',
		locals())



