from django.contrib import admin
from notes.models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'body', 'status']
    list_filter = ['created', 'updated', 'user']
