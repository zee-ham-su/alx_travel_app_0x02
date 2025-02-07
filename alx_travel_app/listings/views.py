from rest_framework import viewsets
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer
import requests
from django.http import JsonResponse
from django.views import View
from django.conf import settings


class InitiatePaymentView(View):
    def post(self, request, *args, **kwargs):
        # Extract booking details from request
        booking_reference = request.POST.get('booking_reference')
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')

        # Prepare payload for Chapa API
        payload = {
            'amount': amount,
            'currency': 'ETB',
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'phone_number': phone_number,
            'tx_ref': booking_reference,
            'callback_url': 'https://localhost:8000/api/verify-payment/',
            'return_url': 'https://localhost:8000/payment-success/',
            'customisation': {
                'title': 'Payment for booking',
                'description': 'Please complete the payment process'
            }
        }

        headers = {
            'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}',
            'Content-Type': 'application/json'
        }

        # Make a request to Chapa API
        response = requests.post(
            'https://api.chapa.co/v1/transaction/initialize', json=payload, headers=headers)
        data = response.json()

        if response.status_code == 200:
            # Save the payment details in the database
            payment = Payment.objects.create(
                booking_reference=booking_reference,
                payment_status='Pending',
                amount=amount,
                transaction_id=data['data']['tx_ref']
            )
            return JsonResponse({'payment_url': data['data']['checkout_url']})
        else:
            return JsonResponse({'error': 'Payment initiation failed'}, status=400)


class VerifyPaymentView(View):
    def get(self, request, *args, **kwargs):
        transaction_id = request.GET.get('transaction_id')

        # Verify payment status with Chapa
        headers = {
            'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}'
        }
        response = requests.get(
            f'https://api.chapa.co/v1/transaction/verify/{transaction_id}', headers=headers)
        data = response.json()

        if response.status_code == 200 and data['status'] == 'success':
            # Update the payment status in the database
            payment = Payment.objects.get(transaction_id=transaction_id)
            payment.payment_status = 'Completed'
            payment.save()
            return JsonResponse({'status': 'Payment completed successfully'})
        else:
            return JsonResponse({'status': 'Payment verification failed'}, status=400)


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
