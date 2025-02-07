from django.db import models
import uuid


class Listing(models.Model):
    property_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=255, null=False)
    price_per_night = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)
    status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pending'), ('confirmed',
                                          'Confirmed'), ('canceled', 'Canceled')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.property.name} ({self.start_date} to {self.end_date})"


class Review(models.Model):
    review_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(null=False)
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.property.name}: {self.rating}/5"
