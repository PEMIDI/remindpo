from django.contrib import admin

from reminder.models import Category, Reminder


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['title', 'scheduled_at']
    search_fields = ['title', 'message']




