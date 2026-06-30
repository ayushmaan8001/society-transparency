from pydantic import BaseModel
from typing import Optional
from app.models.flat import FlatType


class FlatCreate(BaseModel):
    flat_number: str
    floor: Optional[int] = None
    type: Optional[FlatType] = FlatType.vacant


class FlatUpdate(BaseModel):
    flat_number: Optional[str] = None
    floor: Optional[int] = None
    type: Optional[FlatType] = None
    owner_id: Optional[int] = None
    tenant_id: Optional[int] = None


class FlatResponse(BaseModel):
    id: int
    society_id: int
    flat_number: str
    floor: Optional[int]
    type: FlatType
    owner_id: Optional[int]
    tenant_id: Optional[int]

    class Config:
        from_attributes = True