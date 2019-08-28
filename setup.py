from cx_Freeze import setup, Executable

setup(
    name="qr_detection",
    version="0.1",
    description="Qr detection",
    executables=[Executable("view.py")],
)
