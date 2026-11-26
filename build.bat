@echo off
python -m nuitka --standalone --onefile --enable-plugin=pyside6 --include-data-files=src/main.ui=src/main.ui src/main.py