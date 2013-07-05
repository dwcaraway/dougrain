#!/usr/bin/env python
# Copyright (c) 2013 Will Harris
# See the file license.txt for copying permission.

from setuptools import setup

VERSION = "0.5"

base_url = "http://github.com/wharris/dougrain/"

setup(
    name='dougrain',
    version=VERSION,
    description='HAL JSON parser and generator',
    author='Will Harris',
    author_email='will@greatlibrary.net',
    url=base_url,
    packages=['dougrain'],
    provides=['dougrain'],
    long_description=open("README.rst").read(),
    install_requires=['uritemplate'],
    dependency_links=["https://github.com/uri-templates/uritemplate-py/"
                      "archive/d11b6f74a27804fb7d0de45d26bdbd007925913a.zip"
                      "#egg=uritemplate"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
