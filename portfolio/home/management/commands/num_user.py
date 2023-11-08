from django.core.management.base import BaseCommand, CommandParser
from home.models import Customer
from django.utils.crypto import get_random_string
from faker import Faker


class Command(BaseCommand):
    help = "Generate random users"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="count of user")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        faker = Faker()
        for i in range(count):
            Customer.objects.create(name=faker.name(), phone="12345678910")
