# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 4.7
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import aylien_news_api
from aylien_news_api.models.deprecated_entity import DeprecatedEntity  # noqa: E501
from aylien_news_api.rest import ApiException

class TestDeprecatedEntity(unittest.TestCase):
    """DeprecatedEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeprecatedEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.deprecated_entity.DeprecatedEntity()  # noqa: E501
        if include_optional :
            return DeprecatedEntity(
                id = '0', 
                indices = [
                    [
                        56
                        ]
                    ], 
                links = aylien_news_api.models.entity_links.EntityLinks(
                    dbpedia = '0', 
                    wikipedia = '0', 
                    wikidata = '0', ), 
                text = '0', 
                stock_ticker = '0', 
                types = [
                    '0'
                    ], 
                sentiment = aylien_news_api.models.entity_sentiment.EntitySentiment(
                    polarity = 'positive', 
                    confidence = 0, ), 
                surface_forms = [
                    aylien_news_api.models.deprecated_entity_surface_form.DeprecatedEntitySurfaceForm(
                        text = '0', 
                        indices = [
                            [
                                56
                                ]
                            ], 
                        frequency = 0, )
                    ], 
                prominence_score = 0
            )
        else :
            return DeprecatedEntity(
        )

    def testDeprecatedEntity(self):
        """Test DeprecatedEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
