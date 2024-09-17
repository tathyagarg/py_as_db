from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='py_database',
    version="1.2.2",
    license="MIT",
    description="Python files used as databases.",
    long_description=long_description,
    author="Tathya Garg",
    author_email="coding.tathya@gmail.com",
    packages=["py_database"],
    install_requires=['wheel']
)