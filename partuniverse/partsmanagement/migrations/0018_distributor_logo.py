# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsmanagement', '0017_transaction_reverted'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='logo',
            field=models.ImageField(blank=True, help_text='The logo of the company.', null=True, upload_to=b'uploads/logos/'),
        ),
    ]
