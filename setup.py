import sys; sys.exit("NOPE!")

from setuptools import find_packages
from distutils.core import setup

import {{ MY_PROJECT }}

setup(
    name='INSERT NAME HERE',
    version={{ MY_PROJECT }}.__version__,
    # author
    # author_email
    # url
    packages=find_packages('.', exclude=('example_project*',)),
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
    ],
)
