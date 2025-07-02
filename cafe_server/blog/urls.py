from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blogpage, name="main"),
    path("new", views.add_post, name="new_post")
]