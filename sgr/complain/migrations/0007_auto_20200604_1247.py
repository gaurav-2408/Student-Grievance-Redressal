# Generated by Django 3.0.6 on 2020-06-04 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0006_auto_20200604_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complain',
            old_name='registered_datetime',
            new_name='reg_datetime',
        ),
    ]
