import allure 
import pytest 
import requests

@allure.epic("Security and Access Control")
@allure.feature("Authentication Guards")
class TestBookingSecurity:

    @allure.story("Reject PUT Request without Auth Token")
    def test_update_booking_without_token(
        self,booking_service,sample_booking_model
    ):
        create = booking_service.create_booking(sample_booking_model)

        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            booking_service.update_booking(
                booking_id = create.bookingid,
                payload = sample_booking_model,
                token = None
            )

        assert (
            exc_info.value.response.status_code == 403
        ),"Expected 403 Forbidden when token is missing"

    @allure.story("Reject DELETE Request with Invalid Auth Token")
    def test_delete_booking_invalid_token(
        self,booking_service,sample_booking_model
    ):
        create = booking_service.create_booking(sample_booking_model)

        with pytest.raises(requests.exceptions.HTTPError) as exc_info:
            booking_service.delete_booking(
                booking_id = create.bookingid,
                token = "invalid_token_12345"
            )   

        assert (
            exc_info.value.response.status_code == 403
        ), "Expected 403 Forbidden when using an invalid token "