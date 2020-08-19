from django.contrib import admin
from .models import Club, Fixture, Season, Result, AwayTeamStatistic, HomeTeamStatistic, PlayerLineup, Statistic


class ClubAdmin(admin.ModelAdmin):
	list_display = ['name', 'active']
	list_filter = ['active']
	search_fields = ['name']

admin.site.register(Club, ClubAdmin)

class FixtureAdmin(admin.ModelAdmin):
	list_display = ['match_type', 'season']

admin.site.register(Fixture, FixtureAdmin)


admin.site.register(Season)


class HomeTeamStatisticInline(admin.TabularInline):
	model = HomeTeamStatistic
	extra = 0

class AwayTeamStatisticInline(admin.TabularInline):
	model = AwayTeamStatistic
	extra = 0

class PlayerLineupInline(admin.TabularInline):
	model = PlayerLineup
	extra = 1

class ResultAdmin(admin.ModelAdmin):
	inlines = [PlayerLineupInline, HomeTeamStatisticInline, AwayTeamStatisticInline]

admin.site.register(Result, ResultAdmin)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
	list_display = ['player', 'goals', 'assists', 'appearances', 'minutes', 'yellow_card', 'red_card']
	list_editable = ['player', 'goals', 'assists', 'appearances', 'minutes', 'yellow_card', 'red_card']
