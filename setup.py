import sys; sys.exit("NOPE!")

from setuptools import find_packages
from distutils.core import setup


setup(
    name='INSERT NAME HERE',
    version=open('VERSION').read(),
    # author
    # author_email
    # url
    packages=find_packages('.', exclude=('exampleproject*',)),
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
    ],
)
