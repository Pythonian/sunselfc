from django.urls import path 

from . import views

urlpatterns = [

	path('players/',
		views.players,
		name='players'),

	path('players/<slug:slug>/',
		views.player,
		name='player'),

	path('technical-crew/',
		views.crew,
		name='crew'),

	path('club-management/',
		views.management,
		name='management'),

	path('backroom-staff/',
		views.backroom,
		name='backroom'),


]