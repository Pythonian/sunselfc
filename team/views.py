from django.shortcuts import render, get_object_or_404

from .models import Player, Staff 

def players(request):
	section = 'players'

	goalkeepers = Player.objects.filter(
		position__iexact='Goalkeeper',
		status__iexact='Active')
	defenders = Player.objects.filter(
		position__iexact='Defender',
		status__iexact='Active')
	midfielders = Player.objects.filter(
		position__iexact='Midfielder',
		status__iexact='Active')
	strikers = Player.objects.filter(
		position__iexact='Striker',
		status__iexact='Active')

	return render(
		request,
		'club/players.html',
		locals())

def player(request, slug):
	section = 'player'

	player = get_object_or_404(Player,
		slug__iexact=slug)

	return render(
		request,
		'club/player.html',
		locals())

def crew(request):
	section = 'crew'

	crew = Staff.objects.filter(
		active=True,
		staff__iexact='TECHNICAL')

	return render(
		request,
		'club/crew.html',
		locals())

def management(request):
	section = 'management'

	management = Staff.objects.filter(
		active=True,
		staff__iexact='MANAGEMENT')

	return render(
		request,
		'club/management.html',
		locals())

def backroom(request):
	section = 'backroom'

	backroom = Staff.objects.filter(
		active=True,
		staff__iexact='BACKROOM')

	return render(
		request,
		'club/backroom.html',
		locals())

