from pydantic import BaseModel, Field

class AddressCreate(BaseModel):
    street: str = Field(..., max_length=255)
    city: str = Field(..., max_length=100)
    state: str = Field(..., max_length=100)
    zip_code: str = Field(..., max_length=20)
    latitude: float | None = None
    longitude: float | None = None

class AddressRead(AddressCreate):
    id: int

    class Config:
        orm_mode = True
    
    