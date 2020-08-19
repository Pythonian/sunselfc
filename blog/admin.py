from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User 
from .models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'get_tags', 'created']
    list_filter = ['created', 'category']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    fieldsets = (
        ('Post Entry', {
            'fields': ('title', 'slug', 'image', 'caption', 'excerpt', 'body')
        }),
        ('Meta', {
            'fields': ('category', 'tags')
        }),
        ('Utility', {
            'classes': ('collapse',),
            'fields': ('impressions',)
        }),
    )

