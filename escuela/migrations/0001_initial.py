# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escuela.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('escuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escuela.Escuela')),
                ('laptop', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='laptop.Laptop')),
            ],
        ),
        migrations.AddField(
            model_name='escuela',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escuela.Municipio'),
        ),
    ]