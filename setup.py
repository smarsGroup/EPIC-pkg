from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="epic_pkg",
    version="0.1.0",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'epic_pkg=epic_pkg.dispatcher:main',
        ],
    },
)