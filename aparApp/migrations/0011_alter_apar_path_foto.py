# Generated by Django 4.2 on 2023-04-06 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0010_apar_path_qr_alter_apar_id_alter_pemeriksaan_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apar',
            name='path_foto',
            field=models.ImageField(upload_to='images/%Y%m'),
        ),
    ]
