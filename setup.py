# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='USR CSV helper tool',
    version='0.1.0',
    description='A helper tool for creating USR CSV format for Indian languages',
    long_description=readme,
    author='Arghya Bhattacharya',
    author_email='arghya.b@research.iiit.ac.in',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

