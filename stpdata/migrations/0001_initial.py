# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-24 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=140)),
                ('industry', models.CharField(max_length=140)),
                ('entrepreneur_gender', models.CharField(max_length=140)),
            ],
        ),
    ]
