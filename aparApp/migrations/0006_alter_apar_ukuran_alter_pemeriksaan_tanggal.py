# Generated by Django 4.1.1 on 2022-09-20 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0005_auto_20200622_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apar',
            name='ukuran',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 20, 2, 48, 37, 86709, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
