from pydantic import BaseModel
from typing import Optional


class SocietyCreate(BaseModel):
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    total_flats: Optional[int] = None
    registration_number: Optional[str] = None


class SocietyUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    total_flats: Optional[int] = None
    registration_number: Optional[str] = None


class SocietyResponse(BaseModel):
    id: int
    name: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    total_flats: Optional[int]
    registration_number: Optional[str]
    is_active: bool

    class Config:
        from_attributes = True