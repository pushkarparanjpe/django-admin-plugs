#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-admin-plugs',
    version='1.0',
    description='Plugabble apps that extend the django admin.',
    author='Pushkar Paranjpe',
    author_email='pushkar@metamatic.us',
    url='https://github.com/pushkarparanjpe/django-admin-plugs/',
    packages=find_packages(exclude=['DjangoAdminPlugs']),
    include_package_data=True,
)
