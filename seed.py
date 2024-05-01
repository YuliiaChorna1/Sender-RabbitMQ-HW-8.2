import connect
import random
from faker import Faker
from models import Contacts

fake_data = Faker()

def generate_fake_contacts(contacts_number):
    for contact in range(contacts_number):
        contact = Contacts(
            fullname=fake_data.name(),
            email=fake_data.email(),
            phone=fake_data.phone_number(),
            preferable=random.choice(["sms", "email"]),
            birthday=fake_data.date_of_birth(minimum_age=18, maximum_age=100)
        )
        contact.save()

def main():
    generate_fake_contacts(contacts_number=5)

if __name__ == '__main__':
    main()