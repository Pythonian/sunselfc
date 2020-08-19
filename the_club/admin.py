from django.contrib import admin

from .models import About, Timeline, Achievement, Stadium, StadiumPhoto, Sponsorship


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	pass

@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
	pass


class TimelineAdminInline(admin.TabularInline):
	model = Timeline
	extra = 0

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
	inlines = [TimelineAdminInline]


class StadiumPhotoAdminInline(admin.TabularInline):
	model = StadiumPhoto
	extra = 0

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
	inlines = [StadiumPhotoAdminInline]

