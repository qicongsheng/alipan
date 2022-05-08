#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from setuptools import setup, find_packages

setup(
    name = 'alipan',
    version = '1.2.9',
    keywords='alipan',
    description = 'Commandline tools for aliyundrive',
    license = 'MIT License',
    url = 'https://github.com/qicongsheng/alipan',
    author = 'qicongsheng',
    author_email = 'qicongsheng@outlook.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'aligo>=3.5.1'
    ],
    entry_points = {
        'console_scripts': [
            'alipan = alipan.__main__:main'
        ]
    }
)