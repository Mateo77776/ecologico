from django.db import models
from django.contrib.auth.models import User

class Reciclaje(models.Model):
    MATERIALES = [
        ('Plástico', 'Plástico'),
        ('Papel', 'Papel y Cartón'),
        ('Vidrio', 'Vidrio'),
        ('Metal', 'Metal'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    tipo_material = models.CharField(max_length=50, choices=MATERIALES, verbose_name="Tipo de material")
    peso_kg = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Peso (kg)")
    punto_acopio = models.CharField(max_length=150, verbose_name="Punto de acopio")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha")

class Plantacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Responsable")
    especie_arbol = models.CharField(max_length=100, verbose_name="Especie de árbol")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    ubicacion = models.CharField(max_length=200, verbose_name="Ubicación")
    fecha_plantacion = models.DateField(verbose_name="Fecha de plantación")