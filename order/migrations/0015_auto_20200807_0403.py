# Generated by Django 2.1.3 on 2020-08-07 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20200807_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 7, 4, 3, 48, 306605)),
        ),
    ]
