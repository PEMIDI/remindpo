from django.urls import path
from rest_framework import routers

from reminder.api.views import ReminderModelViewSet

router = routers.SimpleRouter()
router.register('reminder', ReminderModelViewSet, basename='reminder-urls')


urlpatterns = [

] + router.urls
