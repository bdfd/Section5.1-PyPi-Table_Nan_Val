'''
Author:  BDFD
Date: 2021-10-27 18:39:19
LastEditTime: 2021-10-27 21:33:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \6.0-PyPI_Missing_Value_Table\setup.py
'''
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="templateproj",
    version="1.0.0",
    author="BDFD",
    author_email="bdfd2005@gmail.com",
    description="find missing value for DataFrame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bdfd",
    project_urls={
        "Bug Tracker": "https://github.com/bdfd",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
