from sqlalchemy import (
    VARCHAR,
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    DateTime,
    Boolean,
    UUID,
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
import uuid

Base = declarative_base()


class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer(), primary_key=True)
    # client_id = Column(
    #     UUID(as_uuid=True), ForeignKey("customers.id"), nullable=False
    # )
    # collaborator_id = Column(
    #     VARCHAR(36), ForeignKey("collaborators.id"), nullable=False
    # )
    total_amount = Column(Float, nullable=False)
    remaining_amount = Column(Float, nullable=False)
    creation_date = Column(DateTime, default=datetime.now, nullable=False)
    is_signed = Column(Boolean, default=False, nullable=False)

    # customers = relationship("Customer", back_populates="contracts")
    # collaborators = relationship("Collaborator", back_populates="contracts")
    # events = relationship("Event", back_populates="contracts")

    def __init__(
        self,
        client_id,
        collaborator_id,
        total_amount,
        remaining_amount,
        is_signed=False,
    ):
        self.id = uuid.uuid4()
        self.client_id = client_id
        self.collaborator_id = collaborator_id
        self.total_amount = total_amount
        self.remaining_amount = remaining_amount
        self.creation_date = datetime.now()
        self.is_signed = is_signed

    def __str__(self):
        return (
            f"Contract ID: {self.id}, "
            f"Client ID: {self.client_id}, "
            f"Collaborator ID: {self.collaborator_id}, "
            f"Total Amount: {self.total_amount}, "
            f"Remaining Amount: {self.remaining_amount}, "
            f"Creation Date: {self.creation_date}, "
            f"Status: {'Signed' if self.is_signed else 'Not Signed'}"
        )
