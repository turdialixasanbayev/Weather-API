from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=225, unique=True)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.code}"
    
    @property
    def get_id(self) -> int:
        return self.id or None
    
    @property
    def get_pk(self) -> int:
        return self.pk or None


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='regions')
    name = models.CharField(max_length=225, unique=True)

    class Meta:
        unique_together = ('country', 'name')

    def __str__(self) -> str:
        return f"{self.name} ({self.country.name})"
    
    @property
    def get_id(self) -> int:
        return self.id or None
    
    @property
    def get_pk(self) -> int:
        return self.pk or None


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=225, unique=True)

    class Meta:
        unique_together = ('region', 'name')

    def __str__(self) -> str:
        return f"{self.name}, {self.region.name}"
    
    @property
    def get_id(self) -> int:
        return self.id or None
    
    @property
    def get_pk(self) -> int:
        return self.pk or None


class Village(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='villages')
    name = models.CharField(max_length=225, unique=True)

    class Meta:
        unique_together = ('district', 'name')

    def __str__(self) -> str:
        return f"{self.name}, {self.district.name}"
    
    @property
    def get_id(self) -> int:
        return self.id or None
    
    @property
    def get_pk(self) -> int:
        return self.pk or None


class Weather(models.Model):
    village = models.ForeignKey(
        Village,
        on_delete=models.CASCADE,
        related_name='weathers'
    )

    # Asosiy ko‘rsatkichlar
    temperature = models.FloatField()            # Harorat (°C)
    feels_like = models.FloatField()             # Seziladigan harorat (°C)

    humidity = models.PositiveSmallIntegerField()  # Namlik (%)
    pressure = models.PositiveIntegerField()        # Bosim (hPa)

    wind_speed = models.FloatField()             # Shamol tezligi (m/s)
    wind_deg = models.PositiveSmallIntegerField()  # Shamol yo‘nalishi (0–360°)

    visibility = models.PositiveIntegerField()      # Ko‘rinish masofasi (m)

    # Ob-havo holati
    condition = models.CharField(max_length=50)     # "Clear", "Cloudy", "Rainy"
    description = models.CharField(max_length=255)  # "clear sky", "light rain"

    # Quyosh chiqish va botish
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()

    # Yangilanish vaqti
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.village.name} - {self.temperature}°C"

    @property
    def get_id(self) -> int:
        return self.id or None

    @property
    def get_pk(self) -> int:
        return self.pk or None
