from django.urls import path
from .views import UserDetailView, UserRegistrationView

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]