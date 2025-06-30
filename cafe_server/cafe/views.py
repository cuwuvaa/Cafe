from django.shortcuts import render
from cafe.models import Dish

def index(request):
    dishes = Dish.objects.all()
    return render(request,"main/index.html", {"dishes":dishes})