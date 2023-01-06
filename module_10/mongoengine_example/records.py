from mongoengine_example.models import Contact, Phone, Email
# import connect


class Record:
    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"name: {self.name}, phone: {self.phone}, email: {self.email}"

    def save_contact(self):
        contact = Contact(name=self.name)
        contact.save()

    def save_phone(self):
        phone = Phone(phone=self.phone, contact=self.find_contact_by_name())
        phone.save()

    def save_email(self):
        email = Email(email=self.email, contact=self.find_contact_by_name())
        email.save()

    def find_contact(self):
        contact = Contact.objects()
        contact_lict = []
        for con in contact:
            contact_lict.append(con.to_mongo().to_dict())
        return contact_lict

    def find_contact_by_name(self):
        for contact in Contact.objects(name=self.name):
            return contact

    def find_phone(self):
        phone = Phone.objects(contact=self.find_contact_by_name())
        return phone

    def find_email(self):
        email = Email.objects(contact=self.find_contact_by_name())
        return email

    def update_name(self, old_name):
        contact = Contact.objects(name=old_name)
        contact.update(name=self.name)

    def update_phone(self, old_phone):
        phone = Phone.objects(phone=old_phone)
        phone.update(phone=self.phone)

    def update_email(self, old_email):
        email = Email.objects(email=old_email)
        email.update(email=self.email)

    def remove_contact(self):
        con = Contact.objects(name=self.name)
        con.delete()

    def remove_phone(self):
        phone = Phone.objects(phone=self.phone)
        phone.delete()

    def remove_email(self):
        email = Email.objects(email=self.email)
        email.delete()
