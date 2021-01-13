import os
from setuptools import setup
from setuptools import find_packages
from pymed.version import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pymed-iplweb",
    version=__version__,
    author="Gijs Wobben",
    maintainer="Michał Pasternak",
    author_email="gijswobben@gmail.com",
    maintainer_email="michal.dtz@gmail.com",
    description=("Python library for access to PubMed"),
    license="MIT",
    keywords="PubMed PMC",
    url="https://github.com/mpasternak/pymed-iplweb",
    packages=find_packages(),
    install_requires=["requests>=2.20.0"],
    tests_require=["pytest"],
    long_description_content_type="text/x-rst",
    long_description=read("README.rst"),
    classifiers=[
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
