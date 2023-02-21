from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from . import views
from .models import Post 
from .feeds import AtomPostFeed, Rss2PostFeed

info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'created',
}


urlpatterns = [
    path('',
        views.news,
        name='news'),

    path('<year>/<month>/<day>/<slug>/',
        views.post,
        name='news'),

    path('category/<slug>/',
        views.category,
        name='category'),

    path('tag/<slug>/',
        views.tag,
        name='tag'),

    path('rss/', 
        Rss2PostFeed(),
        name='rss'),

    path('atom/',
        AtomPostFeed(),
        name='atom'),

    path('sitemap\.xml', 
        sitemap,
        {'sitemaps': {'post': GenericSitemap(info_dict, priority=0.5)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
