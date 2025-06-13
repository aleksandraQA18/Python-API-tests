import logging

from faker import Faker

LOG = logging.getLogger("faker")
LOG.setLevel(logging.INFO)

fake = Faker()


def generate_user():
    """
    Generate a random user payload for testing.
    """
    return {
        "name": f"{fake.first_name()} {fake.last_name()}",
        "username": fake.user_name(),
        "email": fake.email(),
        "address": {
            "street": fake.street_address(),
            "suite": fake.building_number(),
            "city": fake.city(),
            "zipcode": fake.postcode(),
            "geo": {"lat": str(fake.latitude()), "lng": str(fake.longitude())},
        },
        "phone": fake.phone_number(),
        "website": fake.url(),
        "company": {
            "name": fake.company(),
            "catchPhrase": fake.catch_phrase(),
            "bs": fake.bs(),
        },
    }
