# core/forms.py
from django import forms
from .models import Movimiento

class RetiroForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ["toner", "servicio", "cantidad", "entregado_a", "observaciones"]
