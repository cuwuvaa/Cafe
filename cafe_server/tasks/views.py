from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse


class NewTaskForm(forms.Form): 
    task = forms.CharField(label="Имя задачи")

def list_tasks(request):
    if "list" not in request.session:
        request.session["list"] = []
    return render(request, "list_tasks.html", {"list":request.session["list"]})

def add_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid(): 
            task = form.cleaned_data["task"]
            request.session["list"].append(task)
            return HttpResponseRedirect(reverse("tasks:list"))
    return render(request, "new_task.html", {"form":NewTaskForm()})