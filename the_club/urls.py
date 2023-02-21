from django.urls import path
from . import views


urlpatterns = [

	path('history/',
		views.history,
		name='history'),

	path('stadium/',
		views.stadium,
		name='stadium'),

	path('achievements/',
		views.honors,
		name='honors'),

	path('sponsorships/',
		views.sponsorships,
		name='sponsorships'),


]