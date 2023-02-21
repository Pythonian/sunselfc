import datetime

from django.urls import reverse
from django.core.paginator import (Paginator, 
    InvalidPage, EmptyPage)
from django.db import models
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.dates import (
    YearArchiveView, MonthArchiveView, DayArchiveView)
from django.utils.text import slugify

from .models import Category, Post, Tag


PAGINATION = 9

def mk_paginator(request, items, num_items):
    '''Create and return a paginator.'''
    paginator = Paginator(items, num_items)
    try: 
        page = int(request.GET.get('page', '1'))
    except ValueError: 
        page = 1
    try: 
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items

def news(request):
    section = 'news'
    post_list = Post.objects.all()
    post_list = mk_paginator(request, post_list, PAGINATION)
    
    return render(
        request,
        'club/news.html',
        locals())

def post(request, year, month, day, slug):
    queryset = Post.objects.filter(
        slug__iexact=slug,
        created__year=year,
        created__month=month,
        created__day=day)
    if request:
        queryset.update(impressions=models.F("impressions") + 1)
    post = get_object_or_404(queryset)
    # Similar posts
    post_tags_ids = post.tags.values_list(
        'id', flat=True)
    similar_posts = Post.objects.filter(
        tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(
        same_tags=Count('tags')).order_by(
            '-same_tags', '-created')[:2]
    return render(
        request,
        'club/post.html',
        locals())

    
def category(request, slug):
    category = get_object_or_404(
        Category, slug__iexact=slug)
    post_list = Post.objects.filter(
        category=category)
    post_list = mk_paginator(request, post_list, PAGINATION)
    return render(
        request,
        'club/category.html',
        locals())

def tags(request):
	tag_list = Tag.objects.all()
	return render(
		request,
		'club/tags.html',
		locals())

def tag(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    post_list = Post.objects.filter(
        tags=tag)
    post_list = mk_paginator(request, post_list, PAGINATION)
    return render(
        request,
        'club/tag.html',
        locals())


    