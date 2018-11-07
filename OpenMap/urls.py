from django.contrib import admin

from django.urls import path, include
from .views import *


app_name = 'OpenMap'
urlpatterns = [
    path('', home_view, name='home'),
    path('projects/', project_Page, name='project'),

]
