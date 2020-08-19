from django.conf.urls import url
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
    url(r'^$',
        views.news,
        name='news'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
        views.post,
        name='news'),

    url(r'^category/(?P<slug>[-\w]+)/$',
        views.category,
        name='category'),

    url(r'^tag/(?P<slug>[-\w]+)/$',
        views.tag,
        name='tag'),

    url(r'^rss/$', 
        Rss2PostFeed(),
        name='rss'),

    url(r'^atom/$',
        AtomPostFeed(),
        name='atom'),

    url(r'^sitemap\.xml$', 
        sitemap,
        {'sitemaps': {'post': GenericSitemap(info_dict, priority=0.5)}},
        name='django.contrib.sitemaps.views.sitemap'),
]
