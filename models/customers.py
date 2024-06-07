from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import (
    CHAR,
    VARCHAR,
    Column,
    Integer,
    String,
    ForeignKey,
    UUID,
    DateTime,
)
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
import uuid


Base = declarative_base()


class Customer(Base):

    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True)
    phone_number = Column(String(20), unique=True, index=True)
    compagny_name = Column(String(100), unique=False, index=True)
    creation_date = Column(DateTime, default=datetime.now)
    last_contact_date = Column(DateTime, default=datetime.now)
    # sales_id = Column(Integer(), ForeignKey("users.id"), nullable=True)
    # sales = relationship("User", back_populates="customers")
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # user = relationship("User", back_populates="contract")

    def __init__(
        self,
        first_name,
        last_name,
        email,
        phone_number,
        compagny_name,
        sales_id,
    ):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.compagny_name = compagny_name

        self.sales_id = sales_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
