from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from apps.weather.models import Village, Weather


class CustomUser(AbstractUser):
    # user_permissions = None
    # groups = None
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(unique=True)

    village = models.ForeignKey(
        to=Village,
        on_delete=models.SET_NULL,
        related_name='users',
        null=True,
        blank=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-date_joined']

    def __str__(self) -> str:
        return f"{self.email}"

    ### Propertylar

    @property
    def get_village(self):
        return self.village if self.village else None

    @property
    def get_district(self):
        if self.village:
            return self.village.district
        return None

    @property
    def get_region(self):
        if self.village:
            return self.village.district.region
        return None

    @property
    def get_country(self):
        if self.village:
            return self.village.district.region.country
        return None

    @property
    def get_full_location(self):
        if not self.village:
            return None

        data = {
            "country": self.get_country.name,
            "region": self.get_region.name,
            "district": self.get_district.name,
            "village": self.get_village.name,
        }

        return data

    @property
    def get_weather(self):
        if not self.village:
            return None
        if not Weather.objects.filter(village=self.village).exists():
            return None
        return self.village.weathers.order_by('-updated_at').first()

    @property
    def get_profile(self):
        data = {"email": self.email}

        return data
    
    @property
    def get_id(self) -> int:
        return self.id or None
    
    @property
    def get_pk(self) -> int:
        return self.pk or None
