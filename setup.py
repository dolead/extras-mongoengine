#!/usr/bin/env python3
from setuptools import setup


setup(name='dolead_extras_mongoengine',
      version='0.3.1',
      description='Extra stuff for MongoEngine ORM',
      keywords='mongoengine soft-delete enum',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"],
      license="GPLv3",
      author="François Schmidts",
      author_email="francois.schmidts@dolead.com",
      maintainer="François Schmidts",
      maintainer_email="francois.schmidts@dolead.com",
      packages=['extras_mongoengine'],
      url='https://github.com/dolead/dolead_entry_points',
)
