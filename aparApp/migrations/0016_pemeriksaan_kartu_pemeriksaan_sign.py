# Generated by Django 4.2 on 2023-04-14 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0015_alter_pemeriksaan_handle_alter_pemeriksaan_label_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pemeriksaan',
            name='kartu',
            field=models.BooleanField(choices=[(True, 'OK'), (False, 'Tidak OK')], default=False),
        ),
        migrations.AddField(
            model_name='pemeriksaan',
            name='sign',
            field=models.BooleanField(choices=[(True, 'OK'), (False, 'Tidak OK')], default=False),
        ),
    ]