"""Urls file."""
from django.urls import path

from frontend.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
