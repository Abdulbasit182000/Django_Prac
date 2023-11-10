from django.shortcuts import render, HttpResponse
from home.models import Contact


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
        email = request.POST["email"]
        phone = request.POST["phone"]
        print(name, email, phone)
        ins = Contact(name=name, email=email, phone=phone)
        ins.save()
    return render(request, "contact.html")
