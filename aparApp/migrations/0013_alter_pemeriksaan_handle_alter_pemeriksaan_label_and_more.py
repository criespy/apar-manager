# Generated by Django 4.2 on 2023-04-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0012_apar_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemeriksaan',
            name='handle',
            field=models.CharField(choices=[('OK', 'OK'), ('Not OK', 'Not OK')], default='Not OK', max_length=10),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='label',
            field=models.CharField(choices=[('OK', 'OK'), ('Not OK', 'Not OK')], default='Not OK', max_length=10),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='pin',
            field=models.CharField(choices=[('OK', 'OK'), ('Not OK', 'Not OK')], default='Not OK', max_length=10),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='selang',
            field=models.CharField(choices=[('OK', 'OK'), ('Not OK', 'Not OK')], default='Not OK', max_length=10),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='tabung',
            field=models.CharField(choices=[('OK', 'OK'), ('Not OK', 'Not OK')], default='Not OK', max_length=10),
        ),
        migrations.AlterField(
            model_name='pemeriksaan',
            name='tekanan',
            field=models.CharField(choices=[('OK', 'OK'), ('Not OK', 'Not OK')], default='Not OK', max_length=10),
        ),
    ]