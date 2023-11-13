from django.contrib import admin
from project.models import *

admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Hospital)
