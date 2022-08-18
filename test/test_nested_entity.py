# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.3
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import aylien_news_api
from aylien_news_api.models.nested_entity import NestedEntity  # noqa: E501
from aylien_news_api.rest import ApiException

class TestNestedEntity(unittest.TestCase):
    """NestedEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NestedEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.nested_entity.NestedEntity()  # noqa: E501
        if include_optional :
            return NestedEntity(
                id = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                name = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                surface_forms_text = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                sentiment = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                element = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                links_wikipedia = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                links_wikidata = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                stock_ticker = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, ), 
                type = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
                    __eq = null, 
                    __text = null, 
                    __in = [
                        null
                        ], 
                    __gt = 1.337, 
                    __gte = 1.337, 
                    __lt = 1.337, 
                    __lte = 1.337, 
                    __boost = 1.337, )
            )
        else :
            return NestedEntity(
        )

    def testNestedEntity(self):
        """Test NestedEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
