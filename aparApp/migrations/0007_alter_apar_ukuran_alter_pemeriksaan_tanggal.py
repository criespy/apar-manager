# Generated by Django 4.1.1 on 2022-09-20 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0006_alter_apar_ukuran_alter_pemeriksaan_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apar',
            name='ukuran',
            field=models.IntegerField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='tanggal',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 9, 20, 2, 51, 16, 665347, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
