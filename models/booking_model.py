from typing import Optional
from pydantic import BaseModel,ConfigDict

#BookingDate: Encapsulates the check-in/check-out dates so it can be re-used inside booking
class BookingDates(BaseModel):
    checkin: str
    checkout: str

class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str]=None
#extra = "forbid", gurantees that if the backend API randomly starts returning undocumented extra keys, our automated contract test will fail immediately 
    model_config = ConfigDict(extra="forbid")

class BookingResponse(BaseModel):
    bookingid: int
    booking: Booking
