# Generated by Django 4.2.2 on 2023-07-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_customuser_tel_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reset_password_token',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
