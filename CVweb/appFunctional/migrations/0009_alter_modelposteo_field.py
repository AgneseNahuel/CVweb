# Generated by Django 4.1 on 2023-01-20 12:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appFunctional', '0008_alter_modelposteo_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelposteo',
            name='Field',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=1000),
        ),
    ]