@echo off

title /output
echo building...

pyinstaller --onefile --windowed --uac-admin --optimize=2 --i="NONE" --add-data "assets/fonts/arial.ttf;fonts" --add-data "assets/fonts/icons.ttf;fonts" --add-data "assets/fonts/weapon.ttf;fonts" --add-data "assets/textures/colorpicker.png;textures" src/main.py > nul 2>&1

timeout /t 1 > nul

if exist build rd /s /q build
if exist main.spec del main.spec
if exist dist ren dist output
