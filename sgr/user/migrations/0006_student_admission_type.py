# Generated by Django 3.0.6 on 2020-06-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200606_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_type',
            field=models.CharField(default='first year', max_length=15),
            preserve_default=False,
        ),
    ]
