from datetime import datetime

from mongoengine import Document
from mongoengine.fields import DateField, EmailField, BooleanField, StringField



class Contacts(Document):
    fullname = StringField(required=True)
    email = EmailField(required=True)
    phone = StringField(required=True)
    preferable = StringField(choices=["sms", "email"], required=True)
    sent = BooleanField(default=False)
    birthday = DateField()
