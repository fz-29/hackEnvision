# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fblogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbid', models.CharField(max_length=40)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
