from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Nurse(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor, related_name="doctor_of")
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name="Patients")
    date_admitted = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="Hospitals"
    )
    doctor = models.ManyToManyField(Doctor)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="Medical_Records"
    )
    diagnoses = models.TextField()
    perscription = models.TextField()
