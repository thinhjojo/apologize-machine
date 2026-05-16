#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apologize Machine - The World's Most Dramatic Apology Generator

Setup script for pip installation.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="apologize-machine",
    version="1.0.0",
    author="The Absurd Devs",
    author_email="notreal@apologize-machine.dev",
    description="The world's most dramatic apology generator with multi-language support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thinhjojo/apologize-machine",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Home Sugar Mama :: Humor",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: English",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: Japanese",
        "Natural Language :: Vietnamese",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'apologize=apologize_machine:main',
        ],
    },
    keywords="apology humor funny excuse generator",
    project_urls={
        "Bug Reports": "https://github.com/thinhjojo/apologize-machine/issues",
        "Source": "https://github.com/thinhjojo/apologize-machine",
        "Contributing": "https://github.com/thinhjojo/apologize-machine/blob/main/CONTRIBUTING.md",
    },
)