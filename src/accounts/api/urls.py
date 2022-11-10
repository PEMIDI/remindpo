from django.urls import path

from accounts.api.views import UserProfileRetrieveUpdateView, UserRegistrationCreateAPIView, UserChangePasswordAPIView

urlpatterns = [
    path('profile/', UserProfileRetrieveUpdateView.as_view(), name='user-profile'),
    path('profile/changepassword', UserChangePasswordAPIView.as_view(), name='change-password'),
    path('register/', UserRegistrationCreateAPIView.as_view(), name='user-register'),
]
