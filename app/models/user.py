from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
import enum

from app.db.base import Base, TimestampMixin


class UserRole(str, enum.Enum):
    super_admin = "super_admin"
    society_admin = "society_admin"
    resident_owner = "resident_owner"
    resident_tenant = "resident_tenant"
    security = "security"


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    password_hash = Column(String, nullable=False)

    phone_number = Column(String, nullable=True)

    role = Column(Enum(UserRole), nullable=False)

    society_id = Column(
        Integer,
        ForeignKey("societies.id", use_alter=True, name="fk_user_society_id"),
        nullable=True,
    )

    is_active = Column(Boolean, default=True)