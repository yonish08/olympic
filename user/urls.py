from django.urls import path
from .views import (
    ClientRegisterView,
    UserLoginView,
    UserLogoutView
)

app_name = 'user'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', ClientRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]