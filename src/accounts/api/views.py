from django.contrib.auth import get_user_model

from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.api.serializers import UserProfileSerializer

User = get_user_model()


class UserProfileRetrieveUpdateView(RetrieveAPIView, UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)




