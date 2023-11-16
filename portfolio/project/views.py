from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from project.models import Doctor
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Publisher, Book, Author
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AuthorModelForm


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


class AuthorListView(DetailView):
    content_type = "authors"
    models = Author
    template_name = "project/author_list.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Author, id=id_)


class PublisherBookListView(ListView):
    context_object_name = "books"
    template_name = "project/book_list"

    def get_object(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs["publisher"])
        return Book.objects.filter(publisher=self.publisher)


class AuthorCreateView(CreateView):
    form_class = AuthorModelForm
    template_name = "project/author_create.html"
    queryset = Author.objects.all()
    success_url = "/"


class AuthorUpdateView(UpdateView):
    form_class = AuthorModelForm
    template_name = "project/author_create.html"
    queryset = Author.objects.all()
    success_url = "/"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Author, id=id_)


class AuthorDeleteView(DeleteView):
    template_name = "project/author_delete.html"
    success_url = "/"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Author, id=id_)

