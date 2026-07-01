from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    Date,
    Enum,
    ForeignKey,
    Float,
)
import enum

from app.db.base import Base, TimestampMixin


class OccupancyType(str, enum.Enum):
    owner = "owner"
    tenant = "tenant"
    family = "family"
    caretaker = "caretaker"


class FlatOccupancy(Base, TimestampMixin):
    __tablename__ = "flat_occupancies"

    id = Column(Integer, primary_key=True, index=True)

    flat_id = Column(
        Integer,
        ForeignKey("flats.id", use_alter=True, name="fk_occupancy_flat_id"),
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id", use_alter=True, name="fk_occupancy_user_id"),
        nullable=False,
    )

    occupancy_type = Column(
        Enum(OccupancyType),
        nullable=False,
    )

    ownership_percentage = Column(
        Float,
        nullable=True,
    )

    move_in_date = Column(
        Date,
        nullable=True,
    )

    move_out_date = Column(
        Date,
        nullable=True,
    )

    is_current = Column(
        Boolean,
        default=True,
    )

    verified_by = Column(
        Integer,
        ForeignKey("users.id", use_alter=True, name="fk_verified_by"),
        nullable=True,
    )