# Generated by Django 4.0.4 on 2022-05-12 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xyStashStore', '0005_alter_fromcontactform_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fromcontactform',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
