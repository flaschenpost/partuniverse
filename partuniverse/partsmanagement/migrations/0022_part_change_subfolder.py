# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsmanagement', '0021_adding_logo_and_url_to_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='pic',
            field=models.ImageField(blank=True, help_text='The actual image.', null=True, upload_to=b'part'),
        ),
    ]
