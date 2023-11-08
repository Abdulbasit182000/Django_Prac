from typing import Any
from django.db import models
from django.core.exceptions import ValidationError


# Custom Validators
def int_even(value):
    if len(value) != 11:
        raise ValidationError(f"{value} is not correct")


def end_with(value):
    if value.endswith("er"):
        raise ValidationError("invalid string")


def number_even(value):
    if value % 2 != 0:
        raise ValidationError("number is not even")


# Model Classes
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[int_even])

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(
        auto_now_add=True, null=True, db_column="Date_Time"
    )
    tag = models.ManyToManyField(Tags)

    def __str__(self):
        return self.name

    @property
    def get_price(self):
        return self.price


class Order(models.Model):
    sTATUS = (
        ("Pending", "Pending"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(
        Product, null=True, on_delete=models.SET_NULL, db_index=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=sTATUS)


class test(models.Model):
    name = models.CharField(
        max_length=20, validators=[end_with], help_text="Test to check if this works."
    )


class Even_Integer(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators.append(number_even)


class My_model(models.Model):
    num = Even_Integer()


class Animal(models.Model):
    legs = models.IntegerField()

    class Meta:
        db_table = "Pets"
        verbose_name = "dog"


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        abstract = True


class Student(Person):
    School = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = "student"
