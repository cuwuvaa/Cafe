from django.shortcuts import render

my_list = ["поехать в евпаторию", "погулять", "на море"]

def list_tasks(request):
    return render(request, "list_tasks.html", {"list":my_list})