exit("NOPE!")

from setuptools import setup, find_packages

setup(
    name='{{ app_name }}',
    version='0.1.0',
    author='',
    author_email='c@crccheck.com',
    url='',
    packages=[{{ app_name }}],
    include_package_data=True,  # automatically include things from MANIFEST
    license='Apache License, Version 2.0',
    description='',
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
    ],
)
