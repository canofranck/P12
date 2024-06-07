# import uuid

# from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey, UUID, DateTime

# Base = declarative_base()


# class Event(Base):

#     __tablename__ = "events"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     contract_id = Column(UUID, ForeignKey("contract.id"))
#     collaborator_id = Column(UUID, ForeignKey("collaborator.id"))
#     customer_id = Column(UUID, ForeignKey("customers.id"))
#     event_name = Column(String(50), unique=True, index=True)
#     start_date = Column(DateTime, unique=False, index=True)
#     end_date = Column(DateTime, unique=False, index=True)
#     location = Column(String(50), unique=False, index=True)
#     nb_attendees = Column(Integer, unique=False, index=False)
#     notes = Column(String(200), unique=False, index=False)

#     contacts = relationship("Collaborator", back_populates="events")
#     customers = relationship("Customer", back_populates="events")
#     contracts = relationship("Contract", back_populates="events")

#     def __init__(
#         self,
#         event_name,
#         start_date,
#         end_date,
#         location,
#         nb_attendees,
#         notes,
#         customer,
#         contract,
#         contact=None,
#     ):
#         self.id = uuid.uuid4()
#         self.name = event_name
#         self.start_date = start_date
#         self.end_date = end_date
#         self.location = location
#         self.attendees = nb_attendees
#         self.notes = notes

#         self.customer = customer
#         self.contact = contact
#         self.contract = contract

#     def __str__(self):
#         return f"Event {self.id} - Name: {self.event_name} - Start: {self.start_date} - End: {self.end_date} - Location: {self.location} - Attendees: {self.nb_attendees}"
