from django.contrib import admin # admin.ModelAdmin uchun
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.site_header = "Weather Admin Paneli"
admin.site.site_title = "Weather Admin Paneli"
admin.site.index_title = "Weather Admin Paneliga xush kelibsiz!"
admin.site.empty_value_display = "Mavjud emas!"


# admin.site.unregister(Group) # Extimol

admin.site.register(CustomUser)
