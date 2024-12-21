Airline Booking System

A simple Airline Booking System built using Django and Django Rest Framework. The application includes API endpoints for managing flights and passengers
Project Description

The Airline Booking System simulates basic operations in an airline booking environment:

Manage flights (add, view, update, delete).
Manage passengers (add, view, update, delete).
Associate passengers with specific flights.
The system supports both API-based interactions


Features
Flight Management
-Add new flights.
-View all flights and their details.
-Delete flights.

Passenger Management
-Add new passengers.
-View all passengers and their assigned flights.
-Delete passengers.


User-friendly UI for managing flights and passengers.
Dynamic content fetching using JavaScript.
REST API
-CRUD endpoints for both flights and passengers.
-Pagination and filtering options for large datasets.



Installation Instructions
Prerequisites
-Python 3.x
-Django 4.x
-A web browser (for UI testing)



Step 1: Clone the Repository
bash
Copy code
git clone <repository-url>
cd airline-booking-system


Step 2: Create a Virtual Environment
bash
Copy code
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows


Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt


Step 4: Apply Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate


Step 5: Create a Superuser (Optional for Admin Access)
bash
Copy code
python manage.py createsuperuser


Step 6: Run the Development Server
bash
Copy code
python manage.py runserver
Usage Instructions
Access the API
Once the server is running, you can access the API at:

Flights API: http://127.0.0.1:8000/api/flights/
Passengers API: http://127.0.0.1:8000/api/passengers/
Access the UI


Navigate to:

arduino
Copy code
http://127.0.0.1:8000/


Use the web interface to:

View flights and passengers.
Add new passengers to flights.



API Documentation
Endpoints
Flights
GET /api/flights/: Retrieve all flights.
POST /api/flights/: Add a new flight.
GET /api/flights/<id>/: Retrieve details of a specific flight.
DELETE /api/flights/<id>/: Delete a flight.


Passengers
GET /api/passengers/: Retrieve all passengers.
POST /api/passengers/: Add a new passenger.
GET /api/passengers/<id>/: Retrieve details of a specific passenger.
DELETE /api/passengers/<id>/: Delete a passenger.
Example Payloads
Create a Flight

json
Copy code
{
    "flight_number": "D123",
    "departure": "2024-12-20T10:00:00Z",
    "arrival": "2024-12-20T14:00:00Z",
    "origin": "London",
    "destination": "New York",
    "capacity": 200
}


Create a Passenger

json
Copy code
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone_number": "+1234567890",
    "flight": 1
}


Technologies Used
Back-End: Django, Django Rest Framework
Database: SQLite (default)
API Testing Tools: Postman

Folder Structure
csharp
Copy code
airline-booking-system/
├── airline_booking/       # Main project folder
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL configurations
│   └── ...
├── bookings/              # Application folder
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # ViewSets for API
│   
├── db.sqlite3             # SQLite database
├── requirements.txt       # Python dependencies
└── README.md              # Project README file


Contributors
Natasha Muiyuro
License
This project is licensed under the MIT License - see the LICENSE file for details.
