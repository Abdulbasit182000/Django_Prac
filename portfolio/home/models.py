from typing import Any
from django.db import models
from django.core.exceptions import ValidationError


def inteven(value):
    if len(value) != 11:
        raise ValidationError(str(value) + "is not correct")


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=13, validators=[inteven])

    def __str__(self):
        return self.name


# Tables and Relationship


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class tags(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(tags)

    def __str__(self):
        return self.name


class Order(models.Model):
    sTATUS = (
        ("Pending", "Pending"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=sTATUS)



#test class for validators

def end_with(value):
    if value.endswith('er'):
        raise ValidationError('invalid string')

class test(models.Model):
    name=models.CharField(max_length=20, validators=[end_with])

#custom field

def number_even(value):
    if(value % 2 != 0):
        raise ValidationError('number is not even')


class EvenInteger(models.IntegerField):
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.validators.append(number_even)

class My_model(models.Model):
    num=EvenInteger()

#Meta Class

class Animal(models.Model):
    legs = models.IntegerField()

    class Meta:
        db_table='Pets'
        verbose_name='dog'


class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    class Meta:
        abstract=True

class Student(Person):
    School=models.CharField(max_length=50)

    class Meta:
        db_table='student'