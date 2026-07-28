from client.base_client import BaseClient
from config.settings import settings
from models.auth_model import AuthRequest,AuthResponse

#AuthClient inherits all core requests features directly from BaseClient 
class AuthClient(BaseClient):
    def get_token(
            self,
            username:str = settings.USERNAME,
            password:str = settings.PASSWORD
            ) ->str:
    #model_dump(), converts the pydantic AuthRequest object clearly into Python dictionary to send as JSON
        payload = AuthRequest(username=username,password=password).model_dump()
        response = self.post("/auth",data=payload)

        #validates status code and parse response through Pydantic
        response.raise_for_status()
    #AuthResponse(**response.json()), instantly validates that the server returend a valid dictionary containing tokens
        auth_response = AuthResponse(**response.json())
        return auth_response.token  

