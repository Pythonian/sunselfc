# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 17:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwayTeamStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possession', models.PositiveIntegerField(default=0)),
                ('shots', models.PositiveIntegerField(default=0)),
                ('shots_on_target', models.PositiveIntegerField(default=0)),
                ('corners', models.PositiveIntegerField(default=0)),
                ('saves', models.PositiveIntegerField(default=0)),
                ('offsides', models.PositiveIntegerField(default=0)),
                ('fouls', models.PositiveIntegerField(default=0)),
                ('yellow_card', models.PositiveIntegerField(default=0)),
                ('red_card', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_type', models.CharField(help_text='E.g: NPFL Matchday 1', max_length=50)),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField(blank=True, default='16:00:00', help_text='Default is 16:00:00 for 4p.m.', null=True)),
                ('venue', models.CharField(help_text='E.g. Lagos', max_length=50)),
                ('map_venue', models.TextField(blank=True, help_text='Embed the code of the map here.')),
                ('stadium', models.CharField(help_text='E.g. Teslim Balogun Stadium', max_length=50)),
                ('preview', ckeditor.fields.RichTextField(blank=True)),
                ('preview_video', models.TextField(blank=True, help_text='Embed the youtube video code here.')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixture_away_team', to='matches.Club')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fixture_home_team', to='matches.Club')),
            ],
            options={
                'ordering': ['match_date'],
                'get_latest_by': 'match_date',
            },
        ),
        migrations.CreateModel(
            name='HomeTeamStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possession', models.PositiveIntegerField(default=0)),
                ('shots', models.PositiveIntegerField(default=0)),
                ('shots_on_target', models.PositiveIntegerField(default=0)),
                ('corners', models.PositiveIntegerField(default=0)),
                ('saves', models.PositiveIntegerField(default=0)),
                ('offsides', models.PositiveIntegerField(default=0)),
                ('fouls', models.PositiveIntegerField(default=0)),
                ('yellow_card', models.PositiveIntegerField(default=0)),
                ('red_card', models.PositiveIntegerField(default=0)),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Club')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerLineup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.PositiveIntegerField(default=0)),
                ('goals', models.PositiveIntegerField(default=0)),
                ('assists', models.PositiveIntegerField(default=0)),
                ('yellow_card', models.PositiveIntegerField(default=0)),
                ('red_card', models.PositiveIntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_type', models.CharField(help_text='E.g: NPFL Matchday 1', max_length=50)),
                ('slug', models.SlugField(editable=False, max_length=200, unique=True)),
                ('home_team_score', models.PositiveIntegerField()),
                ('away_team_score', models.PositiveIntegerField()),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField(blank=True, default='16:00:00', help_text='Default is 16:00:00 for 4p.m.', null=True)),
                ('venue', models.CharField(help_text='E.g. Lagos', max_length=50)),
                ('stadium', models.CharField(help_text='E.g. Teslim Balogun Stadium', max_length=50)),
                ('review', ckeditor.fields.RichTextField(blank=True)),
                ('video_highlight', models.TextField(blank=True, help_text='Embed the youtube video code here.')),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_away_team', to='matches.Club')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_home_team', to='matches.Club')),
            ],
            options={
                'ordering': ['-match_date'],
                'get_latest_by': 'match_date',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='2016/ 2017 Nigerian Professional Football League', max_length=100)),
                ('year', models.PositiveIntegerField(help_text='2017')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.PositiveIntegerField(default=0)),
                ('assists', models.PositiveIntegerField(default=0)),
                ('appearances', models.PositiveIntegerField(default=0)),
                ('minutes', models.PositiveIntegerField(default=0)),
                ('yellow_card', models.PositiveIntegerField(default=0)),
                ('red_card', models.PositiveIntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Player')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Season'),
        ),
        migrations.AddField(
            model_name='playerlineup',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Result'),
        ),
        migrations.AddField(
            model_name='hometeamstatistic',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Result'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Season'),
        ),
        migrations.AddField(
            model_name='awayteamstatistic',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Club'),
        ),
        migrations.AddField(
            model_name='awayteamstatistic',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.Result'),
        ),
    ]