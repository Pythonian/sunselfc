from django import template
from django.db.models import Count
import datetime
from django.utils.timezone import now as tz_now

register = template.Library()

from ..models import Post, Category, Tag


@register.assignment_tag
def get_latest_posts():    
    return Post.objects.all()[:3]

@register.assignment_tag
def get_popular_posts():
    return Post.objects.order_by(
        '-impressions')[:3]

@register.assignment_tag
def get_sidebar_categories():    
    return Category.objects.all()

@register.assignment_tag
def get_sidebar_tags():    
    return Tag.objects.all()

