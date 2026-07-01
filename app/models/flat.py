from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean
import enum

from app.db.base import Base, TimestampMixin


class FlatType(str, enum.Enum):
    owner = "owner"
    tenant = "tenant"
    vacant = "vacant"


class Flat(Base, TimestampMixin):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True, index=True)

    society_id = Column(
        Integer,
        ForeignKey("societies.id"),
        nullable=False,
    )

    flat_number = Column(String, nullable=False)

    floor = Column(Integer, nullable=True)

    type = Column(
        Enum(FlatType),
        default=FlatType.vacant,
    )

    is_active = Column(
        Boolean,
        default=True,
    )