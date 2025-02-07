import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Seed the database with sample Listings and Bookings for Ghana settings'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data for Ghana settings...')

        # Create sample users (hosts and guests)
        users = []
        for i in range(5):
            username = f'user_ghana{i}'
            email = f'user{i}@ghanaexample.com'
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username, email, 'password')
                users.append(user)
                self.stdout.write(f'Created user: {username}')
            else:
                user = User.objects.get(username=username)
                users.append(user)
                self.stdout.write(f'User {username} already exists')

        # Create sample listings
        locations = ['Accra', 'Kumasi', 'Tamale', 'Takoradi', 'Cape Coast']
        listings = []
        for i in range(20):
            listing = Listing.objects.create(
                host=random.choice(users),
                name=f'Comfortable Home {i+1}',
                description=f'A cozy and affordable home in the heart of {random.choice(locations)}. Perfect for travelers!',
                location=random.choice(locations),
                price_per_night=random.randint(100, 1000)  # Price in GHS
            )
            listings.append(listing)
            self.stdout.write(f'Created listing: {listing.name}')

        # Create sample bookings
        for _ in range(50):
            start_date = timezone.now().date() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(1, 7))
            nights = (end_date - start_date).days
            listing = random.choice(listings)
            Booking.objects.create(
                property=listing,
                user=random.choice(users),
                start_date=start_date,
                end_date=end_date,
                total_price=listing.price_per_night * nights,
                status=random.choice(['pending', 'confirmed', 'canceled'])
            )
            self.stdout.write(f'Created booking for {listing.name}')

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded Listings and Bookings for Ghana settings!'
        ))
