from django.contrib import admin
from django.urls import path, include
from AppTwo import views

urlpatterns = [
    path('', views.users, name='users'),
    path('', views.signUp, name='signUp'),
]
