# Generated by Django 2.1.3 on 2020-09-02 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0038_auto_20200902_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 2, 2, 20, 29, 575913)),
        ),
    ]
