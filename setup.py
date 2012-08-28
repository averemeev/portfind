from setuptools import setup, find_packages
import re

version = 1.0

setup(
    name = 'portfind',
    version = version,
    description = 'Find ip with opened specified port',
    author = 'Eremeev A.V',
    author_email = 'eremeev.dev@gmail.com',

    packages = find_packages(),
    include_package_data = True,

    license = "BSD",
    keywords = "nmap ip scan",

    install_requires=[
        'python-nmap',
        'netifaces',
    ],
    entry_points = {
        'console_scripts': [
            'portfind = portfind.portfind:main'
        ]
    }
)
