from django.urls import path
from django.views.generic.base import TemplateView

from . import views

app_name = 'sample'
urlpatterns = [
    path("some", views.some, name="some"),
]
