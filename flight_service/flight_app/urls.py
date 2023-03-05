from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from . import views


router = DefaultRouter()

router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('find-flight/', views.find_flight),
    path('save-reservation/', views.save_reservation),
    # * get token
    path('api_token_auth/', obtain_auth_token, name='api_token_auth'),
    path('quero_token/', views.get_user_from_token, name='quero_token')
]
