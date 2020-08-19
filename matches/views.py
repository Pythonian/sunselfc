from django.shortcuts import render, get_object_or_404

from .models import Fixture, Result, Statistic
from LeagueTable.models import Standings


def fixtures(request):
	section = 'fixtures'

	fixtures = Fixture.objects.all()[:10]

	return render(
		request,
		'club/fixtures.html',
		locals())

def preview(request, slug):
	section = 'preview'

	preview = get_object_or_404(
		Fixture, slug=slug)

	return render(
		request,
		'club/preview.html',
		locals())

def results(request):
	section = 'results'

	results = Result.objects.all()

	return render(
		request,
		'club/results.html',
		locals())

def review(request, slug):
	section = 'review'

	review = get_object_or_404(
		Result, slug=slug)

	return render(
		request,
		'club/review.html',
		locals())

def table(request):
	section = 'table'
	standings = Standings.objects.all()

	return render(
		request,
		'club/table.html',
		locals())

def statistics(request):
	section = 'statistics'

	players = Statistic.objects.all()

	return render(
		request,
		'club/statistics.html',
		locals())
