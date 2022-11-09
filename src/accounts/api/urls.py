from django.urls import include, path

from accounts.api.views import UserProfileRetrieveUpdateView

urlpatterns = [
    path('profile/', UserProfileRetrieveUpdateView.as_view(), name='user-profile')
]