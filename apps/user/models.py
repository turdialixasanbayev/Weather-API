from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager
from apps.weather.models import Village


class CustomUser(AbstractUser):
    """
    CustomUser modeli foydalanuvchi ma'lumotlarini saqlash uchun ishlatiladi.
    Email manzili asosida autentifikatsiya qilishni qo'llab-quvvatlaydi.
    """

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
        if not self.village:
            return None

        data = {'village': self.village.name}
        return data

    @property
    def get_district(self):
        if not self.village:
            return None

        data = {'district': self.village.district.name}
        return data

    @property
    def get_region(self):
        if not self.village:
            return None
        
        data = {'region': self.village.district.region.name}
        return data

    @property
    def get_country(self):
        if not self.village:
            return None

        data = {'country': self.village.district.region.country.name}
        return data

    @property
    def get_full_location(self):
        if not self.village:
            return None

        data = {
            "country": self.get_country['country'],
            "region": self.get_region['region'],
            "district": self.get_district['district'],
            "village": self.get_village['village'],
        }

        return data

    @property
    def get_weather(self):
        if not self.village:
            return None

        weather = self.village.weathers.order_by('-updated_at').first()

        if not weather:
            return None
        
        data = {
            "village": self.village.name,
            "temperature": weather.temperature,
            "feels_like": weather.feels_like,
            "wind_speed": weather.wind_speed,
            "wind_deg": weather.wind_deg,
            "visibility": weather.visibility,
            "condition": weather.condition,
            "description": weather.description,
            "sunrise": weather.sunrise,
            "sunset": weather.sunset,
            "humidity": weather.humidity,
            "pressure": weather.pressure,
            "updated_at": weather.updated_at,
        }

        return data

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


### MonitoringLog modeli


class MonitoringLog(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    status = models.IntegerField()

    duration_ms = models.FloatField()
    sql_count = models.IntegerField()
    sql_data = models.JSONField()

    ip = models.GenericIPAddressField(null=True)
    user_agent = models.TextField(null=True)
    user_id = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return f"{self.method} {self.path} - {self.status} ({self.created_at})"

    class Meta:
        verbose_name = "Monitoring Log"
        verbose_name_plural = "Monitoring Logs"
        ordering = ["-created_at"]
