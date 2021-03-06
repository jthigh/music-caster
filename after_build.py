import zipfile

with zipfile.ZipFile('dist/Portable.zip', 'w') as zf:
    zf.write('dist/Music Caster.exe', 'Music Caster.exe')
    zf.write('dist/Updater.exe', 'Updater.exe')
    zf.write('resources/default.png', 'images/default.png')
    zf.write('CHANGELOG.txt')

print('Created dist/Portable.zip')

with zipfile.ZipFile('dist/Python Files.zip', 'w') as zf:
    zf.write('music_caster.py', 'music_caster.pyw')
    zf.write('updater.py', 'updater.pyw')
    zf.write('resources/Music Caster.ico', 'icon.ico')
    zf.write('resources/default.png', 'images/default.png')
    zf.write('requirements.txt')
    zf.write('CHANGELOG.txt')

print('Created dist/Python Files.zip')