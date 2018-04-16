#encoding: utf-8
import os
import re
from setuptools import setup, find_packages

# parse version from webcrawler/__init__.py
with open(os.path.join(os.path.dirname(__file__), 'mscraper', '__init__.py')) as f:
    version = re.compile(r"__version__\s+=\s+'(.*)'", re.I).match(f.read()).group(1)

with open('README.md') as f:
    long_description = f.read()

setup(
    name='magento-py-scraper',
    version=version,
    description='A simple magento scraper.',
    long_description=long_description,
    author='Hector Herranz',
    author_email='hectorherranz91@gmail.com',
    url='https://github.com/hectorherranz91/magento-py-scraper.git',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    package_data={
        'webcrawler': ['default_config.yml'],
    },
    keywords='diff compare',
    install_requires=[
        'termcolor',
        'PyYAML',
        'future',
        'lxml',
        'requests',
        'jenkins-mail-py',
        'bs4',
        'robotparser',
        'urlparse'
    ],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'mscraper=mscraper:main'
        ]
    }
)
