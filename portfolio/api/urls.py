from project.views import (
    index,
    Doctors,
    Nurses,
    Patients,
    DoctorAPI,
    DoctorViewSet,
    NurseAPI,
    PatientAPI,
    NurseViewSet,
    PatientViewSet,
    RegisterAPI,
    LoginApi
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"doc", DoctorViewSet, basename="doctor")
router.register(r"nur", NurseViewSet, basename="nurse")
router.register(r"pat", PatientViewSet, basename="patient")
urlpatterns = router.urls


urlpatterns = [
    # Model Viewsets
    path("", include(router.urls)),
    # Simple Function Model Serializer
    path("index/", index),
    path("doctor/", Doctors),
    path("nurse/", Nurses),
    path("patient/", Patients),
    # API Views
    path("doctors/", DoctorAPI.as_view()),
    path("nurses/", NurseAPI.as_view()),
    path("patients/", PatientAPI.as_view()),
    path('register/',RegisterAPI.as_view()),
    path('login/',LoginApi.as_view()),
]
