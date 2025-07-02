from django.urls import path
from . import views


app_name = "cafe"
urlpatterns = [
    path("", views.index, name="main"),
    path("add", views.add_dish, name="add_dish")
]