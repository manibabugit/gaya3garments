# Generated by Django 3.1 on 2020-09-15 18:38

from django.db import migrations, models
import g3garments.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_uploadimage_uploaded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='Img',
            field=models.FileField(storage=g3garments.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
