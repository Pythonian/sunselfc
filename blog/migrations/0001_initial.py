# Generated by Django 4.1.7 on 2023-02-21 09:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Maximum of 50 characters.', max_length=50, unique=True)),
                ('slug', models.SlugField(help_text='URL automatically generated from the title.', unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description for the Category. For S.E.O purposes.')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Maximum of 50 characters.', max_length=50, unique=True)),
                ('slug', models.SlugField(help_text='URL automatically generated from the title.', unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description for the Tag. For S.E.O purposes.')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(help_text='An auto-generated label to be used in the URL.', max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='images')),
                ('caption', models.CharField(blank=True, help_text='Image Caption. Optional', max_length=200)),
                ('excerpt', models.TextField(help_text='Summary of the Blog Post.')),
                ('body', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('impressions', models.PositiveIntegerField(default=0, help_text='Number of page views')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, to='blog.tag')),
            ],
            options={
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
    ]
