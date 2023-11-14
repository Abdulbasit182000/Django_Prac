from django.core.management.base import BaseCommand, CommandParser
from project.models import *
from faker import Faker
import random


class Command(BaseCommand):
    help = "Fills Whole Database"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="count of user")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        faker = Faker()
        for _ in range(count):  # Fake Doctor Data
            Doctor.objects.create(
                name=faker.name(),
                specialization=faker.job(),
                contact_number=faker.phone_number,
            )
        for _ in range(count):  # Fake Nurse Data
            Nurse.objects.create(
                name=faker.name(),
                contact_number=faker.phone_number,
            )
        doctors = list(Doctor.objects.all())
        nurses = list(Nurse.objects.all())
        for _ in range(count):  # Fake Patient data
            patient = Patient.objects.create(
                name=faker.name(),
                age=faker.random_int(min=18, max=90),
                nurse=random.choice(nurses),
                date_admitted=faker.date(),
            )
            patient.doctor.set(random.sample(doctors, k=faker.random_int(1, 10)))
        patients = list(Patient.objects.all())
        for _ in range(count):
            MedicalRecord.objects.create( #Fake Record
                patient=random.choice(patients),
                diagnoses=faker.sentence(),
                perscription=faker.paragraph(),
            )
        for i in range(len(patients)):
            hospital= Hospital.objects.create( #Fake Hospital Record
                patient=patients[i],
                nurse= patients[i].nurse,
            )
            hospital.doctor.set(patients[i].doctor.all())

