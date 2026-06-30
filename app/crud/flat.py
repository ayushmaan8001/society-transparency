from sqlalchemy.orm import Session

from app.models.flat import Flat
from app.schemas.flat import FlatCreate, FlatUpdate


def create_flat(db: Session, data: FlatCreate, society_id: int) -> Flat:
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
    return db.query(Flat).filter(Flat.society_id == society_id).all()


def get_flat_by_id(db: Session, flat_id: int):
    return db.query(Flat).filter(Flat.id == flat_id).first()


def update_flat(db: Session, flat: Flat, data: FlatUpdate):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(flat, field, value)
    db.commit()
    db.refresh(flat)
    return flat


def delete_flat(db: Session, flat: Flat):
    db.delete(flat)
    db.commit()