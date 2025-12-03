from django.contrib import admin

from .models import CustomUser


admin.site.site_header = "Weather Admin Paneli"
admin.site.site_title = "Weather Admin Paneli"
admin.site.index_title = "Weather Admin Paneliga xush kelibsiz!"
admin.site.empty_value_display = "Mavjud emas!"


admin.site.register(CustomUser)
