from django.urls import path

from . import views

app_name = 'main' # необходимо при использовании namespace

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
]
