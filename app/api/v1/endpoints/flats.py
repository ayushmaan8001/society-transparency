from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User, UserRole
from app.schemas.flat import FlatCreate, FlatUpdate, FlatResponse
from app.crud.flat import create_flat, get_all_flats, get_flat_by_id, update_flat, delete_flat
from app.crud.society import get_society_by_id

router = APIRouter()


@router.post("/", response_model=FlatResponse, status_code=status.HTTP_201_CREATED)
def create(society_id: int, data: FlatCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.super_admin, UserRole.society_admin]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    society = get_society_by_id(db, society_id)
    if not society:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Society not found")
    return create_flat(db, data, society_id)


@router.get("/", response_model=List[FlatResponse])
def get_all(society_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_flats(db, society_id)


@router.get("/{flat_id}", response_model=FlatResponse)
def get_one(society_id: int, flat_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    flat = get_flat_by_id(db, flat_id)
    if not flat or flat.society_id != society_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Flat not found")
    return flat


@router.put("/{flat_id}", response_model=FlatResponse)
def update(society_id: int, flat_id: int, data: FlatUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.super_admin, UserRole.society_admin]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    flat = get_flat_by_id(db, flat_id)
    if not flat or flat.society_id != society_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Flat not found")
    return update_flat(db, flat, data)


@router.delete("/{flat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(society_id: int, flat_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.super_admin, UserRole.society_admin]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    flat = get_flat_by_id(db, flat_id)
    if not flat or flat.society_id != society_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Flat not found")
    delete_flat(db, flat)