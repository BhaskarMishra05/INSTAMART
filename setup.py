import os
import sys
from setuptools import setup, find_packages
from typing import List

setup(
    name='InstaMart-DataAnalysis',
    version='0.0.0',
    author='Bhaskar Mishra',
    author_email='bhaskarmishra1590@gmail.com',
    description='A data processing and analysis package',
    packages=find_packages(),
    python_requires='>=3.8',
)