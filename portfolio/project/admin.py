from django.contrib import admin
from project.models import Patient, Doctor, Nurse, MedicalRecord, Hospital
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
                # Use get instead of filter to retrieve a single Doctor object
                doctor = Doctor.objects.get(name="Gerald Barnett")
                queryset = queryset.filter(doctor=doctor)
            except Doctor.DoesNotExist:
                # Handle the case where the doctor does not exist
                queryset = queryset.none()
        return queryset


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_filter = (DoctorsList,)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_filter = (NameContainsLopez,)


admin.site.register(Nurse)
admin.site.register(MedicalRecord)
admin.site.register(Hospital)
