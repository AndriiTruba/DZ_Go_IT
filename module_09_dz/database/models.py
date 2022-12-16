from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column('phone', String(100), nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship(Contact)


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column('email', String(100), nullable=False)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    contact = relationship(Contact)


# class Contact(Base):
#     __tablename__ = 'Contacts'
#     id = Column(Integer, primary_key=True)
#     name_id = Column('name_id', ForeignKey('name.id', ondelete='CASCADE'))
#     phone_id = Column('phone_id', ForeignKey('phone.id', ondelete='CASCADE'))
#     email_id = Column('email_id', ForeignKey('email.id', ondelete='CASCADE'))

