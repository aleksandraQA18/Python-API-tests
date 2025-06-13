import logging
from random import randint

from faker import Faker

LOG = logging.getLogger("faker")
LOG.setLevel(logging.INFO)

fake = Faker()


def generate_post():
    """
    Generate a random post payload for testing.
    """
    return {
        "title": fake.word(),
        "body": fake.sentence(nb_words=10),
        "userId": randint(1, 5),
    }
