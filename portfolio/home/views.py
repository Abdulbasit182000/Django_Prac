from django.shortcuts import render, HttpResponse
from project.models import Doctor


def home(request):
    # return HttpResponse('This is my homepage')
    context = {"name": "Basit", "Course": "Django"}
    return render(request, "home.html", context)


def about(request):
    # return HttpResponse('This is my about page')
    return render(request, "about.html")


def projects(request):
    # return HttpResponse('This is my project page')
    return render(request, "projects.html")


def contact(request):
    # return HttpResponse('This is my contact page')
    if request.method == "POST":
        name = request.POST["name"]
        specialization = request.POST["specialization"]
        phone = request.POST["phone"]
        print(name, specialization, phone)
        ins = Doctor(name=name, specialization=specialization, contact_number=phone)
        ins.save()
    return render(request, "contact.html")
