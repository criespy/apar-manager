# Generated by Django 4.1.1 on 2022-09-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0009_apar_path_foto_alter_pemeriksaan_tanggal'),
    ]

    operations = [
        migrations.AddField(
            model_name='apar',
            name='path_QR',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='apar',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='tanggal',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
