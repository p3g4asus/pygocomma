'''
Created on 25 apr 2019

@author: Matteo
'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygocomma",
    version="1.13",
    author="p3g4asus",
    author_email="fulminedipegasus@gmail.com",
    description="Asyncio module for Gocomma R9 devices control",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/p3g4asus/pygocomma",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pycryptodome',
    ]
)
