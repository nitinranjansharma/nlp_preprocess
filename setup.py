# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name='nlp_preprocess',
    version='0.0.1',
    description='Industrial Adventure in NLP',
    author='Nitin Ranjan Sharma',
    author_email='nitinranjansharma@gmail.com',
    url='https://github.com/nitinranjansharma/nlp_preprocess',
    #packages=find_packages(exclude=('nlp_preprocess', 'utility', 'docs'))
    py_modules=["case_unify", "htmlstrip", "remove_extra_space",
                "remove_special_chars", "stopwords_removal"],
    package_dir={'': 'nlp_preprocess'}
)
