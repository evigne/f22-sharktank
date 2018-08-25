# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    season = models.IntegerField()
    episode = models.IntegerField()
    company=models.CharField(max_length=140)
    deal=models.CharField(max_length=140)
    industry=models.CharField(max_length=140)
    entrepreneur_gender=models.CharField(max_length=140)
    amount=models.IntegerField(default=0)
    equity=models.FloatField(default=0)
    valuation=models.IntegerField(default=0)
    corcoran=models.BooleanField()
    cuban=models.BooleanField()
    greiner=models.BooleanField()
    herjavec=models.BooleanField()
    john=models.BooleanField()
    olary=models.BooleanField()
    harrington=models.BooleanField()
    guests=models.BooleanField()
    no_of_sharks=models.IntegerField(default=0)
    investPer_shark=models.IntegerField(default=0)
    note=models.TextField()


    def __str__(self):
        return self.company

# Create your models here.
