# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='grado',
            field=models.CharField(choices=[('K', 'Preescolar'), ('1', '1-Primer'), ('2', '2-Segundo'), ('3', '3-Tercer'), ('4', '4-Cuarto'), ('5', '5-Quinto'), ('6', '6-Sexto'), ('D', 'Docente'), ('P', 'Director'), ('V', 'Voluntario')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
