from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Contact, Customer, Product, Order, Tags, Animal
from home.admin_filter import Name_Filter
from django_object_actions import DjangoObjectActions
from django.urls import path
from subprocess import call
from django.core import management


# Register your models here.
@admin.register(Customer)
class Customer_List_Display(DjangoObjectActions, admin.ModelAdmin):
    list_display = ("name", "phone", "email", "date_created")
    search_fields = ("name",)
    list_filter = (Name_Filter,)
    change_list_template = "admin/customer/customer_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "Add_ten_Customers/",
                self.add_ten_Customers,
                name="Add_ten_Customers",
            ),
        ]
        return custom_urls + urls

    def add_ten_Customers(self, request):
        success = management.call_command("num_user", "10")
        if success:
            print("yay")
        else:
            print("error")
        return HttpResponseRedirect("../")


@admin.register(Contact)
class Contact_List_Display(admin.ModelAdmin):
    list_display = ("name", "email", "phone")


@admin.register(Product)
class ProductListDisplay(admin.ModelAdmin):
    list_display = ("name", "price", "category")


@admin.register(Order)
class OrderListDisplay(admin.ModelAdmin):
    list_display = ("customer", "product", "date_created", "status")
    fieldsets = [
        (
            None,
            {
                "fields": ["status", "customer", "product"],
            },
        ),
    ]
    list_filter = (
        "customer",
        "status",
    )
    actions = ["Pending", "Out_For_Delivery", "Delivered"]

    def pending(self, request, queryset):
        queryset.update(status="Pending")

    def out_for_delivery(self, request, queryset):
        queryset.update(status="Out for Delivery")

    def delivered(self, request, queryset):
        queryset.update(status="Delivered")


admin.site.register(Tags)
admin.site.register(Animal)
