exit("NOPE!")

from setuptools import find_packages
from distutils.core import setup

import {{ MY_PROJECT }} as app

setup(
    name=app.__name__,
    version=app.__version__,
    # author
    # author_email
    # url
    packages=find_packages('.', exclude=('example_project*',)),
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    description=app.__doc__.strip(),
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
    ],
)
