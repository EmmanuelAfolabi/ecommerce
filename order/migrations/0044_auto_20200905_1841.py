# Generated by Django 2.1.3 on 2020-09-05 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0043_auto_20200905_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 5, 18, 41, 46, 507827)),
        ),
    ]
