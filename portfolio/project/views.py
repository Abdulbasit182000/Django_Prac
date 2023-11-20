from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from project.models import Doctor, Nurse, Patient
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Publisher, Book, Author
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DoctorSerializer,NurseSerializer, PatientSerializer
from django.db.models import Q


def home(request):
    context = {"name": "Basit", "Course": "Django"}
    return render(request, "test.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        specialization = request.POST["specialization"]
        phone = request.POST["phone"]
        print(name, specialization, phone)
        ins = Doctor(name=name, specialization=specialization, contact_number=phone)
        ins.save()
    return render(request, "contact.html")


class Myview(View):
    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        name = request.POST["name"]
        specialization = request.POST["specialization"]
        phone = request.POST["phone"]
        print(name, specialization, phone)
        ins = Doctor(name=name, specialization=specialization, contact_number=phone)
        ins.save()
        return render(request, "contact.html")


class Greeting(View):
    greeting = "Good Morning"

    def get(self, request):
        return HttpResponse(self.greeting)


class AnotherGreeting(Greeting):
    greeting = "hey, whats up"


# Test for Django class Based on Models


class PublisherListView(ListView):
    model = Publisher
    context_object_name = "my_publishers"


class PublisherDetailView(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["book_list"] = Book.objects.all()
        return context


class BookListView(ListView):
    context_object_name = "books"
    queryset = Book.objects.filter(publisher__name="")
    template_name = "project/book_list.html"


class AuthorListView(ListView):
    context_object_name = "authors"
    model = Author
    template_name = "project/author_list.html"


class AuthorDetailView(DetailView):
    content_type = "authors"
    model = Author
    template_name = "project/author_list.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Author, id=id_)


class PublisherBookListView(ListView):
    context_object_name = "books"
    template_name = "project/book_list"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Author, pk=id_)


class AuthorCreateView(CreateView):
    form_class = AuthorModelForm
    template_name = "project/author_create.html"
    queryset = Author.objects.all()

    def get_success_url(self):
        return reverse("author-detail")


class MultiCreateView(CreateView):
    template_name = "project/author_create.html"

    def get(self, request: HttpRequest, *args, **kwargs):
        self.author_form= AuthorModelForm()
        self.publisher_form= PublisherModelForm()
        self.book_form= BookModelForm()
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.author_form = AuthorModelForm(request.POST)
        if self.author_form.is_valid():
            author = self.author_form.save(commit=False)
        else:
            return self.form_invalid()
    
    def get_success_url(self):
        return reverse("author-detail")
    
    def get_queryset(self):
        return Author.objects.none()


        
        
class AuthorUpdateView(UpdateView):
    form_class = AuthorModelForm
    template_name = "project/author_create.html"
    queryset = Author.objects.all()
    success_url = "author"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Author, pk=id_)

    def get_success_url(self):
        return reverse("Author-List")


class AuthorDeleteView(DeleteView):
    template_name = "project/author_delete.html"
    context_object_name = "author"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Author, pk=id_)

    def get_success_url(self):
        return reverse("Author-List")


#Django Rest Framework

@api_view(['GET'])
def index(request):
    courses={
        'course_name' : 'Python',
        'learn' :  ['Flask', 'django', 'FastApi'],
        'course_provider' : 'scaler',
    }
    return Response(courses)

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def Doctors(request):
    if request.method=='GET':
        name= request.GET.get('name')
        if name is not None:
            docs= Doctor.objects.filter(Q(name__icontains=name)).all()
        else:
            docs = Doctor.objects.all()
        serializer = DoctorSerializer(docs, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = request.data
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    elif request.method=='PUT':
        data = request.data
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method=='PATCH': #
        data = request.data
        docs = Doctor.objects.get(id = data['id'])
        serializer = DoctorSerializer(docs,data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        doctor = Doctor.objects.get(id= data['id'])
        doctor.delete()
        return Response ({'message': 'Doctor Deleted'})

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def Nurses(request):
    if request.method=='GET':
        name= request.GET.get('name')
        if name is not None:
            Nur= Nurse.objects.filter(Q(name__icontains=name)).all()
        else:
            Nur = Nurse.objects.all()
        serializer = NurseSerializer(Nur, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = request.data
        serializer = NurseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    elif request.method=='PUT':
        data = request.data
        serializer =NurseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method=='PATCH': #
        data = request.data
        Nur = Nurse.objects.get(id = data['id'])
        serializer = NurseSerializer(Nur,data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        Nur = Nurse.objects.get(id= data['id'])
        Nur.delete()
        return Response ({'message': 'Nurse Deleted'})


@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
def Patients(request):
    if request.method=='GET':
        name= request.GET.get('name')
        if name is not None:
            Pat= Patient.objects.filter(Q(name__icontains=name)).all()
        else:
            Pat=Patient.objects.all()
        serializer = PatientSerializer(Pat, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = request.data
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    elif request.method=='PUT':
        data = request.data
        serializer =PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method=='PATCH': #
        data = request.data
        Pat = Patient.objects.get(id = data['id'])
        serializer = PatientSerializer(Pat,data=data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    else:
        data = request.data
        Pat = Patient.objects.get(id= data['id'])
        Pat.delete()
        return Response ({'message': 'Patient Deleted'})

    
