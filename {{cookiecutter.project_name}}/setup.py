#!/usr/bin/env python
from setuptools import setup

setup(
    name="{{cookiecutter.project_name}}",
    version="0.1.0",
    description="DPMN tap for extracting data",
    author="",
    url="",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["{{cookiecutter.package_name}}"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "requests",
    ],
    entry_points="""
    [console_scripts]
    {{cookiecutter.project_name}}={{cookiecutter.package_name}}:main
    """,
    packages=["{{cookiecutter.package_name}}"],
    package_data = {
        "schemas": ["{{cookiecutter.package_name}}/schemas/*.json"]
    },
    include_package_data=True,
)
