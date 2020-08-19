from django.conf.urls import url 

from . import views

urlpatterns = [

	url(r'^players/$',
		views.players,
		name='players'),

	url(r'^players/(?P<slug>[\w-]+)/$',
		views.player,
		name='player'),

	url(r'^technical-crew/$',
		views.crew,
		name='crew'),

	url(r'^club-management/$',
		views.management,
		name='management'),

	url(r'^backroom-staff/$',
		views.backroom,
		name='backroom'),


]