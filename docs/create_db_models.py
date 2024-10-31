# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Define the database engine and session
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Define data model classes

class Dog(Base):
    """description: Represents a dog that is part of the dog walking business."""
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey('owners.id'))

class Owner(Base):
    """description: Represents the owner of a dog."""
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)

class Walker(Base):
    """description: Represents a person who walks dogs."""
    __tablename__ = 'walkers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    experience_years = Column(Integer)
    hourly_rate = Column(Float)

class Walk(Base):
    """description: A scheduled walk for one or more dogs."""
    __tablename__ = 'walks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'))
    date_time = Column(DateTime)
    duration_minutes = Column(Integer)

class DogWalk(Base):
    """description: Junction table for many-to-many relationship between dogs and walks."""
    __tablename__ = 'dog_walks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    walk_id = Column(Integer, ForeignKey('walks.id'))

class Payment(Base):
    """description: Payment records for the dog walking service."""
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    walk_id = Column(Integer, ForeignKey('walks.id'))
    amount = Column(Float)
    payment_date = Column(DateTime, default=datetime.datetime.utcnow)

class Address(Base):
    """description: Address details for owners and walkers."""
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip_code = Column(String)
    owner_id = Column(Integer, ForeignKey('owners.id'), nullable=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'), nullable=True)

class Schedule(Base):
    """description: Scheduling details and availability for walkers."""
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'))
    available_from = Column(DateTime)
    available_to = Column(DateTime)

class Service(Base):
    """description: Different services offered by the business."""
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(Text)
    base_rate = Column(Float)

class WalkerService(Base):
    """description: Junction table for many-to-many relationship between walkers and services."""
    __tablename__ = 'walker_services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walker_id = Column(Integer, ForeignKey('walkers.id'))
    service_id = Column(Integer, ForeignKey('services.id'))

class Complaint(Base):
    """description: Represents complaints lodged by dog owners."""
    __tablename__ = 'complaints'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    description = Column(Text)
    complaint_date = Column(DateTime, default=datetime.datetime.utcnow)

class Feedback(Base):
    """description: Feedback from owners about the dog walking service."""
    __tablename__ = 'feedbacks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, ForeignKey('owners.id'))
    walker_id = Column(Integer, ForeignKey('walkers.id'))
    rating = Column(Integer)
    comments = Column(Text)
    feedback_date = Column(DateTime, default=datetime.datetime.utcnow)

class Promotion(Base):
    """description: Promotions and discounts offered to owners."""
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    discount_percentage = Column(Float)
    valid_from = Column(DateTime)
    valid_until = Column(DateTime)

class Enrollment(Base):
    """description: Records of dog enrollments for various walking plans."""
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    enrollment_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String)

class Incident(Base):
    """description: Incidents or issues that occurred during a walk."""
    __tablename__ = 'incidents'
    id = Column(Integer, primary_key=True, autoincrement=True)
    walk_id = Column(Integer, ForeignKey('walks.id'))
    description = Column(Text)
    incident_date = Column(DateTime)

# Create all tables
Base.metadata.create_all(engine)

# Create sample data
owners = [Owner(name=f"Owner {i}", phone_number=f"555-010{i}", email=f"owner{i}@example.com") for i in range(1, 6)]
walkers = [Walker(name=f"Walker {i}", experience_years=i, hourly_rate=15.0 + (i * 2)) for i in range(1, 6)]
dogs = [Dog(name=f"Dog {i}", breed="Breed A", age=2 + i, owner_id=owners[i % 5].id) for i in range(1, 11)]
walks = [Walk(walker_id=walkers[i % 5].id, date_time=datetime.datetime.now() + datetime.timedelta(days=i), duration_minutes=30 + (i * 5)) for i in range(10)]
dog_walks = [DogWalk(dog_id=dogs[i % 10].id, walk_id=walks[i % 10].id) for i in range(20)]
payments = [Payment(owner_id=owners[i % 5].id, walk_id=walks[i % 10].id, amount=30.0 + (i * 5)) for i in range(10)]
addresses = [Address(street=f"Street {i}", city="CityX", state="StateY", zip_code=f"1000{i}", owner_id=owners[i % 5].id) for i in range(5)]
addresses += [Address(street=f"Ave {i}", city="CityZ", state="StateY", zip_code=f"2000{i}", walker_id=walkers[i % 5].id) for i in range(5)]
schedules = [Schedule(walker_id=walkers[i % 5].id, available_from=datetime.datetime.now(), available_to=datetime.datetime.now() + datetime.timedelta(hours=8)) for i in range(10)]
services = [Service(name=f"Service {i}", description=f"Description of Service {i}", base_rate=20.0 + i) for i in range(5)]
walker_services = [WalkerService(walker_id=walkers[i % 5].id, service_id=services[i % 5].id) for i in range(10)]
complaints = [Complaint(owner_id=owners[i % 5].id, description=f"Complaint {i}") for i in range(5)]
feedbacks = [Feedback(owner_id=owners[i % 5].id, walker_id=walkers[i % 5].id, rating=4, comments=f"Good job by walker {walkers[i % 5].name}") for i in range(5)]
promotions = [Promotion(code=f"PROMO{i}", discount_percentage=10.0 + i, valid_from=datetime.datetime.now(), valid_until=datetime.datetime.now() + datetime.timedelta(days=30)) for i in range(5)]
enrollments = [Enrollment(dog_id=dogs[i % 10].id, service_id=services[i % 5].id, status="Active") for i in range(10)]
incidents = [Incident(walk_id=walks[i % 10].id, description=f"Incident {i}", incident_date=datetime.datetime.now() + datetime.timedelta(days=i)) for i in range(5)]

# Add to session and commit
session.add_all(owners + walkers + dogs + walks + dog_walks + payments + addresses + schedules + services + walker_services + complaints + feedbacks + promotions + enrollments + incidents)
session.commit()
