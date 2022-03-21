from setuptools import setup

setup(
    name="lutris_wrapper",
    description="Lutris wrapper for Lutris Flatpak",
    py_modules=["lutris_wrapper"],
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "lutris-wrapper = lutris_wrapper:main",
        ]
    }
)
