# main_desktop.py
import os
import sys
import time
import threading
import urllib.request
import importlib
import webview

# --- Config ---
HOST = "127.0.0.1"
PORT = 8001
URL  = f"http://{HOST}:{PORT}"

# Asegurar cwd estable (especialmente cuando está empaquetado con PyInstaller)
def set_stable_cwd():
    base = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
    os.chdir(base)

def pick_settings():
    """
    Si tenés dos proyectos (core y stocktoner), autodetecta el primero que exista.
    """
    candidates = ["core.settings", "stocktoner.settings"]
    for mod in candidates:
        try:
            importlib.import_module(mod)
            return mod
        except ModuleNotFoundError:
            pass
    raise RuntimeError("No encontré settings. Asegurate de tener 'core.settings' o 'stocktoner.settings'.")

def start_wsgi_server():
    """
    Levanta Django bajo waitress (WSGI) en un hilo en segundo plano.
    """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", pick_settings())

    import django
    from waitress import serve
    from django.core.wsgi import get_wsgi_application

    django.setup()
    application = get_wsgi_application()
    # Servir en http://127.0.0.1:8001
    serve(application, host=HOST, port=PORT, threads=4)

def wait_for_server(timeout=20.0):
    """
    Espera a que el server responda antes de abrir la ventana.
    """
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(URL, timeout=1):
                return True
        except Exception:
            time.sleep(0.3)
    return False

if __name__ == "__main__":
    # Compatibilidad PyInstaller en Windows
    try:
        import multiprocessing as mp
        mp.freeze_support()
    except Exception:
        pass

    set_stable_cwd()

    # Iniciar servidor en segundo plano
    t = threading.Thread(target=start_wsgi_server, daemon=True)
    t.start()
    wait_for_server()

    webview.create_window("StockToner", URL, width=1200, height=800)
    webview.start(gui="mshtml")



    # Preferir Edge (WebView2). Si no está, caer a mshtml como backup.
    try:
        webview.start(gui="edgechromium")   # requiere Microsoft Edge WebView2 Runtime (x64)
    except Exception:
        webview.start(gui="mshtml")
