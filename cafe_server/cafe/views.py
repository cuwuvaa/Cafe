from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from django.urls import reverse
from cafe.models import Dish

class SendDishForm(forms.Form):
    name = forms.CharField(max_length=64)
    rating = forms.IntegerField(max_value=10)

def index(request):
    dishes = Dish.objects.all()
    return render(request,"main/index.html", {"dishes":dishes})

def add_dish(request):
    if request.method == "POST":
        form = SendDishForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data["name"]
            frating = form.cleaned_data["rating"]
            s = Dish(name=fname, rating = frating).save()
            return HttpResponseRedirect(reverse('cafe:main'))
    else:
        form = SendDishForm()
        
    return render(request, "main/add.html", {"form":form})