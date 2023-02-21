from django.urls import path 
from . import views


urlpatterns = [

	path('',
		views.home,
		name='home'),

	path('videos/',
		views.videos,
		name='videos'),

	path('gallery/',
		views.gallery,
		name='gallery'),

	path('shop/',
		views.shop,
		name='shop'),

	path('contact/',
		views.contact,
		name='contact'),




	# url(r'^team/players/$',
	# 	views.players,
	# 	name='players'),

]