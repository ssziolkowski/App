from django.urls import path

from . import views

app_name = 'mc_cloud'

urlpatterns = [
    path("", views.text_generation, name="text_generation"),
]