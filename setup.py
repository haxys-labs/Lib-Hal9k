import pathlib
import re
import sys

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
PACKAGE_NAME = "hal9k"

CONST_TEXT = (HERE / f"{PACKAGE_NAME}/const.py").read_text()
VERSION = re.search('__version__ = "([^\']+)"', CONST_TEXT).group(1)

setup(
    name="Lib-HaL9k",
    version=VERSION,
    description="The HackerLab 9000 Controller Library.",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="hacker hacking lab laboratory virtual machine virtualbox vm",
    url="https://github.com/haxys-labs/Lib-Hal9k",
    project_urls={
        "Source Code": "https://github.com/haxys-labs/Lib-Hal9k",
        "Documentation": "https://github.com/haxys-labs/Lib-Hal9k",
    },
    author="CMSteffen",
    author_email="cmsteffen@haxys.net",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
    packages=[PACKAGE_NAME],
    include_package_data=True,
    install_requires=["virtualbox ==2.0.0"],
    entry_points={},
)
