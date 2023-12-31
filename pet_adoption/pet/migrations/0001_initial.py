# Generated by Django 4.2.4 on 2023-08-27 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Adoption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("application_text", models.TextField(max_length=500)),
                ("application_date", models.DateTimeField(auto_now_add=True)),
                (
                    "application_status",
                    models.CharField(
                        choices=[
                            ("", "Select Status"),
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Denied", "Denied"),
                        ],
                        default="",
                        max_length=32,
                    ),
                ),
                ("reason_for_adoption", models.TextField(default="")),
                ("time_spending_habbit", models.TextField(default="")),
                ("pet_fate", models.TextField(default="")),
                ("street", models.CharField(default="", max_length=64)),
                (
                    "living_space",
                    models.CharField(
                        choices=[
                            ("", "Select Type"),
                            ("House", "House"),
                            ("Apartment", "Apartment"),
                        ],
                        default="",
                        max_length=32,
                    ),
                ),
                ("square_meters", models.CharField(default="", max_length=9)),
                (
                    "initial_pet",
                    models.CharField(
                        choices=[("", "Select Choice"), ("Yes", "Yes"), ("No", "No")],
                        default="",
                        max_length=32,
                    ),
                ),
                ("is_approved", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "Adoptions",
            },
        ),
        migrations.CreateModel(
            name="Animal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
                ("color", models.CharField(max_length=64)),
                (
                    "species",
                    models.CharField(
                        choices=[
                            ("", "Select Species"),
                            ("Dog", "Dog"),
                            ("Cat", "Cat"),
                            ("Other", "Other"),
                        ],
                        default="",
                        max_length=9,
                    ),
                ),
                ("breed", models.CharField(max_length=32)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("", "Select Gender"),
                            ("Male", "Male"),
                            ("Female", "Female"),
                        ],
                        default="",
                        max_length=9,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("", "Select Size"),
                            ("Small", "Small (0-10kg)"),
                            ("Medium", "Medium (11-30kg)"),
                            ("Large", "Large (31-50kg)"),
                            ("Exter Large", "Extra Large (51kg or more)"),
                        ],
                        default="",
                        max_length=32,
                    ),
                ),
                ("age", models.IntegerField()),
                ("chip", models.CharField(max_length=64, unique=True)),
                ("about_pet", models.TextField(max_length=500)),
                ("image", models.ImageField(upload_to="animal_pics/")),
                ("is_available_for_adoption", models.BooleanField(default=True)),
                (
                    "favourites",
                    models.ManyToManyField(
                        blank=True,
                        default=None,
                        related_name="favorites",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Animals",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("city_key", models.CharField(default="XXX", max_length=3)),
                ("city_name", models.CharField(default="XXXXXX", max_length=32)),
            ],
            options={
                "verbose_name_plural": "Locations",
            },
        ),
        migrations.CreateModel(
            name="Treatment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "treatment_name",
                    models.CharField(
                        choices=[
                            ("", "Select Treatment"),
                            ("Vaccination", "Vaccination"),
                            ("Deworming", "Deworming"),
                            ("Flea and Tick Prevention", "Flea and Tick Prevention"),
                            ("Dental Care", "Dental Care"),
                            ("Annual Wellness Check-up", "Annual Wellness Check-up"),
                        ],
                        default="",
                        max_length=64,
                    ),
                ),
                ("next_date", models.DateField()),
                ("description", models.TextField(max_length=500)),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pet.animal"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Treatments",
            },
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "service_name",
                    models.CharField(
                        choices=[
                            ("", "Select Service"),
                            ("Luxury Spa Day", "Luxury Spa Day"),
                            ("Canine Massage Therapy", "Canine Massage Therapy"),
                            (
                                "Personalized Training Packages",
                                "Personalized Training Packages",
                            ),
                            (
                                "Pet Photography and Portraits",
                                "Pet Photography and Portraits",
                            ),
                            ("Pet Parties and Events", "Pet Parties and Events"),
                            ("VIP Boarding Suites", "VIP Boarding Suites"),
                            ("Pet Concierge Services", "Pet Concierge Services"),
                        ],
                        default="",
                        max_length=64,
                    ),
                ),
                ("description", models.TextField(max_length=500)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "animal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pet.animal"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Services",
            },
        ),
        migrations.AddField(
            model_name="animal",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pet.location"
            ),
        ),
        migrations.CreateModel(
            name="AdoptionStory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("story_title", models.CharField(max_length=128)),
                ("story_description", models.TextField(max_length=500)),
                (
                    "adoption",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="pet.adoption"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Adoption Stories",
            },
        ),
        migrations.AddField(
            model_name="adoption",
            name="animal",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pet.animal"
            ),
        ),
        migrations.AddField(
            model_name="adoption",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pet.location"
            ),
        ),
        migrations.AddField(
            model_name="adoption",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
