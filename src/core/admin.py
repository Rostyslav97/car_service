from django.contrib import admin
from core.models import City, Defect


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Defect)
class DefectAdmin(admin.ModelAdmin):
    list_display = ("description", "adress", "customer")