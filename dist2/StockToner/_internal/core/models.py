from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Servicio(models.Model):
    nombre = models.CharField(max_length=120, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Toner(models.Model):
    marca = models.CharField(max_length=60, blank=True)       # p.ej. HP
    modelo = models.CharField(max_length=80)                  # p.ej. 12A / Q2612A
    codigo = models.CharField(max_length=50, blank=True)      # opcional (interno)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [("marca", "modelo")]
        ordering = ["marca", "modelo"]

    def __str__(self):
        base = f"{self.marca} {self.modelo}".strip()
        return f"{base} (stock: {self.stock})"


class Movimiento(models.Model):
    TIPO = (
        ("INGRESO", "Ingreso a depósito"),
        ("EGRESO", "Egreso/Retiro para servicio"),
    )
    toner = models.ForeignKey(Toner, on_delete=models.PROTECT, related_name="movimientos")
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT, related_name="movimientos",
                                 blank=True, null=True)  # null cuando es INGRESO
    tipo = models.CharField(max_length=10, choices=TIPO)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    entregado_a = models.CharField(max_length=120, blank=True)  # quién lo retiró (opcional)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha"]

    def clean(self):
        # Regla: para EGRESO debe indicar servicio
        if self.tipo == "EGRESO" and not self.servicio:
            raise ValidationError("En un EGRESO debe seleccionar un servicio.")
        # Regla: la cantidad debe ser > 0 (PositiveInteger ya cubre, pero por las dudas)
        if self.cantidad <= 0:
            raise ValidationError("La cantidad debe ser mayor que cero.")

        # Validar stock disponible en EGRESO
        if self.pk is None and self.tipo == "EGRESO":
            if self.toner.stock < self.cantidad:
                raise ValidationError(f"No hay stock suficiente de {self.toner}. (Disponible: {self.toner.stock})")

    def apply_to_stock(self):
        """Aplica el movimiento al stock del toner."""
        if self.tipo == "INGRESO":
            self.toner.stock += self.cantidad
        else:  # EGRESO
            if self.toner.stock < self.cantidad:
                raise ValidationError("Stock insuficiente.")
            self.toner.stock -= self.cantidad
        self.toner.save(update_fields=["stock"])

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        self.full_clean()
        super().save(*args, **kwargs)
        # Sólo aplicar cambio de stock al crear (para evitar duplicar en ediciones)
        if is_new:
            self.apply_to_stock()

    def __str__(self):
        s = self.servicio.nombre if self.servicio else "-"
        return f"[{self.tipo}] {self.cantidad} x {self.toner} -> {s} {self.fecha:%Y-%m-%d %H:%M}"
