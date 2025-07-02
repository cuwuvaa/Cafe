from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django import forms
from .models import Post

class CreatePostForm(forms.Form):
    text = forms.CharField(label="Text (250 chars)", max_length=250)
    title = forms.CharField(label="Title of the post (64 chars)", max_length=64)

def blogpage(request):
    posts = Post.objects.all()
    return render(request, "blog/mainpage.html", 
                  {
                      "title_name":"Главная страница",
                      "posts":posts
                    })

def add_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            formated_title = form.cleaned_data["title"]
            formated_text = form.cleaned_data["text"]
            NewPost = Post(title=formated_title, text=formated_text, date=datetime.now()).save()
            return HttpResponseRedirect(reverse('blog:main'))
    else:
        form = CreatePostForm()
        return render(request, "blog/createpost.html",
                {
                    "title_name":"Создать пост",
                    "form":form
                })

