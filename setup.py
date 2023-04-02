from cx_Freeze import setup, Executable

setup(
    name="Plus500 Data Analyser",
    version="1.0.0.X",
    description="Daily analysis of the trading data will give you clear picture what you have done wrong, what you have done right.",
    executables=[Executable("main.py")],
)