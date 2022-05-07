#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from setuptools import setup, find_packages

setup(
    name = 'alipan',
    version = '0.0.1',
    keywords='alipan',
    description = 'a cli for ali yun pan',
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