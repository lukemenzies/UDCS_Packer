# -*- mode: python -*-


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

block_cipher = None
a = Analysis(['UPack4DS.py'],
             pathex=['C:\\Users\\limen\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\rdflib', 'C:\\Users\\limen\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\rdflib\\plugins', 'C:\\Users\\limen\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\rdflib\\tools', 'C:\\Users\\limen\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\rdflib\\extras', 'C:\\Users\\limen\\Desktop\\UPack4DS'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas + [("UPackInstructions.txt", resource_path("UPackInstructions.txt"), "DATA"), ("UPackLogo300.jpg", resource_path("UPackLogo300.jpg"), "DATA")],
          [],
          name='UPack4DS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          icon=resource_path("UPack.ico"),
          console=False)
