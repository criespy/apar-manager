# Generated by Django 3.0.7 on 2020-06-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0002_auto_20200622_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apar',
            name='expired',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apar',
            name='tanggal_periksa',
            field=models.DateField(blank=True, null=True),
        ),
    ]