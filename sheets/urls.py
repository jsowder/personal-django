from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.activity_view, name='activity-home'),
]
