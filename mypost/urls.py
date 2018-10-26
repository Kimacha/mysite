from django.contrib import admin

from django.urls import path

from mypost.views import myproject

urlpatterns = [
    path('', myproject, ),
]
