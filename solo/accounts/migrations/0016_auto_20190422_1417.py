# Generated by Django 2.1.5 on 2019-04-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20190422_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='bed',
            field=models.CharField(choices=[('E', 'Early Riser'), ('L', 'Late Riser')], default=None, max_length=1),
        ),
    ]
