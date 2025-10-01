from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from .models import Toner, Movimiento
from .forms import RetiroForm

def stock_view(request):
    toners = Toner.objects.all().order_by("marca", "modelo")
    return render(request, "core/stock.html", {"toners": toners})

@transaction.atomic
def retiro_view(request):
    if request.method == "POST":
        form = RetiroForm(request.POST)
        if form.is_valid():
            mov: Movimiento = form.save(commit=False)
            mov.tipo = "EGRESO"
            try:
                mov.save()
                messages.success(request, "Retiro registrado correctamente.")
                return redirect("home")
            except Exception as e:
                messages.error(request, f"Error: {e}")
    else:
        form = RetiroForm()
    return render(request, "core/retiro.html", {"form": form})
