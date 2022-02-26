from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_price_per_km_is_greater_or_equal_zero(price_per_km):
    if price_per_km <= 0:
        raise ValidationError("Quilometragem não pode ser menor ou igual a 0!")


class Vehicle(models.Model):
    category = models.CharField(max_length=50, unique=True, verbose_name="Categoria")
    price_per_km = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[validate_price_per_km_is_greater_or_equal_zero],
        verbose_name="Preço por km",
    )

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
