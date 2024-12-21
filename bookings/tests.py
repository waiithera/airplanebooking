from django.test import TestCase
from .models import Flight, Passenger

class FlightModelTest(TestCase):
    def setUp(self):
        Flight.objects.create(
            flight_number="AB123",
            departure="2024-01-01T10:00:00Z",
            arrival="2024-01-01T14:00:00Z",
            origin="London",
            destination="New York",
            capacity=100,
        )

    def test_flight_creation(self):
        flight = Flight.objects.get(flight_number="AB123")
        self.assertEqual(flight.origin, "London")
        self.assertEqual(flight.destination, "New York")
