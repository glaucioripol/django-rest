from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('find-flight/', views.find_flight),
    path('save-reservation/', views.save_reservation)
]
