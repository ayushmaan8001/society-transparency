from sqlalchemy.orm import Session

from app.models.society import Society
from app.schemas.society import SocietyCreate, SocietyUpdate


def create_society(db: Session, data: SocietyCreate, admin_id: int) -> Society:
    society = Society(
        name=data.name,
        address=data.address,
        city=data.city,
        state=data.state,
        total_flats=data.total_flats,
        registration_number=data.registration_number,
        admin_id=admin_id,
    )
    db.add(society)
    db.commit()
    db.refresh(society)
    return society


def get_all_societies(db: Session):
    return db.query(Society).filter(Society.is_active == True).all()


def get_society_by_id(db: Session, society_id: int):
    return db.query(Society).filter(Society.id == society_id).first()


def update_society(db: Session, society: Society, data: SocietyUpdate):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(society, field, value)
    db.commit()
    db.refresh(society)
    return society


def deactivate_society(db: Session, society: Society):
    society.is_active = False
    db.commit()
    return society