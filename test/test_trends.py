# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 4.6
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import aylien_news_api
from aylien_news_api.models.trends import Trends  # noqa: E501
from aylien_news_api.rest import ApiException

class TestTrends(unittest.TestCase):
    """Trends unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Trends
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.trends.Trends()  # noqa: E501
        if include_optional :
            return Trends(
                field = '0', 
                trends = [
                    aylien_news_api.models.trend.Trend(
                        count = 56, 
                        value = '0', 
                        sentiment = aylien_news_api.models.aggregated_sentiment.AggregatedSentiment(
                            positive = 56, 
                            neutral = 56, 
                            negative = 56, ), )
                    ], 
                published_at_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                published_at_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Trends(
        )

    def testTrends(self):
        """Test Trends"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
