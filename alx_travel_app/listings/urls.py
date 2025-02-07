from django.urls import path
from .views import InitiatePaymentView, VerifyPaymentView, ListingViewSet, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'listings', ListingViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('initiate-payment/', InitiatePaymentView.as_view(),
         name='initiate-payment'),
    path('verify-payment/', VerifyPaymentView.as_view(), name='verify-payment'),
]

urlpatterns += router.urls
