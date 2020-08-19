# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 17:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', ckeditor.fields.RichTextField()),
                ('history', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='the_club')),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='the_club')),
            ],
            options={
                'verbose_name_plural': 'Achievement',
            },
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='the_club')),
            ],
            options={
                'verbose_name_plural': 'Sponsorship',
            },
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Stadium',
            },
        ),
        migrations.CreateModel(
            name='StadiumPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='stadium')),
                ('caption', models.CharField(max_length=50)),
                ('stadium', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='the_club.Stadium')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('achievement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='the_club.Achievement')),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
    ]
