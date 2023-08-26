# Generated by Django 4.2.4 on 2023-08-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pet", "0002_alter_adoptionstory_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="favorites",
            field=models.ManyToManyField(
                blank=True, related_name="favorites", to="pet.userprofile"
            ),
        ),
    ]