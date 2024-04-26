from django.db import models

# Create your models here.
from enum import IntEnum

class CountryTypes(IntEnum):
    BANGLADESH = 0
    INDIA = 1
    THILAND = 2
    CHINA = 3
    VIETNAM = 4
    PHILIPINES = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
