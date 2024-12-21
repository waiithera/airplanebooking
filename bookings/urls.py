from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from .views import FlightViewSet, PassengerViewSet

router = DefaultRouter()
router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'passengers', PassengerViewSet, basename='passenger')

urlpatterns = [
    path('', include(router.urls)),
     path('admin/', admin.site.urls),
    path('api/', include('bookings.urls'))
]
