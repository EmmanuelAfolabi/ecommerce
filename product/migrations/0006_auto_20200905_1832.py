# Generated by Django 2.1.3 on 2020-09-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200905_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('gown', 'gown'), ('short', 'short'), ('bonnet', 'bonnet')], max_length=30, null=True),
        ),
    ]