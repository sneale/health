# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160207_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='challenge.Customer'),
        ),
    ]