# Generated by Django 4.1 on 2023-01-19 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modelPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='TEXTO EJEMPLO', max_length=50)),
                ('Field', models.TextField(max_length=50)),
                ('Time', models.TimeField(verbose_name=datetime.datetime(2023, 1, 19, 9, 39, 7, 457610, tzinfo=datetime.timezone.utc))),
                ('image', models.ImageField(default=None, upload_to='')),
            ],
        ),
    ]
