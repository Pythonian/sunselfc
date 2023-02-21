from django import template

register = template.Library()

from ..models import Fixture, Result


@register.simple_tag
def get_upcoming_fixtures():    
    return Fixture.objects.all()[:3]

@register.simple_tag
def get_latest_results():    
    return Result.objects.all()[:3]



# @register.simple_tag
# def get_popular_posts():
#     return Post.objects.order_by(
#         '-impressions')[:3]

# @register.simple_tag
# def get_sidebar_categories():    
#     return Category.objects.all()

# @register.simple_tag
# def get_sidebar_tags():    
#     return Tag.objects.all()

