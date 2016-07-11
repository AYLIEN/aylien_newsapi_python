# coding: utf-8

# Copyright 2016 Aylien, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import os
import sys
import unittest

import aylien_news_api
from aylien_news_api.rest import ApiException
from aylien_news_api.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = aylien_news_api.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_list_autocompletes(self):
        """
        Test case for list_autocompletes

        List autocompletes
        """
        pass

    def test_list_coverages(self):
        """
        Test case for list_coverages

        List coverages
        """
        pass

    def test_list_histograms(self):
        """
        Test case for list_histograms

        List histograms
        """
        pass

    def test_list_related_stories(self):
        """
        Test case for list_related_stories

        List related stories
        """
        pass

    def test_list_stories(self):
        """
        Test case for list_stories

        List Stories
        """
        pass

    def test_list_time_series(self):
        """
        Test case for list_time_series

        List time series
        """
        pass

    def test_list_trends(self):
        """
        Test case for list_trends

        List trends
        """
        pass


if __name__ == '__main__':
    unittest.main()
