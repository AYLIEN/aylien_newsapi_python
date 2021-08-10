# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import aylien_news_api
from aylien_news_api.models.parameter import Parameter  # noqa: E501
from aylien_news_api.rest import ApiException

class TestParameter(unittest.TestCase):
    """Parameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Parameter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.parameter.Parameter()  # noqa: E501
        if include_optional :
            return Parameter(
                author_id = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                author_name = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                body = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                categories_confident = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                categories_id = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                categories_level = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                categories_taxonomy = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                clusters = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                links_permalink = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                entities_id = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                entities_surface_forms_text = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                entities_links_wikipedia = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                entities_links_wikidata = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                entities_title_surface_forms_text = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                entities_body_surface_forms_text = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                language = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_content_length_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_content_length_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_count_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_count_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_format = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_height_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_height_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_width_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_images_width_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_videos_count_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                media_videos_count_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                sentiment_body_polarity = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                sentiment_title_polarity = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                social_shares_count_facebook_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                social_shares_count_facebook_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                social_shares_count_reddit_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                social_shares_count_reddit_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_domain = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_id = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_links_in_count_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_links_in_count_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_locations_city = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_locations_country = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_locations_state = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_rankings_alexa_country = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_rankings_alexa_rank_max = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_rankings_alexa_rank_min = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_scopes_city = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_scopes_country = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_scopes_level = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                source_scopes_state = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                story_url = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                story_language = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                text = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                title = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                translations_en_body = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                translations_en_text = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                translations_en_title = aylien_news_api.models.query_defines_the_search_query_on_a_field.Query defines the search query on a field(
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
                entity = null
            )
        else :
            return Parameter(
        )

    def testParameter(self):
        """Test Parameter"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
