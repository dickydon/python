# -*- mode: python -*-

block_cipher = None


a = Analysis(['general_space_config_xml.py'],
             pathex=['E:\\workspace\\python'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='general_space_config_xml',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
