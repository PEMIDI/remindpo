from rest_framework import serializers

from accounts.api.serializers import UserProfileSerializer
from reminder.models import Reminder, Alert, Category, ReminderCategory


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = ['id', 'alert_time', 'is_active']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']


class ReminderCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ReminderCategory
        fields = ['category']


class ReminderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    alerts = AlertSerializer(many=True)
    categories = ReminderCategorySerializer(many=True)

    class Meta:
        model = Reminder
        fields = ['id', 'user', 'title', 'message', 'categories', 'scheduled_at', 'alerts']



