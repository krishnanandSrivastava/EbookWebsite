from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signUp', views.index,name='signUp'),
    path('handleSignup', views.reg),
]
