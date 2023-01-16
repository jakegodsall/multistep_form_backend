from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=32)
    cost = models.FloatField()
    yearly_offer = models.CharField(max_length=128)
    is_monthly = models.BooleanField()

    def __str__(self):
        return f"{self.name} (£{self.cost:.2f})"


class Addon(models.Model):
    identifier = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.name} (£{self.cost:.2f})"


class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)
    addons = models.ForeignKey(Addon, on_delete=models.CASCADE)
    total = models.FloatField()
