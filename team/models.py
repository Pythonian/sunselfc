from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse


class Staff(models.Model):
	STAFF_TYPES = (
		('TECHNICAL', 'Technical Crew'),
		('MANAGEMENT', 'Club Management'),
		('BACKROOM', 'Backroom Staff'),
	)
	name = models.CharField(
		max_length=100)
	image = models.ImageField(
		upload_to='staff')
	staff = models.CharField(
		max_length=20,
		choices=STAFF_TYPES)
	position = models.CharField(
		max_length=100)
	active = models.BooleanField(
		default=True,
		help_text='Uncheck this if the Official is no longer with the club.')

	class Meta:
		ordering = ['name', 'staff']

	def __str__(self):
		return self.name 


class Player(models.Model):
	POSITION_TYPES = (
		('GOALKEEPER', 'Goalkeeper'),
		('DEFENDER', 'Defender'),
		('MIDFIELDER', 'Midfielder'),
		('STRIKER', 'Striker'),
	)
	STATUS_TYPES = (
		('ACTIVE', 'Active'),
		('LOAN', 'On Loan'),
		('SOLD', 'Sold'),
	)
	AVAILABILITY_TYPES = (
		('INJURED', 'Injured'),
		('SUSPENDED', 'Suspended'),
		('LEAVE', 'On Leave'),
	)
	name = models.CharField(
		max_length=100,
		unique=True)
	slug = models.SlugField(
		max_length=50,
		unique=True)
	squad_number = models.PositiveIntegerField(
		blank=True,
		null=True)
	image = models.ImageField(
		upload_to='players')
	position = models.CharField(
		max_length=15,
		choices=POSITION_TYPES,
		blank=True)
	status = models.CharField(
		max_length=15,
		choices=STATUS_TYPES,
		blank=True)
	availability = models.CharField(
		max_length=15,
		choices=AVAILABILITY_TYPES,
		blank=True)
	club_appearances = models.PositiveIntegerField(
		blank=True,
		null=True,
		help_text='Total club appearances since joining the club.')
	goals = models.PositiveIntegerField(
		blank=True,
		null=True,
		help_text='Total goals since joining the club.')
	nationality = models.CharField(
		max_length=50,
		blank=True)
	yellow_cards = models.PositiveIntegerField(
		blank=True,
		null=True,
		help_text='Total yellow cards since joining the club.')
	red_cards = models.PositiveIntegerField(
		blank=True,
		null=True,
		help_text='Total red cards since joining the club.')
	date_of_birth = models.DateField(
		blank=True,
		null=True)
	height = models.CharField(
		max_length=10,
		blank=True,
		help_text='Height in cm.')
	weight = models.CharField(
		max_length=10,
		blank=True,
		help_text='Weight in kg.')
	previous_clubs = models.CharField(
		max_length=255,
		blank=True)
	biography = RichTextField(
		blank=True)

	class Meta:
		ordering = ['squad_number']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('player',
			kwargs={'slug': self.slug})
