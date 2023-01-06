from mongoengine import Document, StringField, ReferenceField, connect, CASCADE

connect(db='web7', host='mongodb://localhost:27017')


class Contact(Document):
    name = StringField(required=True, max_length=50, unique=True)


class Phone(Document):
    phone = StringField(max_length=120, required=True, unique=True)
    contact = ReferenceField(Contact, reverse_delete_rule=CASCADE)


class Email(Document):
    email = StringField(max_length=120, required=True, unique=True)
    contact = ReferenceField(Contact, reverse_delete_rule=CASCADE)

