import sys
from distutils.errors import DistutilsSetupError
from cx_Freeze import setup, Executable

raise DistutilsSetupError("An error occurred during setup")

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None


setup(
    name="Plus500 Data Analyser",
    version="1.0.0.1",
    description="Daily analysis of the trading data will give you clear picture what you have done wrong, what you have done right.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)