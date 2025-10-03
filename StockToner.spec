# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main_desktop.py'],
    pathex=[],
    binaries=[('C:\\Users\\bsolohaga\\Desktop\\bere\\GIT\\stockToner\\.venv\\Lib\\site-packages\\webview\\lib\\runtimes\\win-x64\\native\\WebView2Loader.dll', 'webview\\runtimes\\win-x64\\native'), ('C:\\Users\\bsolohaga\\Desktop\\bere\\GIT\\stockToner\\.venv\\Lib\\site-packages\\webview\\lib\\runtimes\\win-arm64\\native\\WebView2Loader.dll', 'webview\\runtimes\\win-arm64\\native'), ('C:\\Users\\bsolohaga\\Desktop\\bere\\GIT\\stockToner\\.venv\\Lib\\site-packages\\webview\\lib\\runtimes\\win-x64\\native\\WebView2Loader.dll', 'webview\\lib\\runtimes\\win-x64\\native'), ('C:\\Users\\bsolohaga\\Desktop\\bere\\GIT\\stockToner\\.venv\\Lib\\site-packages\\webview\\lib\\runtimes\\win-arm64\\native\\WebView2Loader.dll', 'webview\\lib\\runtimes\\win-arm64\\native')],
    datas=[('core', 'core'), ('core\\templates', 'core\\templates'), ('stocktoner', 'stocktoner'), ('staticfiles', 'staticfiles'), ('db.sqlite3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='StockToner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='StockToner',
)
