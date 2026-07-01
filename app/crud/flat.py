from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.flat import Flat
from app.schemas.flat import FlatCreate, FlatUpdate


def create_flat(db: Session, data: FlatCreate, society_id: int) -> Flat:
    existing_flat = (
        db.query(Flat)
        .filter(
            Flat.society_id == society_id,
            Flat.flat_number == data.flat_number,
            Flat.is_active == True,
        )
        .first()
    )

    if existing_flat:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Flat number already exists in this society",
        )

    flat = Flat(
        society_id=society_id,
        flat_number=data.flat_number,
        floor=data.floor,
        type=data.type,
    )

    db.add(flat)
    db.commit()
    db.refresh(flat)
    return flat


def get_all_flats(db: Session, society_id: int):
    return (
        db.query(Flat)
        .filter(
            Flat.society_id == society_id,
            Flat.is_active == True,
        )
        .all()
    )


def get_flat_by_id(db: Session, flat_id: int):
    return (
        db.query(Flat)
        .filter(
            Flat.id == flat_id,
            Flat.is_active == True,
        )
        .first()
    )


def update_flat(db: Session, flat: Flat, data: FlatUpdate):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(flat, field, value)

    db.commit()
    db.refresh(flat)
    return flat


def delete_flat(db: Session, flat: Flat):
    flat.is_active = False
    db.commit()
    db.refresh(flat)
    return flat