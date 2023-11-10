from django.contrib import admin
from .models import Customer

class NameFilter(admin.SimpleListFilter):
    title='Name Filter'
    parameter_name='name'

    def lookups(self, request, model_admin):
        return (
            ('name_contains b', 'name_contains b'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'contains_b':
            return queryset.filter(name__icontains='b')