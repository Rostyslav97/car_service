from django.db import models
from django.conf import settings


class City(models.Model):
    name = models.CharField("City", max_length=50)

    def __str__(self):
        return self.name


class Defect(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, null=False, blank=False)
    adress = models.TextField("Adress")
    car = models.CharField(max_length=40)
    description = models.TextField("Description")
    price = models.PositiveIntegerField("Price", help_text = "Put amount in hrn")
    created_at = models.DateTimeField(auto_now_add=True)
    service_arrival_time = models.DateTimeField("Arrival")
    image = models.ImageField(null=True, blank=True)

    STATUS_CHOICES = (
        ('D', 'Done'),
        ('N', 'Not Done')
    )

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='N')
    