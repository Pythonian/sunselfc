from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^history/$',
		views.history,
		name='history'),

	url(r'^stadium/$',
		views.stadium,
		name='stadium'),

	url(r'^achievements/$',
		views.honors,
		name='honors'),

	url(r'^sponsorships/$',
		views.sponsorships,
		name='sponsorships'),


]