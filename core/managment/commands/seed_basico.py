from django.core.management.base import BaseCommand
from core.models import Servicio, Toner

class Command(BaseCommand):
    help = "Carga servicios y toners de ejemplo"

    def handle(self, *args, **kwargs):
        servicios = ["Mesa de Entradas", "Recursos Humanos", "Sistemas", "Mantenimiento"]
        for s in servicios:
            Servicio.objects.get_or_create(nombre=s)

        toners = [
            ("HP", "12A"), ("HP", "85A"), ("Brother", "TN-1060"),
        ]
        for marca, modelo in toners:
            Toner.objects.get_or_create(marca=marca, modelo=modelo, defaults={"stock": 5})
        self.stdout.write(self.style.SUCCESS("Datos cargados"))
