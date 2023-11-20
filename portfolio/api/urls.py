from project.views import index, Doctors,Nurses, Patients
from django.urls import path


urlpatterns = [
    path('index/', index),
    path('doctor/',Doctors ),
    path('nurse/',Nurses ),
    path('patient/',Patients ),
]