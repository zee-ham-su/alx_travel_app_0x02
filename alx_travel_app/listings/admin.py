from django.contrib import admin
from .models import Listing, Booking, Payment

admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(Payment)
