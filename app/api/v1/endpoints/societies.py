from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.core.dependencies import get_current_user
from app.models.user import User, UserRole
from app.schemas.society import SocietyCreate, SocietyUpdate, SocietyResponse
from app.crud.society import (
    create_society, get_all_societies,
    get_society_by_id, update_society, deactivate_society
)

router = APIRouter()


@router.post("/", response_model=SocietyResponse, status_code=status.HTTP_201_CREATED)
def create(data: SocietyCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.super_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    return create_society(db, data, current_user.id)


@router.get("/", response_model=List[SocietyResponse])
def get_all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_all_societies(db)


@router.get("/{society_id}", response_model=SocietyResponse)
def get_one(society_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    society = get_society_by_id(db, society_id)
    if not society:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Society not found")
    return society


@router.put("/{society_id}", response_model=SocietyResponse)
def update(society_id: int, data: SocietyUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.super_admin, UserRole.society_admin]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    society = get_society_by_id(db, society_id)
    if not society:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Society not found")
    return update_society(db, society, data)


@router.delete("/{society_id}", status_code=status.HTTP_204_NO_CONTENT)
def deactivate(society_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.super_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    society = get_society_by_id(db, society_id)
    if not society:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Society not found")
    deactivate_society(db, society)