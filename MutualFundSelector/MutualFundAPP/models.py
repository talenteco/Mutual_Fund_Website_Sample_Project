from django.db import models

class users(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class mutualfund(models.Model):
    company = models.CharField(max_length = 100)
    theme = models.CharField(max_length = 100)
    risk = models.CharField(max_length = 50)
    minimum_hold_duration_years = models.IntegerField()
