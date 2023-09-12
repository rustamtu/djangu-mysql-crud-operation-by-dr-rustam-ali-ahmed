from django.urls import path

from . import views as polls_view

urlpatterns = [
    path("polls/", polls_view.index, name="index"),
    path("p/", polls_view.index, name="index"),
    path("raa/", polls_view.raa, name="raa"),
]