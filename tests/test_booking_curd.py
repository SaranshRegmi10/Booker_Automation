import allure
import pytest
from models.booking_model import Booking, BookingResponse


@allure.epic("Booking Management")
@allure.feature("CRUD Operations")
class TestBookingCRUD:

    @allure.story("Create Booking")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_booking(self, booking_service, sample_booking_payload):
        # Act
        created_booking: BookingResponse = booking_service.create_booking(
            sample_booking_payload
        )

        # Assert
        assert created_booking.bookingid is not None
        assert (
            created_booking.booking.firstname
            == sample_booking_payload.firstname
        )
        assert (
            created_booking.booking.totalprice
            == sample_booking_payload.totalprice
        )

    @allure.story("Full Lifecycle (Create -> Read -> Update -> Delete)")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_booking_lifecycle(
        self, booking_service, sample_booking_payload, auth_token
    ):
        # 1. CREATE
        created = booking_service.create_booking(sample_booking_payload)
        booking_id = created.bookingid

        # 2. READ
        fetched_booking = booking_service.get_booking(booking_id)
        assert fetched_booking.lastname == sample_booking_payload.lastname

        # 3. UPDATE
        sample_booking_payload.totalprice = 500
        updated_booking = booking_service.update_booking(
            booking_id, sample_booking_payload, auth_token
        )
        assert updated_booking.totalprice == 500

        # 4. DELETE
        delete_response = booking_service.delete_booking(booking_id, auth_token)
        assert delete_response.status_code == 201