# Generated by Django 4.1 on 2023-01-19 10:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appFunctional', '0006_alter_modelposteo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelposteo',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
