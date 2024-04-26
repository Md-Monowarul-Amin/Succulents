from django.db import models
from enums.models import CountryTypes
# Create your models here.

class Succulent(models.Model):
    name = models.CharField(max_length=150, blank=True)
    succulent_type = models.CharField(max_length=150, blank=True)
    importedFrom = models.IntegerField(choices=CountryTypes.choices(), default=CountryTypes.BANGLADESH)
    buyingPrice = models.IntegerField("buyingPrice", blank=True, default=0)
    sellingPrice = models.IntegerField("sellingPrice", blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)


    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['first_name']

    # objects = CustomUserManager()

    def __str__(self):
        return self.name


"""{
"name":"ABC",
"succulent_type":"Big",
"importedFrom":0,
"buyingPrice":100,
"sellingPrice":150
}
"""
