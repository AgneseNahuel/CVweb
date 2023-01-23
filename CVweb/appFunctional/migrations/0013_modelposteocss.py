# Generated by Django 4.1 on 2023-01-22 04:02

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appFunctional', '0012_rename_modelposteo_modelposteopython'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelPosteoCSS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='TEXTO EJEMPLO', max_length=50)),
                ('Field', ckeditor_uploader.fields.RichTextUploadingField()),
                ('Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]