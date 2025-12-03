from django.contrib import admin

from .models import Country, Region, District, Village, Weather


admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Village)
admin.site.register(Weather)
