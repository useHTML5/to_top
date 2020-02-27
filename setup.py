# coding: utf-8
from setuptools import setup, find_packages

setup(
    name="to_top",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-libsass',
    ],
)
