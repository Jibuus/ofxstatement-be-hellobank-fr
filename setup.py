#!/usr/bin/python3
"""Setup for ofxstatement-be-hellobank-fr plugin"""
from setuptools import find_packages
from distutils.core import setup

version = "0.0.1"

with open('README.rst') as f:
    long_description = f.read()

setup(name='ofxstatement-be-hellobank-fr',
      version="0.1",
      author="jibus",
      author_email="yoga-stretch-bony@duck.com",
      url="https://github.com/jibuus/ofxstatement-be-hellobank-fr",
      description=("ofxstatement plugin for parsing Hello Bank FR's CSV statements to OFX"),
      long_description=long_description,
      license="GPLv3",
      keywords=["ofx", "banking", "statement", "hellobank", "csv"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3',
          'Natural Language :: French',
          'Topic :: Office/Business :: Financial :: Accounting',
          'Topic :: Utilities',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=["ofxstatement", "ofxstatement.plugins"],
      entry_points={
          'ofxstatement':
          ['be_hellobank_fr = ofxstatement.plugins.be_hellobank_fr:HelloBankFRPlugin']
          },
      install_requires=['ofxstatement'],
      include_package_data=True,
      zip_safe=True
      )
