# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import aylien_news_api
from aylien_news_api.api.coverages_api import CoveragesApi  # noqa: E501
from aylien_news_api.rest import ApiException


class TestCoveragesApi(unittest.TestCase):
    """CoveragesApi unit test stubs"""

    def setUp(self):
        self.api = aylien_news_api.api.coverages_api.CoveragesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_coverages(self):
        """Test case for list_coverages

        List coverages  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
