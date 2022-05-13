# Generated by Django 4.0.4 on 2022-05-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xyStashStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_fname', models.CharField(max_length=50)),
                ('db_lname', models.CharField(max_length=50)),
                ('db_email', models.CharField(max_length=100)),
                ('db_username', models.CharField(max_length=100)),
                ('db_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created',)},
        ),
    ]
