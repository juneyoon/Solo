# Generated by Django 2.1.5 on 2019-04-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20190424_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='cleanliness',
            field=models.IntegerField(default=3, max_length=2),
        ),
    ]
