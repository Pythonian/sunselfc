from django.contrib import admin

from .models import Staff, Player


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
	pass

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ['name', 'squad_number', 'status', 'position']
	list_filter = ['status', 'position', 'availability']