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
    # changelist_actions = ('imports', )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "your-model-changelist/",
                self.your_model_changelist,
                name="your_model_changelist",
            ),
        ]
        return custom_urls + urls

    def your_model_changelist(self, request):
        success = management.call_command("num_user", "10")
        if success:
            print("yay")
        else:
            print("error")
        return HttpResponseRedirect("../")

    # def imports(modeladmin, request, queryset):
    #     print("Imports button pushed")


@admin.register(Contact)
class Contact_List_Display(admin.ModelAdmin):
    list_display = ("name", "email", "phone")


@admin.register(Product)
class Product_List_Display(admin.ModelAdmin):
    list_display = ("name", "price", "category")


@admin.register(Order)
class Order_List_Display(admin.ModelAdmin):
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

    def Pending(self, request, queryset):
        queryset.update(status="Pending")

    def Out_For_Delivery(self, request, queryset):
        queryset.update(status="Out for Delivery")

    def Delivered(self, request, queryset):
        queryset.update(status="Delivered")


admin.site.register(Tags)
admin.site.register(Animal)
