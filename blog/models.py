# Python libraries
from __future__ import unicode_literals
import datetime

# Django modules
from django.contrib.sitemaps import ping_google
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible

# Third-party Django apps
from ckeditor.fields import RichTextField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text='Maximum of 50 characters.')
    slug = models.SlugField(
        unique=True,
        help_text='URL automatically generated from the title.')
    description = models.TextField(
        blank=True,
        help_text='Optional description for the Category. For S.E.O purposes.')

    class Meta:
        ordering = ['title']
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'category',
            args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Tag(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text='Maximum of 50 characters.')
    slug = models.SlugField(
        unique=True,
        help_text='URL automatically generated from the title.')
    description = models.TextField(
        blank=True,
        help_text='Optional description for the Tag. For S.E.O purposes.')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'tag',
            args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Post(models.Model):
    """
    Stores a single blog post.
    """
    title = models.CharField(
    	max_length=250,
    	unique=True)
    slug = models.SlugField(
        max_length=250,
        unique=True,
        help_text='An auto-generated label to be used in the URL.')
    # image = ProcessedImageField(
    #     upload_to="images",
    #     processors = [ResizeToFill(750, 400)],
    #     format = 'JPEG',
    #     options = {'quality': 100})
    image = models.ImageField(
        upload_to="images")
    caption = models.CharField(
        max_length=200,
        blank=True,
        help_text="Image Caption. Optional")
    excerpt = models.TextField(
        help_text='Summary of the Blog Post.')
    body = RichTextField()
    created = models.DateTimeField(
        auto_now_add=True)
    updated = models.DateTimeField(
    	auto_now=True)
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True)
    tags = models.ManyToManyField(
    	Tag,
    	blank=True)
    impressions = models.PositiveIntegerField(
        default=0,
        help_text='Number of page views')

    def get_tags(self):
        return ', '.join([t.title for t in self.tags.all()[:5]])
    get_tags.short_description = 'Tags'

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'

    def get_previous_post(self):
        return self.get_previous_by_created()

    def get_next_post(self):
        return self.get_next_by_created()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'news',
            args=[self.created.year,
                  self.created.strftime('%m'),
                  self.created.strftime('%d'),
                  self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
	        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        # Ping google due to sitemap changes that
        # arises from a new Post being created.
        try:
            ping_google()
        except Exception:
            pass

