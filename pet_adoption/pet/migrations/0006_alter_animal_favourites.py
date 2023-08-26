# Generated by Django 4.2.4 on 2023-08-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pet", "0005_merge_20230826_1543"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="favourites",
            field=models.ManyToManyField(
                blank=True, default=None, related_name="favorites", to="pet.userprofile"
            ),
        ),
    ]