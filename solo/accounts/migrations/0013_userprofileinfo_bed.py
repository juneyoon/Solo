# Generated by Django 2.1.5 on 2019-04-22 00:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20190421_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='bed',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
