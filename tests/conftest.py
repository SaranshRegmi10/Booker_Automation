import pytest
from models.booking_model import Booking,BookingDates
from services.booking_service import BookingService

@pytest.fixture(scope="session")
def booking_service():
    return BookingService()

@pytest.fixture(scope="session")
def auth_token(booking_service):
    return booking_service.auth_client.get_token()

@pytest.fixture
def sample_booking_payload():
    return Booking(
        firstname="Saransh",
        lastname="Tester",
        totalprice= 250,
        depositpaid = True,
        bookingdates= BookingDates(
            checkin="2026-08-01",
            checkout = "2026-08-10"
        ),
        additionalneeds="Late Checkout"
    )
