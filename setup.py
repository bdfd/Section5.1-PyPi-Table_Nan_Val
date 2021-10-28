'''
Author:  BDFD
Date: 2021-10-27 18:39:19
LastEditTime: 2021-10-28 10:34:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \6.0-PyPI_Missing_Value_Table\setup.py
'''
from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="table_nan_val",
    version="1.0.0",
    author="BDFD",
    author_email="bdfd2005@gmail.com",
    description="find missing value for DataFrame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bdfd/6.1-PyPI_Table_Nan_Val",
    project_urls={
        "Bug Tracker": "https://github.com/bdfd/6.1-PyPI_Table_Nan_Val/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy >= 1.19.5",
        "pandas >= 1.1.5",
        "matplotlib >= 3.2.2",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
