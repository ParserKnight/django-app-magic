# Generated by Django 2.1.2 on 2018-11-01 10:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magicdb', '0002_auto_20181027_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='users',
            field=models.ManyToManyField(related_name='cards', to=settings.AUTH_USER_MODEL),
        ),
    ]
