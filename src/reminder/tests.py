import json
from datetime import datetime, timedelta
import pdb

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory

from reminder.api.serializers import ReminderSerializer
from reminder.models import Reminder, Category

User = get_user_model()


class ReminderTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='pemidi', password='12345', email='rashidi.peman@gmail.com', )
        self.category = Category.objects.create(title='sample category')

        self.reminder = Reminder.objects.create(
            title='sample title', message='sample message', user=self.user, category=self.category,
            scheduled_at="2023-11-26T05:38:04Z", alert_time="2022-12-26T05:38:04Z"
        )
        self.client = APIClient()

    def test_reminder_existence(self):
        self.assertTrue(Reminder.objects.exists())
        self.assertTrue(Reminder.objects.count(), 1)

    def test_reminder_get_single_api_view(self):
        # with credentials 🔒
        check_login = self.client.login(username='pemidi', password='12345')
        self.assertTrue(check_login, 'login failed!')
        result = self.client.get(
            reverse('reminder-urls-detail', kwargs={'pk': self.reminder.pk})
        )
        serializer = ReminderSerializer(self.reminder)
        self.assertEqual(result.data, serializer.data)

    def test_reminder_creation_api_view(self):
        reminder_data = {
            "title": "sample title 2",
            "message": "sample message",
            "category": {"title": "category 99"},
            "scheduled_at": self.reminder.scheduled_at,
            "alert_time": self.reminder.alert_time,
        }
        result = self.client.post('/api/app/reminder/', reminder_data, format='json')
        self.assertEqual(result.status_code, 403, "API is for authenticated users only")
        # with credentials 🔒
        check_login = self.client.login(username='pemidi', password='12345')
        self.assertTrue(check_login, 'login failed!')
        result = self.client.post('/api/app/reminder/', reminder_data, format='json')
        self.assertEqual(result.status_code, 201, f"Status code is wrong ")

    def test_reminder_update_api_view(self):
        reminder_data = {
            "title": "sample title 2",
            "message": "sample message 2",
            "category": {"title": "category 100"},
            "scheduled_at": self.reminder.scheduled_at,
            "alert_time": self.reminder.alert_time,
        }

        result = self.client.put(reverse('reminder-urls-detail', kwargs={'pk': self.reminder.pk}),
                                 data=json.dumps(reminder_data), content_type='application/json')
        self.assertEqual(result.status_code, 403, "API is for authenticated users only")
        # with credentials 🔒
        check_login = self.client.login(username='pemidi', password='12345')
        self.assertTrue(check_login, 'login failed!')
        result = self.client.put(reverse('reminder-urls-detail', kwargs={'pk': self.reminder.pk}),
                                 data=json.dumps(reminder_data), content_type='application/json')
        self.assertEqual(result.status_code, 200, f"Status code is wrong ")

    def test_reminder_delete_api_view(self):
        result = self.client.delete(reverse(
            'reminder-urls-detail', kwargs={'pk': self.reminder.pk}), content_type='application/json'
        )
        self.assertEqual(result.status_code, 403, "API is for authenticated users only")
        # with credentials 🔒
        check_login = self.client.login(username='pemidi', password='12345')
        self.assertTrue(check_login, 'login failed!')
        result = self.client.delete(reverse(
            'reminder-urls-detail', kwargs={'pk': self.reminder.pk}), content_type='application/json'
        )
        self.assertEqual(result.status_code, 204, f"Status code is wrong ")

