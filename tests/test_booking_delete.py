import allure
import pytest
import requests

@allure.epic("Booking Management")
@allure.feature("Resource Lifecycle")
class TestBookingDelete:

    @allure.story("Delete Booking and Verfiy 404 on Subsequent get")
    def test_delete_booking_sucess(
        self,booking_service,sample_booking_payload,auth_token
    ):
        created = booking_service.create_booking(sample_booking_payload)
        booking_id = created.bookingid

        delete_response = booking_service.delete_booking(booking_id,auth_token)
        assert delete_response.status_code == 201

        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            booking_service.get_booking(booking_id)

        assert (
            exc_info.value.response.status_code == 404
        ),f"Booking {booking_id} should no longer exist "