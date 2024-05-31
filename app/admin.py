from django.contrib import admin
from .models import HydroponicSystem, Measurement


@admin.register(HydroponicSystem)
class HydroponicSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner', 'created_at', 'updated_at')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('hydroponic_system', 'ph', 'water_temp', 'tds', 'created_at')
