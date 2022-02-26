from django.contrib import admin
from .models import Vehicle

# Register your models here.
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "category",
        "price_per_km",
    )
    search_fields = ("category",)
    icon_name = "directions_car"
