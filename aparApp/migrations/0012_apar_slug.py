# Generated by Django 4.2 on 2023-04-11 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparApp', '0011_alter_apar_path_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='apar',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
