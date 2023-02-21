from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from .models import Post


class BaseLatestPostFeed(Feed):
    title = "Latest Blog Post Feed"
    link = '/'
    description = "Stay up to date with my latest blog post."

    def items(self):
        return Post.objects.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_created(self, item):
        return item.created

class AtomPostFeed(BaseLatestPostFeed, Feed):
    feed_type = Atom1Feed


class Rss2PostFeed(BaseLatestPostFeed, Feed):
    feed_type = Rss201rev2Feed


