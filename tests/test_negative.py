import pytest
import requests
import allure

@allure.epic("Booking Management")
@allure.feature("Negative & Edge Cases")
class TestNegativeBooking:

    @allure.story("Get Non-Existent Booking")
    @allure.severity(allure.severity_level.NORMAL)
    def test_fet_invalid_booking_id(self,booking_service):
        invalid_id = 90000
        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            booking_service.get_booking(invalid_id)
            assert exc_info.value.response.status_code == 404

    @allure.story("Update Booking with Invalid Token")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_booking_invalid_auth(self,booking_service,sample_booking_payload):
        create = booking_service.create_booking(sample_booking_payload)
        booking_id = create.bookingid

        invalid_token = "invalid_token_12345"

        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            booking_service.update_booking(booking_id,sample_booking_payload,token = invalid_token)

            assert exc_info.value.response.status_code == 403
        