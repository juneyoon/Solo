# Generated by Django 2.1.5 on 2019-04-24 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20190424_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='Dorm_Choice_Third',
            new_name='Dorm_Choice_Three',
        ),
    ]