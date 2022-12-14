from datetime import timedelta

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from reminder.api.paginations import StandardPagination
from reminder.api.permissions import UserObjectOwner
from reminder.api.serializers import ReminderSerializer
from reminder.models import Reminder


class ReminderModelViewSet(ModelViewSet):
    queryset = Reminder.objects.all()
    permission_classes = [IsAuthenticated, UserObjectOwner]
    serializer_class = ReminderSerializer
    pagination_class = StandardPagination
    lookup_field = 'pk'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user).select_related('category')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def snooze(self, request, *args, **kwargs):
        reminder = self.get_object()
        reminder.alert_time += timedelta(minutes=10)
        reminder.save()
        serializer = self.serializer_class(reminder)
        return Response(serializer.data)





