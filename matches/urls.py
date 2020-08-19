from django.conf.urls import url 

from . import views

urlpatterns = [

	url(r'^fixtures/$',
		views.fixtures,
		name='fixtures'),

	url(r'^fixtures/preview/(?P<slug>[-\w]+)/$',
		views.preview,
		name='preview'),

	url(r'^results/$',
		views.results,
		name='results'),

	url(r'^results/review/(?P<slug>[-\w]+)/$',
		views.review,
		name='review'),

	url(r'^table/$',
		views.table,
		name='table'),

	url(r'^statistics/$',
		views.statistics,
		name='statistics'),


]