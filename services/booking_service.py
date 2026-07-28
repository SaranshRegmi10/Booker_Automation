from client.auth_client import AuthClient
from client.base_client import BaseClient
from models.booking_model import Booking,BookingResponse

class BookingService(BaseClient):
    def __init__(self):                                                 
        super().__init__()
        self.auth_client = AuthClient()

    def get_auth_cookie(self) -> str:
        token = self.auth_client.get_token()
        return f"token={token}"
    
    def create_booking(self,booking_data:Booking)-> BookingResponse:
        response = self.post("/booking",data=booking_data.model_dump())
        response.raise_for_status()
        return BookingResponse(**response.json())

    def get_booking(self,booking_id:int)-> Booking:
        response = self.get(f"/booking/{booking_id}")
        response.raise_for_status()
        return Booking(**response.json())

    def update_booking(self,booking_id:int,booking_date:Booking,token:str) -> Booking:
        headers = {"Cookie":f"token={token}"}
        response = self.put(
            f"/booking/{booking_id}",
            data = booking_date.model_dump(),
            headers = headers
        )
        response.raise_for_status()
        return Booking(**response.json())

    def delete_booking(self,booking_id:str,token:str):
        headers = {"Cookie":f"token={token}"}
        response = self.delete(f"/booking/{booking_id}",headers=headers)
        response.raise_for_status()
        return response

