from django.contrib import admin

from reminder.models import Alert, Category, Reminder, ReminderCategory


class AlertInline(admin.TabularInline):
    model = Alert


class ReminderCategoryInline(admin.TabularInline):
    model = ReminderCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['title', 'scheduled_at']
    search_fields = ['title', 'message']

    inlines = [AlertInline, ReminderCategoryInline]



