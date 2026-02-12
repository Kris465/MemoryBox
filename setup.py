"""
Setup file for Sound Terminal
"""

from setuptools import setup, find_packages

setup(
    name="sound_term",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "sounddevice",
        "pyaudio",  # Alternative audio library
    ],
    entry_points={
        "console_scripts": [
            "sound-term=sound_term.main:main",
        ],
    },
    author="Nata",
    description="Audio interface for developers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)