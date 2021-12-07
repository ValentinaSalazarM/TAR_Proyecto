import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win64GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "HidrApp",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "Universidad de los Andes",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
