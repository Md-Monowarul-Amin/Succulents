from django.db import models

# Create your models here.
from django.db import models
from enums.models import CountryTypes
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=1500, blank=True)
    # importedFrom = models.IntegerField(choices=CountryTypes.choices(), default=CountryTypes.BANGLADESH)
    buyingPrice = models.IntegerField("buyingPrice", blank=True, default=0)
    sellingPrice = models.IntegerField("sellingPrice", blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    ownerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    carImg = models.ImageField(upload_to='images/')


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
