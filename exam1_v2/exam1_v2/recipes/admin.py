from django.contrib import admin

from exam1_v2.recipes.models import Recipe


@admin.register(Recipe)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'time')
