# Generated by Django 3.1.7 on 2021-05-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210530_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='end',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
