# users/urls.py
"""This is the url route for app users"""
from django.urls import path

from user import views

app_name = 'user'
urlpatterns = [
    path('create/', views.SignupView.as_view(), name='signup'),
]