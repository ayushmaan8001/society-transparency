from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum

from app.db.base import Base, TimestampMixin


class FlatType(str, enum.Enum):
    owner = "owner"
    tenant = "tenant"
    vacant = "vacant"


class Flat(Base, TimestampMixin):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True, index=True)
    society_id = Column(Integer, ForeignKey("societies.id"), nullable=False)
    flat_number = Column(String, nullable=False)
    floor = Column(Integer, nullable=True)
    type = Column(Enum(FlatType), default=FlatType.vacant)
    owner_id = Column(
        Integer,
        ForeignKey("users.id", use_alter=True, name="fk_flat_owner_id"),
        nullable=True,
    )
    tenant_id = Column(
        Integer,
        ForeignKey("users.id", use_alter=True, name="fk_flat_tenant_id"),
        nullable=True,
    )