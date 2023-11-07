from django.contrib import admin
from .models import Contact,Customer,Product,Order,tags,Animal

# Register your models here.

admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(tags)
admin.site.register(Order)
admin.site.register(Animal)