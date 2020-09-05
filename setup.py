# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nlp_preprocess',
    version='0.1.0',
    description='Industrial Adventure in NLP',
    long_description=readme,
    author='Nitin Ranjan Sharma',
    author_email='nitinranjansharma@gmail.com',
    url='https://github.com/nitinranjansharma/nlp_preprocess',
    license=license,
    packages=find_packages(exclude=('nlp_preprocess', 'utility', 'docs'))
)
