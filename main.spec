# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Collect matplotlib data files
matplotlib_data = collect_data_files('matplotlib')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=matplotlib_data,
    hiddenimports=['numpy', 'matplotlib'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ColorSpaceVisualizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# For macOS, create a .app bundle
if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='ColorSpaceVisualizer.app',
        icon=None,
        bundle_identifier=None,
    )