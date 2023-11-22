from django.contrib import admin
from project.models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter


class NameContainsLopez(SimpleListFilter):
    title = _("Names")
    parameter_name = "contains_names"

    def lookups(self, request, model_admin):
        return (("lopez", "Lopez"), ("john", "John"))

    def queryset(self, request, queryset):
        if self.value() == "lopez":
            queryset = queryset.filter(name__icontains="Lopez")
        if self.value() == "john":
            queryset = queryset.filter(name__icontains="John")
        return queryset


class DoctorsList(SimpleListFilter):
    title = _("Doctors")
    parameter_name = "doctor_patients"

    def lookups(self, request, model_admin):
        return (("gerald barnett", "Gerald Barnett"),)

    def queryset(self, request, queryset):
        if self.value() == "gerald barnett":
            try:
                doctor = Doctor.objects.get(name="Gerald Barnett")
                queryset = queryset.filter(doctor=doctor)
            except Doctor.DoesNotExist:
                queryset = queryset.none()
        return queryset


class AgeRangeList(SimpleListFilter):
    title = _("Age Range")
    parameter_name = "Age Ranges"

    def lookups(self, request, model_admin):
        return (
            ("18-34", "18-34"),
            ("35-49", "35-49"),
            ("50+", "50+"),
        )

    def queryset(self, request, queryset):
        if self.value() == "18-35":
            queryset = queryset.filter(age__gte=20, age__lte=34)

        if self.value() == "35-49":
            queryset = queryset.filter(age__gte=35, age__lte=49)

        if self.value() == "50+":
            queryset = queryset.filter(age__gte=50)

        return queryset


class SpecificDate(SimpleListFilter):
    title = _("Specific Date")
    parameter_name = "Dates"

    def lookups(self, request, model_admin):
        return (("2015-07-07", "2015-07-07"),)

    def queryset(self, request, queryset):
        if self.value() == "2015-07-07":
            queryset = queryset.filter(date_admitted=self.value())

        return queryset


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_filter = (DoctorsList, AgeRangeList, SpecificDate)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_filter = (NameContainsLopez,)


admin.site.register(Nurse)
admin.site.register(MedicalRecord)
admin.site.register(Hospital)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)
