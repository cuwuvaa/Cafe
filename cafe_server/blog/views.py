from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django import forms
from .models import Post

class CreatePostForm(forms.Form):
    text = forms.CharField(label="Text (250 chars)", max_length=250)
    title_name = forms.CharField(label="Title of the post (64 chars)", max_length=64)

def blogpage(request):
    return render(request, "blog/mainpage.html", 
                  {"title_name":"Главная страница"})

def add_post(request):
    if request == "POST":
        NewPost = Post() 

        form = CreatePostForm(request.POST)

        title = form.cleaned_data["title"]
        text = form.cleaned_data["text"]
        NewPost.title = title
        NewPost.text = text

        NewPost.save()
        
        return render(request, "blog/createpost.html",
                {
                    "title_name":"Создать пост",
                    "form":form
                })
    else:
        form = CreatePostForm()
        return render(request, "blog/createpost.html",
                {
                    "title_name":"Создать пост",
                    "form":form
                })

