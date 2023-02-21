# Python libraries
import datetime

# Django modules
from django.urls import reverse
from django.db import models
from django.utils.text import slugify

# Third-party Django apps
from ckeditor.fields import RichTextField

from team.models import Player
from league.models import Team


# class Club(models.Model):
#     name = models.CharField(
#         max_length=50)
#     logo = models.ImageField(
#         upload_to='logos',
#         blank=True,
#         null=True)
#     active = models.BooleanField(
#         default=True) # my_team

#     class Meta:
#         ordering = ['name']

#     def __str__(self):
#         return self.name 


class Season(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='2016/ 2017 Nigerian Professional Football League')
    year = models.PositiveIntegerField(
        help_text='2017')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class FixtureManager(models.Manager):
    def get_queryset(self):
        return super(FixtureManager, self).get_queryset().filter(
            match_date__gte=datetime.datetime.now())

class Fixture(models.Model):
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE)
    match_type = models.CharField(
        max_length=50,
        help_text="E.g: NPFL Matchday 1")
    slug = models.SlugField(
        max_length=200,
        unique=True,
        editable=False)
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="fixture_home_team")
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="fixture_away_team")
    match_date = models.DateField()
    match_time = models.TimeField(
        default='16:00:00',
        help_text="Default is 16:00:00 for 4p.m.",
        blank=True,
        null=True)
    venue = models.CharField(
        max_length=50,
        help_text='E.g. Lagos')
    map_venue = models.TextField(
        blank=True,
        help_text='Embed the code of the map here.')
    stadium = models.CharField(
        max_length=50,
        help_text='E.g. Teslim Balogun Stadium')
    preview = RichTextField(
        blank=True)
    preview_video = models.TextField(
        blank=True,
        help_text='Embed the youtube video code here.')


    objects = FixtureManager()

    class Meta:
        ordering = ['match_date']
        get_latest_by = 'match_date'

    def __str__(self):
        return "%s v %s - %s" % (
            self.home_team, self.away_team, self.match_type)

    def get_absolute_url(self):
        return reverse(
            'preview',
            args=[self.slug]) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.home_team) + "-vs-" + slugify(self.away_team) + "-" + slugify(self.season.year) + "-" + slugify(self.match_type)
        super(Fixture, self).save(*args, **kwargs)



class ResultManager(models.Manager):
    def get_queryset(self):
        return super(ResultManager, self).get_queryset().filter(
            match_date__lte=datetime.datetime.now())

class Result(models.Model):
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE)
    match_type = models.CharField(
        max_length=50,
        help_text="E.g: NPFL Matchday 1")
    slug = models.SlugField(
        max_length=200,
        unique=True,
        editable=False)
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="result_home_team")
    home_team_score = models.PositiveIntegerField()
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="result_away_team")
    away_team_score = models.PositiveIntegerField()
    match_date = models.DateField()
    match_time = models.TimeField(
        default='16:00:00',
        help_text="Default is 16:00:00 for 4p.m.",
        blank=True,
        null=True)
    venue = models.CharField(
        max_length=50,
        help_text='E.g. Lagos')
    stadium = models.CharField(
        max_length=50,
        help_text='E.g. Teslim Balogun Stadium')
    review = RichTextField(
        blank=True)
    video_highlight = models.TextField(
        blank=True,
        help_text='Embed the youtube video code here.')
    
    objects = ResultManager()

    class Meta: 
        ordering = ['-match_date']
        get_latest_by = 'match_date'

    def __str__(self):
        return "%s %d:%d %s" % (
            self.home_team, self.home_team_score,
            self.away_team_score, self.away_team)

    def get_absolute_url(self):
        return reverse(
            'review',
            args=[self.slug]) 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.home_team) + "-" + slugify(self.home_team_score) + "-" + slugify(self.away_team_score) + "-" + slugify(self.away_team) + "-" + slugify(self.season.year) + "-" + slugify(self.match_type)
        super(Result, self).save(*args, **kwargs)


class PlayerLineup(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    minutes = models.PositiveIntegerField(
        default=0)
    goals = models.PositiveIntegerField(
        default=0)
    assists = models.PositiveIntegerField(
        default=0)
    yellow_card = models.PositiveIntegerField(
        default=0)
    red_card = models.PositiveIntegerField(
        default=0)

    def __str__(self):
        return self.player.name


class HomeTeamStatistic(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    possession = models.PositiveIntegerField(
        default=0)
    shots = models.PositiveIntegerField(
        default=0)
    shots_on_target = models.PositiveIntegerField(
        default=0)
    corners = models.PositiveIntegerField(
        default=0)
    saves = models.PositiveIntegerField(
        default=0)
    offsides = models.PositiveIntegerField(
        default=0)
    fouls = models.PositiveIntegerField(
        default=0)
    yellow_card = models.PositiveIntegerField(
        default=0)
    red_card = models.PositiveIntegerField(
        default=0)

    def __str__(self):
        return self.home_team.name 


class AwayTeamStatistic(models.Model):
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    possession = models.PositiveIntegerField(
        default=0)
    shots = models.PositiveIntegerField(
        default=0)
    shots_on_target = models.PositiveIntegerField(
        default=0)
    corners = models.PositiveIntegerField(
        default=0)
    saves = models.PositiveIntegerField(
        default=0)
    offsides = models.PositiveIntegerField(
        default=0)
    fouls = models.PositiveIntegerField(
        default=0)
    yellow_card = models.PositiveIntegerField(
        default=0)
    red_card = models.PositiveIntegerField(
        default=0)

    def __str__(self):
        return self.away_team.name 


class Statistic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goals = models.PositiveIntegerField(
        default=0)
    assists = models.PositiveIntegerField(
        default=0)
    appearances = models.PositiveIntegerField(
        default=0)
    minutes = models.PositiveIntegerField(
        default=0)
    yellow_card = models.PositiveIntegerField(
        default=0)
    red_card = models.PositiveIntegerField(
        default=0)

    def __str__(self):
        return self.player.name 

# class ClubIndex(models.Model):
#     club = models.ForeignKey(
#         Club)
#     played = models.PositiveIntegerField()
#     wins = models.PositiveIntegerField()
#     draws = models.PositiveIntegerField()
#     loss = models.PositiveIntegerField()
#     goals_for = models.PositiveIntegerField()
#     goals_against = models.PositiveIntegerField()
#     goals_difference = models.IntegerField()
#     points = models.PositiveIntegerField()

#     def __unicode__(self):
#         return "For: %s" % self.club.name

#     class Meta:
#     	verbose_name = 'Club Rank'
#         verbose_name_plural = 'Club Ranks'
#         ordering = ['-points', '-goals_difference', '-goals_for', 'club']

