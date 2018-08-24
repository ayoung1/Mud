#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
	name="SneakyMUD",
	version="0.0.0",
	packages=find_packages(),
        package_data={'': ['data_files/races/*.json',
                           'data_files/mobs/*.json',
                           'data_files/cities/*.json',
                           'data_files/locations/*.json']},
)
