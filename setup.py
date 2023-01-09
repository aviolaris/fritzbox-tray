"""
FritzBox Tray - A system tray application for interacting with FRITZ!Box devices.
Copyright (C) 2023 Andreas Violaris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
import os
from setuptools import setup, find_namespace_packages

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='fritzbox-tray',
    version='1.0.55',
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "fritzbox_tray": ["*.py"],
        "fritzbox_tray.resources": ["*.ico"],
    },
    description='A system tray application for interacting with FRITZ!Box devices.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['fritz', 'fritzbox', 'fritzbox-tray', 'fritzbox_tray', 'tray'],
    author='Andreas Violaris',
    url='https://github.com/aviolaris/fritzbox-tray',
    install_requires=requirements,
    entry_points={
        'gui_scripts': [
            'fritzbox-tray=fritzbox_tray.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
