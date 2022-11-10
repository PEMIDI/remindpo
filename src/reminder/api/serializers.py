from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.api.serializers import UserProfileSerializer
from reminder.models import Reminder, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']


class ReminderSerializer(WritableNestedModelSerializer):
    user = UserProfileSerializer(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Reminder
        fields = ['id', 'title', 'message', 'category', 'user', 'scheduled_at', 'alert_time']

    def validate(self, attrs):
        if attrs.get('alert_time') > attrs.get('scheduled_at'):
            raise ValidationError('error: alert you entered is greater than scheduled time')
        return attrs
