# Generated by Django 2.1.3 on 2020-08-07 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20200807_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 7, 4, 42, 3, 970228)),
        ),
    ]
