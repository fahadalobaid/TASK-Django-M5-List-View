
from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import ListSerializer , ListSerializerBooking


class flightsListApiView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ListSerializer

class BookingListApiView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = ListSerializerBooking
