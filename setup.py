#!/usr/bin/env python

'''
Setup file for CLI Documentation Generator (cdg) library
'''

from setuptools import setup, find_packages

setup(name='cdg',
      version='0.0.1',
      description='A tool to automatically generate documentation for command line tools',
      url='https://github.com/imayobrown/cdg',
      author='Ian Brown',
      author_email='i.mayo.brown@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      entry_points={
          'console_scripts': ['cdg = cdg.main:main']
      }
)
