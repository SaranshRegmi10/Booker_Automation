import allure
import pytest

@allure.epic("Booking Management")
@allure.feature("PATCH Operation")
class TestBookingPatch:

    @allure.story("Partial Update Booking FirstName and Price")
    def test_partial_update_booking(
        self,booking_service,sample_booking_payload,auth_token
    ):
        created = booking_service.create_booking(sample_booking_payload)
        booking_id = created.bookingid

        patch_payload = {
            "firstname":"UpadatedFirst",
            "totalprice": 77
        }
        updated_booking = booking_service.partial_update_booking(
            booking_id,patch_payload,auth_token
        )

        assert updated_booking.firstname == "UpadatedFirst"
        assert updated_booking.totalprice == 77
        assert updated_booking.lastname == sample_booking_payload.lastname