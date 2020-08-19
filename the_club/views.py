from django.shortcuts import render


from .models import About, Stadium, Achievement, Sponsorship


def history(request):
	section = 'history'

	try:
		about = About.objects.get()
	except About.DoesNotExist:
		pass

	return render(
		request,
		'club/history.html',
		locals())

def stadium(request):
	section = 'stadium'

	try:
		stadium = Stadium.objects.get()
	except Stadium.DoesNotExist:
		pass

	return render(
		request,
		'club/stadium.html',
		locals())

def honors(request):
	section = 'honors'

	try:
		achievement = Achievement.objects.get()
	except Achievement.DoesNotExist:
		pass

	return render(
		request,
		'club/honors.html',
		locals())

def sponsorships(request):
	section = 'sponsorships'

	try:
		sponsorship = Sponsorship.objects.get()
	except Sponsorship.DoesNotExist:
		pass

	return render(
		request,
		'club/sponsorships.html',
		locals())

