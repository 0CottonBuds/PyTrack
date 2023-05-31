# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['plyer.platforms.win.notification'],
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
    [],
    exclude_binaries=True,
    name='PyTrack',
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
    icon=['Icons\icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyTrack 1.0.1 debug',
)

import shutil
shutil.copyfile('config.ini', str(coll.name) +'/Config.ini'.format(DISTPATH))
shutil.copyfile('pyTrack.db', str(coll.name) + '/pyTrack.db'.format(DISTPATH))
shutil.copytree('Icons', str(coll.name) +'/Icons'.format(DISTPATH))
shutil.copytree('PytrackUtils', str(coll.name) +'/PytrackUtils'.format(DISTPATH))
shutil.copytree('Themes', str(coll.name) +'/Themes'.format(DISTPATH))
shutil.copytree('UI', str(coll.name) +'/UI'.format(DISTPATH))

