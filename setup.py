# coding: utf-8

"""
Copyright 2017 Aylien, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


import sys
from setuptools import setup, find_packages

NAME = "aylien_news_api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="AYLIEN News API Client Library for Python",
    author="AYLIEN Inc., Hamed Ramezanian Nik",
    author_email="support@aylien.com, hamed.r.nik@gmail.com",
    url="https://newsapi.aylien.com/",
    download_url = "https://github.com/AYLIEN/aylien_newsapi_python/tarball/v" + VERSION,
    keywords="aylien news api client",
    install_requires=REQUIRES,
    packages=find_packages(),
    license="Apache-2.0",
    include_package_data=True,
    long_description=open('README.rst').read(),
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: Microsoft',
      'Operating System :: POSIX',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ]
)
