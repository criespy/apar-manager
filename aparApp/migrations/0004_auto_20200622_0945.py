# Generated by Django 3.0.7 on 2020-06-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0003_auto_20200622_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemeriksaan',
            name='keterangan',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
