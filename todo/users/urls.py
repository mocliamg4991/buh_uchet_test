from django.urls import path
from .views import RegistrationView, EmailLoginView, LogoutView,ChangePasswordView, PhoneLoginView
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    path('accounts/register', RegistrationView.as_view(), name='register'),
    path('accounts/login/email', EmailLoginView.as_view(), name='email_login'),
    path('accounts/login/phone', PhoneLoginView.as_view(), name='phone_login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('accounts/change-password', ChangePasswordView.as_view(), name='change_pass'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]