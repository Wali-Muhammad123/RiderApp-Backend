from allauth.account.models import EmailAddress
from django.contrib.gis.geos import Point
from django.core.management import BaseCommand
from tqdm import tqdm
import random

from rides_mgmt.models import RideObject
from users.models import RiderUser, Customer, Rider
from faker import Faker


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        faker = Faker()
        customer_users = []
        rider_users = []
        for i in tqdm(range(30)):
            customers = RiderUser.objects.create_user(
                email=f"test{i}@gmail.com",
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                password="wali12345",
                role="customer",
                is_active=True
            )
            customer_users.append(customers)
        for i in tqdm(range(31, 41)):
            riders = RiderUser.objects.create_user(
                email=f"test{i}@gmail.com",
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                password="wali12345",
                role="rider",
                is_active=True
            )
            rider_users.append(riders)
        self.stdout.write("Successfully created Users")
        customers = Customer.objects.all()
        riders = Rider.objects.all()
        for i in tqdm(customers):
            i.phone_number = faker.phone_number()
            i.address = faker.address()
            i.city = faker.city()
            i.state = faker.state()
            i.bank_details = faker.iban()
            i.status = 'available'
            i.current_location = Point(-122.084, 37.4219983)
            i.save()
        self.stdout.write("Successfully populated Customers")
        for i in tqdm(riders):
            i.phone_number = faker.phone_number()
            i.address = faker.address()
            i.city = faker.city()
            i.state = faker.state()
            i.bank_details = faker.iban()
            i.status = 'available'
            i.current_location = Point(-122.084, 37.4219983)
            i.vehicle = faker.bothify(text='???-####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            i.license = faker.numerify(text='########')
            i.save()
        self.stdout.write("Successfully populated rider users")
        for i in tqdm(rider_users + customer_users):
            EmailAddress.objects.create(
                user=i,
                email=i.email,
                verified=True,
                primary=True
            )
        self.stdout.write("Successfully added email address")
        # Creating ride objects for customers to choose from
        for i in range(1,11):
            RideObject.objects.create(
                rider=(random.choice(rider_users)).rider,
                customer=customer_users[0].customer,
                pickup_location=Point(-122.084, 37.4219983),
                drop_off_location=Point(-122.084, 37.4419983),
                deal_price=100,
            )
        self.stdout.write("Successfully Populated the Ride Objects")
