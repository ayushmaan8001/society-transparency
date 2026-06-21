from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.db.base import Base, TimestampMixin


class Society(Base, TimestampMixin):
    __tablename__ = "societies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    total_flats = Column(Integer, nullable=True)
    registration_number = Column(String, nullable=True)
    admin_id = Column(
        Integer,
        ForeignKey("users.id", use_alter=True, name="fk_society_admin_id"),
        nullable=True,
    )
    is_active = Column(Boolean, default=True)