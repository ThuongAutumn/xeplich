# Generated by Django 3.1.7 on 2021-05-30 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210530_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='number_student',
            field=models.IntegerField(default=0),
        ),
    ]
