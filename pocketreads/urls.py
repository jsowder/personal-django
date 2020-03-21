from django.urls import path, include
from django.conf import settings
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.pocket_index, name='pocket-home'),
    path('more/<str:pocket_type>', views.get_more, name='pocket-more'),
]
