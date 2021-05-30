# Generated by Django 3.1.7 on 2021-05-30 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='end',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(choices=[('9', '9 Days'), ('15', '15 Days'), ('21', '21 Days')], max_length=2),
        ),
    ]