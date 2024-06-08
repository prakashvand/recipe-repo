from django.contrib import admin
from django.urls import path
from user import views
#from rest_framework_simplejwt.models import TokenUser


urlpatterns = [
    path('account/user-create/', views.UserCreateAPI.as_view()),
    path('login-user/', views.LoginUserAPI.as_view()),
]
