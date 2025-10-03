from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.stock_view, name="home"),
    path("retiro/", views.retiro_view, name="retiro"),
]
