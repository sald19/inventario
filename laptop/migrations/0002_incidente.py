# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
