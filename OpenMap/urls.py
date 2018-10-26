from django.contrib import admin

from django.urls import path, include
from .views import *

admin.site.site_header = "OpenMap Development Tanzania"
admin.site.site_title = "OMDTZ"

urlpatterns = [
    path('', home_view, name='home'),
]
