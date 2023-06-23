from django.urls import path
from .views import (
    ClientRegisterView,
    UserLoginView,
    UserLogoutView,
    ActivateAccountView,
)
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', ClientRegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # password reset
    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset.html'),name='password-reset'),
    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset.html',html_email_template_name='account/password_reset_email.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]