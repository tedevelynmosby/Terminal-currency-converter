# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")

# version = re.search(
#     '^__version__\s*=\s*"(.*)"',
#     open('cconvert/cconvert.py').read(),
#     re.M
#     ).group(1)

setup(
    name = "cconvert",
    packages = ["cconvert"],
    entry_points = {
        "console_scripts": ['cconvert = cconvert.cconvert:main']
        },
    version = "1.5",
    description = "Python command line application for currency convertion",
    long_description = long_descr,
    author = "Aravind Balaji",
    author_email = "snaravindbalaji@gmail.com",
    url = "https://github.com/tedevelynmosby/Terminal-currency-converter",
    )
