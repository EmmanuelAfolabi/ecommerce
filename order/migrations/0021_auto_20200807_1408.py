# Generated by Django 2.1.3 on 2020-08-07 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_auto_20200807_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 7, 14, 8, 49, 866535)),
        ),
    ]
