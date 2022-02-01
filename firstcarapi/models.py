import datetime
from django.db import models
from datetime import timezone
from django.db.models.signals import pre_save, post_save

class Car(models.Model):
    unit = models.CharField(max_length=20, primary_key=True)
    mileage = models.IntegerField()
    manufacturer = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    updated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.unit

class UpdatedMileage(models.Model):
    updated_unit = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

def update_mileage(sender, instance, **kwargs):
    if Car.objects.get(updated=True):
        UpdatedMileage.objects.create(updated_unit=instance)

post_save.connect(update_mileage, sender=Car)
