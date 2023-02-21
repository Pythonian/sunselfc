from django.urls import path 

from . import views

urlpatterns = [

	path('fixtures/',
		views.fixtures,
		name='fixtures'),

	path('fixtures/preview/<slug:slug>/',
		views.preview,
		name='preview'),

	path('results/',
		views.results,
		name='results'),

	path('results/review/<slug:slug>/',
		views.review,
		name='review'),

	path('table/',
		views.table,
		name='table'),

	path('statistics/',
		views.statistics,
		name='statistics'),


]