# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='nlp_preprocess',
    version='0.1.0',
    description='Industrial Adventure in NLP',
    author='Nitin Ranjan Sharma',
    author_email='nitinranjansharma@gmail.com',
    url='https://github.com/nitinranjansharma/nlp_preprocess',
    #packages=find_packages(exclude=('nlp_preprocess', 'utility', 'docs'))
    package_dir={'': 'nlp_preprocess'}
)
