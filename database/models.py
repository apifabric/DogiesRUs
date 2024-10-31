# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 31, 2024 00:38:04
# Database: sqlite:////tmp/tmp.i8ssyFEu3B/DogiesRUs/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Owner(SAFRSBaseX, Base):
    """
    description: Represents the owner of a dog.
    """
    __tablename__ = 'owners'
    _s_collection_name = 'Owner'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AddressList : Mapped[List["Address"]] = relationship(back_populates="owner")
    ComplaintList : Mapped[List["Complaint"]] = relationship(back_populates="owner")
    DogList : Mapped[List["Dog"]] = relationship(back_populates="owner")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="owner")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="owner")



class Promotion(SAFRSBaseX, Base):
    """
    description: Promotions and discounts offered to owners.
    """
    __tablename__ = 'promotions'
    _s_collection_name = 'Promotion'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    discount_percentage = Column(Float)
    valid_from = Column(DateTime)
    valid_until = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Service(SAFRSBaseX, Base):
    """
    description: Different services offered by the business.
    """
    __tablename__ = 'services'
    _s_collection_name = 'Service'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    base_rate = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    WalkerServiceList : Mapped[List["WalkerService"]] = relationship(back_populates="service")
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="service")



class Walker(SAFRSBaseX, Base):
    """
    description: Represents a person who walks dogs.
    """
    __tablename__ = 'walkers'
    _s_collection_name = 'Walker'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    experience_years = Column(Integer)
    hourly_rate = Column(Float)

    # parent relationships (access parent)

    # child relationships (access children)
    AddressList : Mapped[List["Address"]] = relationship(back_populates="walker")
    FeedbackList : Mapped[List["Feedback"]] = relationship(back_populates="walker")
    ScheduleList : Mapped[List["Schedule"]] = relationship(back_populates="walker")
    WalkerServiceList : Mapped[List["WalkerService"]] = relationship(back_populates="walker")
    WalkList : Mapped[List["Walk"]] = relationship(back_populates="walker")



class Address(SAFRSBaseX, Base):
    """
    description: Address details for owners and walkers.
    """
    __tablename__ = 'addresses'
    _s_collection_name = 'Address'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    owner_id = Column(ForeignKey('owners.id'))
    walker_id = Column(ForeignKey('walkers.id'))

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("AddressList"))
    walker : Mapped["Walker"] = relationship(back_populates=("AddressList"))

    # child relationships (access children)



class Complaint(SAFRSBaseX, Base):
    """
    description: Represents complaints lodged by dog owners.
    """
    __tablename__ = 'complaints'
    _s_collection_name = 'Complaint'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owners.id'))
    description = Column(Text)
    complaint_date = Column(DateTime)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("ComplaintList"))

    # child relationships (access children)



class Dog(SAFRSBaseX, Base):
    """
    description: Represents a dog that is part of the dog walking business.
    """
    __tablename__ = 'dogs'
    _s_collection_name = 'Dog'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(ForeignKey('owners.id'))

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("DogList"))

    # child relationships (access children)
    DogWalkList : Mapped[List["DogWalk"]] = relationship(back_populates="dog")
    EnrollmentList : Mapped[List["Enrollment"]] = relationship(back_populates="dog")



class Feedback(SAFRSBaseX, Base):
    """
    description: Feedback from owners about the dog walking service.
    """
    __tablename__ = 'feedbacks'
    _s_collection_name = 'Feedback'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owners.id'))
    walker_id = Column(ForeignKey('walkers.id'))
    rating = Column(Integer)
    comments = Column(Text)
    feedback_date = Column(DateTime)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("FeedbackList"))
    walker : Mapped["Walker"] = relationship(back_populates=("FeedbackList"))

    # child relationships (access children)



class Schedule(SAFRSBaseX, Base):
    """
    description: Scheduling details and availability for walkers.
    """
    __tablename__ = 'schedules'
    _s_collection_name = 'Schedule'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'))
    available_from = Column(DateTime)
    available_to = Column(DateTime)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("ScheduleList"))

    # child relationships (access children)



class WalkerService(SAFRSBaseX, Base):
    """
    description: Junction table for many-to-many relationship between walkers and services.
    """
    __tablename__ = 'walker_services'
    _s_collection_name = 'WalkerService'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'))
    service_id = Column(ForeignKey('services.id'))

    # parent relationships (access parent)
    service : Mapped["Service"] = relationship(back_populates=("WalkerServiceList"))
    walker : Mapped["Walker"] = relationship(back_populates=("WalkerServiceList"))

    # child relationships (access children)



class Walk(SAFRSBaseX, Base):
    """
    description: A scheduled walk for one or more dogs.
    """
    __tablename__ = 'walks'
    _s_collection_name = 'Walk'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walker_id = Column(ForeignKey('walkers.id'))
    date_time = Column(DateTime)
    duration_minutes = Column(Integer)

    # parent relationships (access parent)
    walker : Mapped["Walker"] = relationship(back_populates=("WalkList"))

    # child relationships (access children)
    DogWalkList : Mapped[List["DogWalk"]] = relationship(back_populates="walk")
    IncidentList : Mapped[List["Incident"]] = relationship(back_populates="walk")
    PaymentList : Mapped[List["Payment"]] = relationship(back_populates="walk")



class DogWalk(SAFRSBaseX, Base):
    """
    description: Junction table for many-to-many relationship between dogs and walks.
    """
    __tablename__ = 'dog_walks'
    _s_collection_name = 'DogWalk'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dog_id = Column(ForeignKey('dogs.id'))
    walk_id = Column(ForeignKey('walks.id'))

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("DogWalkList"))
    walk : Mapped["Walk"] = relationship(back_populates=("DogWalkList"))

    # child relationships (access children)



class Enrollment(SAFRSBaseX, Base):
    """
    description: Records of dog enrollments for various walking plans.
    """
    __tablename__ = 'enrollments'
    _s_collection_name = 'Enrollment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    dog_id = Column(ForeignKey('dogs.id'))
    service_id = Column(ForeignKey('services.id'))
    enrollment_date = Column(DateTime)
    status = Column(String)

    # parent relationships (access parent)
    dog : Mapped["Dog"] = relationship(back_populates=("EnrollmentList"))
    service : Mapped["Service"] = relationship(back_populates=("EnrollmentList"))

    # child relationships (access children)



class Incident(SAFRSBaseX, Base):
    """
    description: Incidents or issues that occurred during a walk.
    """
    __tablename__ = 'incidents'
    _s_collection_name = 'Incident'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    walk_id = Column(ForeignKey('walks.id'))
    description = Column(Text)
    incident_date = Column(DateTime)

    # parent relationships (access parent)
    walk : Mapped["Walk"] = relationship(back_populates=("IncidentList"))

    # child relationships (access children)



class Payment(SAFRSBaseX, Base):
    """
    description: Payment records for the dog walking service.
    """
    __tablename__ = 'payments'
    _s_collection_name = 'Payment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('owners.id'))
    walk_id = Column(ForeignKey('walks.id'))
    amount = Column(Float)
    payment_date = Column(DateTime)

    # parent relationships (access parent)
    owner : Mapped["Owner"] = relationship(back_populates=("PaymentList"))
    walk : Mapped["Walk"] = relationship(back_populates=("PaymentList"))

    # child relationships (access children)
