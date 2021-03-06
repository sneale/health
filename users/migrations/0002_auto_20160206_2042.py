# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, db_index=True, verbose_name='Date')),
                ('index', models.IntegerField(db_index=True, default=1)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='BFM',
            fields=[
                ('healthdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.HealthData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bfm', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('users.healthdata',),
        ),
        migrations.CreateModel(
            name='PBF',
            fields=[
                ('healthdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.HealthData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pbf', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('users.healthdata',),
        ),
        migrations.CreateModel(
            name='SMM',
            fields=[
                ('healthdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.HealthData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smm', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('users.healthdata',),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('healthdata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.HealthData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('users.healthdata',),
        ),
    ]
