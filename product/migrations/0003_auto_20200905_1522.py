# Generated by Django 2.1.3 on 2020-09-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200902_0220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('gown', 'gown'), ('short', 'short'), ('bonnet', 'bonnet')], max_length=30, null=True),
        ),
    ]
