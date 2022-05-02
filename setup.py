#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2022/5/2'
__author__ = 'sparrow'

import setuptools

setuptools.setup(
    name='snowball',
    version="0.0.1",
    description='SnowBall SDK',
    author='Sparrow',
    long_description="sdk for snowball quant",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['build', 'dist']),
    zip_safe=False,
    python_requires='>=3.6.4',
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)