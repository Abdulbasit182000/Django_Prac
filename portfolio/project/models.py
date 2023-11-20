from django.db import models
from django.urls import reverse


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
    doctor = models.ManyToManyField(Doctor, related_name="patients")
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name="patients")
    date_admitted = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="hospitals"
    )
    doctor = models.ManyToManyField(Doctor, related_name='hospitals')
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, default=1)


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="records"
    )
    diagnoses = models.TextField()
    perscription = models.TextField()

#Test for Class Based Views


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return self.name
        return reverse("author-detail",kwargs={'pk':self.pk})


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()