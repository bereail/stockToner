#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    # Aseguramos que Python vea el paquete interno 'stocktoner'
    BASE_DIR = Path(__file__).resolve().parent              # ...\stockToner\stocktoner
    PKG_DIR = BASE_DIR / "stocktoner"                       # ...\stockToner\stocktoner\stocktoner
    sys.path.insert(0, str(BASE_DIR))                       # añade dir de manage.py
    sys.path.insert(0, str(PKG_DIR))                        # añade paquete interno explícito

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stocktoner.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
