# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 20:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_customer_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='manager',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='customers_managed', to=settings.AUTH_USER_MODEL),
        ),
    ]
