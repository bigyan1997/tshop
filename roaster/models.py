from django.db import models
from tshop import settings


class Roaster(models.Model):
    TIME_CHOICES = (
        ('no shift', 'No Shift'),
        ('8am - 5pm', '8am - 5pm'),
        ('9am - 5pm', '9am - 5pm'),
        ('10am - 5pm', '10am - 5pm'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    week_starting = models.DateField(null=True)
    monday = models.CharField(max_length=20,
                      choices=TIME_CHOICES,
                      default="no shift")
    monday = models.CharField(max_length=20,
                              choices=TIME_CHOICES,
                              default="no shift")
    tuesday = models.CharField(max_length=20,
                              choices=TIME_CHOICES,
                              default="no shift")
    wednesday = models.CharField(max_length=20,
                              choices=TIME_CHOICES,
                              default="no shift")
    thursday = models.CharField(max_length=20,
                              choices=TIME_CHOICES,
                              default="no shift")
    friday = models.CharField(max_length=20,
                              choices=TIME_CHOICES,
                              default="no shift")
    saturday = models.CharField(max_length=20,
                              choices=TIME_CHOICES,
                              default="no shift")
    sunday = models.CharField(max_length=20,
                              choices=TIME_CHOICES,
                              default="no shift")
