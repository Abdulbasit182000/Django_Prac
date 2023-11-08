from django.contrib import admin
from .models import Contact,Customer,Product,Order,Tags,Animal

# Register your models here.

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Tags)
admin.site.register(Order)
admin.site.register(Animal)