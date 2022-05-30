from . import views
from django.urls import path

urlpatterns = [
    path("", views.main, name="main"),
    path("<str:name>", views.greet, name="greet")
]

