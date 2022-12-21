from database.db import session
from database.models import Contact, Phone, Email
from sqlalchemy import and_


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class CellPhone(Field):
    @Field.value.setter
    def value(self, value):
        self._value = value


class EmailAddress(Field):
    @Field.value.setter
    def value(self, value):
        self._value = value


class Record:
    def __init__(self, name: Name = None, phones: CellPhone = None, emails: EmailAddress = None):
        self.name = name
        self.phones = phones
        self.emails = emails

    def __repr__(self):
        return f"name: {self.name.value}, phone: {self.phones.value}, email: {self.emails.value}"

    def save_contact(self):
        contacts = Contact(
            name=self.name.value
        )
        session.add(contacts)
        session.commit()
        session.close()

    def save_phone(self):
        contact = session.query(Contact).filter(Contact.name == self.name.value).first()
        phones = Phone(
            phone=self.phones.value,
            contact_id=contact.id
        )
        session.add(phones)
        session.commit()
        session.close()

    def save_email(self):
        contact = session.query(Contact).filter(Contact.name == self.name.value).first()
        emails = Email(
            email=self.emails.value,
            contact_id=contact.id
        )
        session.add(emails)
        session.commit()
        session.close()

    def get_contact_by_name(self):
        contact = session.query(Contact).filter(Contact.name == self.name.value).first()
        session.close()
        return contact

    def get_all_phones(self):
        phones = session.query(Phone).all()
        return phones

    def get_phones(self, contact):
        phones = session.query(Phone).filter(Phone.contact == contact).all()
        return phones

    def get_emails(self, contact):
        emails = session.query(Email).filter(Email.contact == contact).all()
        return emails

    def get_all_emails(self):
        emails = session.query(Email).all()
        return emails

    def get_all_contact(self):
        contact = session.query(Contact).all()
        return contact

    def update_name(self, old_name):
        contact = session.query(Contact).filter(Contact.name == old_name)
        contact.update({'name': self.name.value})
        session.commit()
        session.close()
        return contact.first()

    def update_phone(self, id_):
        phone = session.query(Phone).filter(and_(Phone.id == id_, Phone.contact == self.get_contact_by_name()))
        phone.update({'phone': self.phones.value})
        session.commit()
        session.close()
        return phone.first()

    def update_email(self, id_):
        email = session.query(Email).filter(and_(Email.id == id_, Email.contact == self.get_contact_by_name()))
        email.update({'email': self.emails.value})
        session.commit()
        session.close()
        return email.first()

    def remove_contact(self, id_):
        contact = session.query(Contact).filter(Contact.id == id_)
        contact.delete()
        session.commit()
        session.close()

    def remove_phone(self, id_, contact):
        phone = session.query(Phone).filter(and_(Phone.id == id_, Phone.contact == contact))
        phone.delete()
        session.commit()
        session.close()
        return phone

    def remove_email(self, id_, contact):
        email = session.query(Email).filter(and_(Email.id == id_, Email.contact == contact))
        email.delete()
        session.commit()
        session.close()
        return email