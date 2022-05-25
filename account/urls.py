
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth.views import LogoutView
from account import views
urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view()),
    path('activate/<uuid:activation_code>/', views.ActivationView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('logout/', views.LogoutApiView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('change_password/', views.NewPasswordView.as_view()),
    path('reset_password/', views.ResetPasswordView.as_view())
]

