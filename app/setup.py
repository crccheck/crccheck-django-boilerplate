from setuptools import setup

setup(
    name='{{ project_name }}',
    version='0.0.0',
    author='',
    author_email='c@crccheck.com',
    url='',
    packages=['{{ project_name }}'],
    include_package_data=True,  # automatically include things from MANIFEST.in
    license='Apache License, Version 2.0',
    description='',
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
)
