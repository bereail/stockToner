from django.contrib import admin
from .models import Toner, Servicio, Movimiento

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_display = ["nombre"]

@admin.register(Toner)
class TonerAdmin(admin.ModelAdmin):
    list_display = ["marca", "modelo", "stock"]
    list_filter = ["marca"]
    search_fields = ["marca", "modelo", "codigo"]

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ["fecha", "tipo", "toner", "cantidad", "servicio", "entregado_a"]
    list_filter = ["tipo", "servicio", "toner", "fecha"]
    search_fields = ["entregado_a", "observaciones"]
    autocomplete_fields = ["toner", "servicio"]
