from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyAudioAnalysis',
      version=version,
      description="alecs audio lib for python",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='py audi',
      author='alec harmon blumenfeld',
      author_email='alecblumenfeld@gmail.com',
      url='alcharmon.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
