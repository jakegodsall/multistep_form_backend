from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=32)
    cost = models.FloatField()
    yearly_offer = models.CharField(max_length=128)
    is_monthly = models.BooleanField()


class Addon(models.Model):
    identifier = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    cost = models.FloatField()


class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)
    addons = models.ForeignKey(Addon, on_delete=models.CASCADE)
