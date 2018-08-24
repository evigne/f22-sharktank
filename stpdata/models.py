# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    company=models.CharField(max_length=140)
    industry=models.CharField(max_length=140)
    entrepreneur_gender=models.CharField(max_length=140)

    def __str__(self):
        return self.company
    
# Create your models here.
