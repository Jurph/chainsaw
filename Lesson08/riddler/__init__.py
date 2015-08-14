from .db import JOKES
import random


def get_joke():
    return random.choice(JOKES)

