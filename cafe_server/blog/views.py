from django.shortcuts import render

def blogpage(request):
    return render(request, "blog/mainpage.html", {"title_name":"Главная страница"})


