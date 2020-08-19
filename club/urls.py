from django.conf.urls import url 
from . import views


urlpatterns = [

	url(r'^$',
		views.home,
		name='home'),

	url(r'^videos/$',
		views.videos,
		name='videos'),

	url(r'^gallery/$',
		views.gallery,
		name='gallery'),

	url(r'^shop/$',
		views.shop,
		name='shop'),

	url(r'^contact/$',
		views.contact,
		name='contact'),




	# url(r'^team/players/$',
	# 	views.players,
	# 	name='players'),

]