# Generated by Django 3.2.7 on 2021-09-15 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20210915_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 15, 2, 58)),
        ),
    ]