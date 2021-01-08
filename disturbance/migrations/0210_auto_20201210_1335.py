# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-12-10 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0209_auto_20201207_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationtype',
            name='domain_used',
            field=models.CharField(choices=[('das', 'DAS'), ('apiary', 'Apiary')], default='das', max_length=40),
        ),
        migrations.AlterField(
            model_name='proposaltype',
            name='name',
            field=models.CharField(choices=[('Disturbance', 'Disturbance')], default='Disturbance', max_length=64, verbose_name='Application name (eg. Disturbance, Apiary)'),
        ),
    ]