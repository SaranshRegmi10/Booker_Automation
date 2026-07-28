from pydantic import BaseModel,ConfigDict

class AuthRequest(BaseModel):
    username:str
    password:str

class AuthResponse(BaseModel):
    token: str

    model_config = ConfigDict(extra="forbid")