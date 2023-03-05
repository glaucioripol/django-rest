from django.http import HttpRequest

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Flight, Passenger, Reservation
from .serializer import (
    FlightSerializer,
    PassengerSerializer,
    ReservationSerializer
)


# ! TODO: refactor this function to use query string parameters and using get
@api_view(['POST'])
def find_flight(request: HttpRequest):
    try:
        query_filters = {
            'departure_city': request.data['departure_city'],
            'arrival_city': request.data['arrival_city'],
            'date_of_departure': request.data['date_of_departure']
        }

        flight = Flight.objects.filter(**query_filters)

        flight_serializer = FlightSerializer(flight, many=True)

        return Response(flight_serializer.data)

    except Flight.DoesNotExist:
        return Response(
            data={'error': 'Flight not found'},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
def save_reservation(request: HttpRequest):
    request_data = request.data

    try:
        flight_id = request_data['flight_id']
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return Response(
            data={'error': 'Flight not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        passenger_id = request_data['passenger_id']
        passenger = Passenger.objects.get(pk=passenger_id)
    except Passenger.DoesNotExist:
        return Response(
            data={'error': 'Passenger not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        reservation = Reservation(flight=flight, passenger=passenger)
        reservation.save()

        reservation_serializer = ReservationSerializer(instance=reservation)

        response_data = {
            'message': 'Reservation saved',
            'reservation': reservation_serializer.data
        }

        return Response(data=response_data, status=status.HTTP_201_CREATED)

    except Exception:
        print('Error saving reservation')
        return Response(
            data={'error': 'Reservation not saved'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]


class PassengerViewSet(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
