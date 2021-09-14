from django.db import models
from datetime import datetime
# Create your models here.


class TypeEmployee(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "TipoEmpleado"
        verbose_name_plural = "TiposEmpleado"
        ordering = ["id"]


class Employee(models.Model):
    typeEmployee = models.ForeignKey(
        TypeEmployee, on_delete=models.SET_NULL, null=True)
    names = models.CharField(max_length=150, verbose_name="Nombres")
    dni = models.CharField(max_length=150, verbose_name="Dni")
    date_joined = models.DateTimeField(
        default=datetime.now, verbose_name="Fecha de registro")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0, blank=True)
    salary = models.DecimalField(max_digits=9, default=0.00, decimal_places=2)
    state = models.BooleanField(default=False)
    gender = models.CharField(max_length=502, default='')
    avatar = models.ImageField(
        upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(
        upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = "empleado"
        ordering = ["id"]
