# Generated by Django 4.1 on 2023-01-19 09:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appFunctional', '0002_remove_modelpost_image_alter_modelpost_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelpost',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2023, 1, 19, 9, 56, 52, 547961, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='modelPosteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='TEXTO EJEMPLO', max_length=50)),
                ('Field', models.TextField(max_length=50)),
                ('Time', models.TimeField(default=datetime.datetime(2023, 1, 19, 9, 56, 52, 547961, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]