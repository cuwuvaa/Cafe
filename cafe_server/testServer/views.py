from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hello(request):
    return HttpResponse(f"Hello!")

def hello_user(request, name):
    return render(request, "index.html", {"msg":name.capitalize(), "year":datetime.datetime.now().year})

