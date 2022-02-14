from django.contrib import admin

from exam3.main_app.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
