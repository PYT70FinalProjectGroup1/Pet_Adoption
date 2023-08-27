from django.db import models
from django.contrib.auth import get_user_model


class BaseModel(models.Model):
    """
    A base model that includes common fields for tracking creation and modification timestamps.

    Fields:
        created_at (DateTimeField): The timestamp when the instance was created.
        updated_at (DateTimeField): The timestamp when the instance was last updated.

    Meta:
        abstract = True: Specifies that this is an abstract base class and won't create a separate database table.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Location(BaseModel):
    """
    Represents a location with a city key and city name.

    Fields:
        city_key (CharField): The city key for the location.
        city_name (CharField): The name of the city.

    Meta:
        verbose_name_plural = "Locations": Specifies the plural name for this model.

    Methods:
        __str__(): Returns a string representation of the location using its city name.
    """

    city_key = models.CharField(max_length=3, default="XXX",null=False)
    city_name = models.CharField(max_length=32, default="XXXXXX",null=False)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.city_name}"


class Animal(BaseModel):
    """
    Represents an animal available for adoption.

    Fields:
        name (CharField): The name of the animal.
        color (CharField): The color of the animal.
        species (CharField): The species of the animal.
        breed (CharField): The breed of the animal.
        gender (CharField): The gender of the animal.
        size (CharField): The size category of the animal.
        age (IntegerField): The age of the animal.
        chip (CharField): A unique identifier for the animal.
        location (ForeignKey): A foreign key to the Location model representing the animal's location.
        about_pet (TextField): A description of the animal.
        image (ImageField): An image of the animal.
        favourites (ManyToManyField): A many-to-many relationship to UserProfiles representing favorite users.
        is_available_for_adoption (BooleanField): Indicates if the animal is available for adoption.

    Meta:
        verbose_name_plural = "Animals": Specifies the plural name for this model.

    Methods:
        __str__(): Returns a string representation of the animal using its name.
    """

    SPECIES_CHOICE = [
        ("", "Select Species"),
        ("Dog", "Dog"),
        ("Cat", "Cat"),
        ("Other", "Other"),
    ]

    SIZE_CHOICE = [
        ("", "Select Size"),
        ("Small", "Small (0-10kg)"),
        ("Medium", "Medium (11-30kg)"),
        ("Large", "Large (31-50kg)"),
        ("Exter Large", "Extra Large (51kg or more)"),
    ]

    GENDER_CHOICE = [
        ("", "Select Gender"),
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    name = models.CharField(max_length=32, null=False)
    color = models.CharField(max_length=64, null=False)
    species = models.CharField(
        max_length=9, blank=False, choices=SPECIES_CHOICE, default=""
    )
    breed = models.CharField(max_length=32, null=False)
    gender = models.CharField(
        max_length=9, null=False, blank=False, choices=GENDER_CHOICE, default=""
    )
    size = models.CharField(max_length=32, blank=False, choices=SIZE_CHOICE, default="")
    age = models.IntegerField(null=False)
    chip = models.CharField(max_length=64, unique=True, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    about_pet = models.TextField(max_length=500, null=False)
    image = models.ImageField(upload_to="animal_pics/")
    favourites = models.ManyToManyField(
        "accounts.CustomUser", related_name="favorites", blank=True, default=None
    )
    is_available_for_adoption = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name


class Adoption(BaseModel):
    """
    Represents an adoption application.

    Fields:
        user (ForeignKey): A foreign key to the User model representing the applicant.
        animal (ForeignKey): A foreign key to the Animal model representing the adopted animal.
        application_text (TextField): A text field for the application description.
        application_date (DateTimeField): The timestamp when the application was submitted.
        application_status (CharField): The status of the application.
        reason_for_adoption (TextField): The reason for wanting to adopt the animal.
        time_spending_habbit (TextField): The applicant's time spending habits with the pet.
        pet_fate (TextField): The applicant's plans for the adopted pet's future.
        street (CharField): The street address of the applicant.
        city (ForeignKey): A foreign key to the Location model representing the city.
        living_space (CharField): The type of living space of the applicant.
        square_meters (CharField): The square meters of the living space.
        initial_pet (CharField): Whether the applicant has had a pet before.
        is_approved (BooleanField): Indicates if the application is approved.

    Meta:
        verbose_name_plural = "Adoptions": Specifies the plural name for this model.

    Methods:
        __str__(): Returns a string representation of the adoption using its ID and approval status.
    """

    RESIDENCE_TYPE_CHOICE = [
        ("", "Select Type"),
        ("House", "House"),
        ("Apartment", "Apartment"),
    ]

    FIRST_PET_CHOICES = [("", "Select Choice"), ("Yes", "Yes"), ("No", "No")]

    STATUS_CHOICE = [
        ("", "Select Status"),
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Denied", "Denied"),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    application_text = models.TextField(max_length=500, null=False)
    application_date = models.DateTimeField(auto_now_add=True)
    application_status = models.CharField(
        max_length=32, choices=STATUS_CHOICE, blank=False, null=False, default=""
    )
    reason_for_adoption = models.TextField(null=False, default="")
    time_spending_habbit = models.TextField(null=False, default="")
    pet_fate = models.TextField(null=False, default="")
    street = models.CharField(max_length=64, null=False, default="")
    city = models.ForeignKey(Location, on_delete=models.CASCADE)
    living_space = models.CharField(
        max_length=32,
        choices=RESIDENCE_TYPE_CHOICE,
        null=False,
        blank=False,
        default="",
    )
    square_meters = models.CharField(max_length=9, null=False, default="")
    initial_pet = models.CharField(
        max_length=32, choices=FIRST_PET_CHOICES, null=False, blank=False, default=""
    )
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Adoptions"

    def __str__(self):
        return f" {self.id} - {self.is_approved}"


class Treatment(BaseModel):
    """
    Represents a medical treatment record for an animal.

    Fields:
        animal (ForeignKey): A foreign key to the Animal model representing the treated animal.
        treatment_name (CharField): The name of the treatment.
        next_date (DateField): The next scheduled date for the treatment.
        description (TextField): A description of the treatment.

    Meta:
        verbose_name_plural = "Treatments": Specifies the plural name for this model.

    Methods:
        __str__(): Returns a string representation of the treatment using the animal's name and treatment name.
    """

    TREATMENTS_CHOICE = [
        ("", "Select Treatment"),
        ("Vaccination", "Vaccination"),
        ("Deworming", "Deworming"),
        ("Flea and Tick Prevention", "Flea and Tick Prevention"),
        ("Dental Care", "Dental Care"),
        ("Annual Wellness Check-up", "Annual Wellness Check-up"),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    treatment_name = models.CharField(
        choices=TREATMENTS_CHOICE, max_length=64, null=False, blank=False, default=""
    )
    next_date = models.DateField(null=False)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Treatments"

    def __str__(self):
        return f"{self.animal.name}_{self.treatment_name}"


class Service(BaseModel):
    """
    Represents a service offered for animals.

    Fields:
        animal (ForeignKey): A foreign key to the Animal model representing the subject of the service.
        date (DateField): The date the service was provided.
        service_name (CharField): The name of the service.
        description (TextField): A description of the service.
        price (DecimalField): The price of the service.

    Meta:
        verbose_name_plural = "Services": Specifies the plural name for this model.

    Methods:
        __str__(): Returns a string representation of the service using the animal's name and service name.
    """

    SERVICES_CHOICE = [
        ("", "Select Service"),
        ("Luxury Spa Day", "Luxury Spa Day"),
        ("Canine Massage Therapy", "Canine Massage Therapy"),
        ("Personalized Training Packages", "Personalized Training Packages"),
        ("Pet Photography and Portraits", "Pet Photography and Portraits"),
        ("Pet Parties and Events", "Pet Parties and Events"),
        ("VIP Boarding Suites", "VIP Boarding Suites"),
        ("Pet Concierge Services", "Pet Concierge Services"),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    service_name = models.CharField(
        choices=SERVICES_CHOICE, max_length=64, null=False, blank=False, default=""
    )
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.animal.name}_{self.service_name}"


class AdoptionStory(BaseModel):
    """
    Represents a story related to an adoption.

    Fields:
        adoption (OneToOneField): A one-to-one relationship to the Adoption model.
        story_title (CharField): The title of the adoption story.
        story_description (TextField): A description of the adoption story.

    Meta:
        verbose_name_plural = "Adoption Stories": Specifies the plural name for this model.

    Methods:
        __str__(): Returns a string representation of the story using its title.
    """

    adoption = models.OneToOneField(Adoption, on_delete=models.CASCADE)
    story_title = models.CharField(max_length=128, null=False)
    story_description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Adoption Stories"

        def __str__(self):
            return f"{self.story_title}"
