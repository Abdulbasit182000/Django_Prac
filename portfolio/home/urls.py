from django.contrib import admin
from django.urls import path
from django.urls import include
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('projects', views.projects,name='projects'),
    path('contact', views.contact,name='contact'),
]
