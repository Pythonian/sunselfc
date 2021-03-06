# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 17:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Maximum of 50 characters.', max_length=50, unique=True)),
                ('slug', models.SlugField(help_text='URL automatically generated from the title.', unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description for the Category. For S.E.O purposes.')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(help_text='An auto-generated label to be used in the URL.', max_length=250, unique=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images')),
                ('caption', models.CharField(blank=True, help_text='Image Caption. Optional', max_length=200)),
                ('excerpt', models.TextField(help_text='Summary of the Blog Post.')),
                ('body', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('impressions', models.PositiveIntegerField(default=0, help_text='Number of page views')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Maximum of 50 characters.', max_length=50, unique=True)),
                ('slug', models.SlugField(help_text='URL automatically generated from the title.', unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description for the Tag. For S.E.O purposes.')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
