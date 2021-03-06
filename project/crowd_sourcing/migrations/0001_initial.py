# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('payee_location', models.CharField(max_length=255)),
                ('payee_sex', models.CharField(max_length=255)),
                ('payee_age', models.IntegerField()),
                ('payee_country', models.CharField(max_length=255)),
            ],
        ),
    ]
