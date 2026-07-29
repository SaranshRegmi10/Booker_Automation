import allure
import pytest 
from models.booking_model import Booking,BookingDates

@allure.epic("Booking Management")
@allure.feature("Boundary & Data-Driven Testing")
class TestBookingBoundary:

    @allure.story("Create Booking with Edge Case Payloads")
    @pytest.mark.parametrize(
        "firstname, lastname,price,deposit,checkin,checkout,needs",
        [
            # Boundary 1: Minimum total price (0)
            ("MinPrice", "User", 0, True, "2026-10-01", "2026-10-05", "Breakfast"),
            # Boundary 2: Special characters & accents in names
            ("Jöhn-François", "O'Connor", 150, False, "2026-11-01", "2026-11-02", None),
            # Boundary 3: Long date range / far future dates
            ("FarFuture", "Traveler", 9999, True, "2030-01-01", "2030-12-31", "All Inclusive"),
        ],
    )
    def test_create_booking_boundary_case(
        self,
        booking_service,
        firstname,
        lastname,
        price,
        deposit,
        checkin,
        checkout,
        needs
    ):
        payloads =  Booking(
            firstname=firstname,
            lastname= lastname,
            totalprice= price,
            depositpaid = deposit,
            bookingdates= BookingDates(checkin=checkin,checkout=checkout),
            additionalneeds=needs,
        )
        response = booking_service.create_booking(payloads)

        assert response.bookingis is not None
        assert response.booking.firstname == firstname
        assert response.booking.totalprice == price