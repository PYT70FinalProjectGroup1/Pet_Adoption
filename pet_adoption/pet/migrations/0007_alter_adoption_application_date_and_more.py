# Generated by Django 4.0.6 on 2023-08-20 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_alter_adoption_application_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='application_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 20, 15, 17, 41, 169081, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='animal',
            name='registration',
            field=models.DateField(default=datetime.datetime(2023, 8, 20, 15, 17, 41, 168060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 20, 15, 17, 41, 169081, tzinfo=utc)),
        ),
    ]
