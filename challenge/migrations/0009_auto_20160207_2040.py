# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 20:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_auto_20160207_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers_managed', to=settings.AUTH_USER_MODEL),
        ),
    ]