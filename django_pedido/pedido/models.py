from django.db import models

# Create your models here.


class Conductor(models.Model):
    numero = models.IntegerField(default=None, blank=True, null=True)
    nombre = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    apellido = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    estado = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    nombre = models.CharField(
        max_length=60, default=None, blank=True, null=True)
    apellido = models.CharField(
        max_length=60, default=None, blank=True, null=True)
    correo = models.CharField(
        max_length=80, default=None, blank=True, null=True)
    telefono = models.BigIntegerField(
        default=None, null=True, blank=False, unique=False)
    direccion = models.CharField(
        max_length=80, default=None, blank=True, null=True)
    fecha_entrega = models.DateField(default=None, blank=True, null=True)
    franja_hora = models.PositiveBigIntegerField(
        default=None, blank=True, null=True)
    conductor = models.IntegerField(
        default=None, null=True, blank=False, unique=False)

    def __str__(self):
        return 'Cliente: ' + self.nombre
