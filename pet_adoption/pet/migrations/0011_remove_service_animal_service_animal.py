# Generated by Django 4.0.6 on 2023-08-20 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0010_rename_services_service_rename_treatments_treatment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='animal',
        ),
        migrations.AddField(
            model_name='service',
            name='animal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pet.animal'),
            preserve_default=False,
        ),
    ]
