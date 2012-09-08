import sys; sys.exit("NOPE!")

from distutils.core import setup


setup(
    name='INSERT NAME HERE',
    version=open('VERSION').read(),
    # author
    # author_email
    # url
    packages=['xxxxxxxx', ],
    license='Apache License, Version 2.0',
    long_description=open('README.md').read(),
    classifiers=[
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
    ],
)
