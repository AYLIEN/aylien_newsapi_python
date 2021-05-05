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
import datetime

import aylien_news_api
from aylien_news_api.models.stories import Stories  # noqa: E501
from aylien_news_api.rest import ApiException

class TestStories(unittest.TestCase):
    """Stories unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Stories
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.stories.Stories()  # noqa: E501
        if include_optional :
            return Stories(
                next_page_cursor = '0', 
                stories = [
                    aylien_news_api.models.story.Story(
                        author = aylien_news_api.models.author.Author(
                            avatar_url = '0', 
                            id = 56, 
                            name = '0', ), 
                        body = '0', 
                        categories = [
                            aylien_news_api.models.category.Category(
                                confident = True, 
                                id = '0', 
                                label = '0', 
                                level = 56, 
                                links = aylien_news_api.models.category_links.CategoryLinks(
                                    parent = '0', 
                                    self = '0', ), 
                                score = 1.337, 
                                taxonomy = 'iab-qag', )
                            ], 
                        characters_count = 56, 
                        clusters = [
                            56
                            ], 
                        entities = aylien_news_api.models.entities.Entities(
                            body = [
                                aylien_news_api.models.entity.Entity(
                                    id = '0', 
                                    indices = [
                                        [
                                            56
                                            ]
                                        ], 
                                    text = '0', 
                                    stock_ticker = '0', 
                                    types = [
                                        '0'
                                        ], 
                                    sentiment = aylien_news_api.models.entity_sentiment.EntitySentiment(
                                        polarity = 'positive', 
                                        confidence = 0, ), 
                                    surface_forms = [
                                        aylien_news_api.models.entity_surface_form.EntitySurfaceForm(
                                            text = '0', 
                                            frequency = 0, )
                                        ], 
                                    prominence_score = 0, )
                                ], 
                            title = [
                                aylien_news_api.models.entity.Entity(
                                    id = '0', 
                                    text = '0', 
                                    stock_ticker = '0', 
                                    prominence_score = 0, )
                                ], ), 
                        hashtags = [
                            '0'
                            ], 
                        id = 56, 
                        keywords = [
                            '0'
                            ], 
                        language = '0', 
                        links = aylien_news_api.models.story_links.StoryLinks(
                            canonical = '0', 
                            permalink = '0', 
                            related_stories = '0', ), 
                        media = [
                            aylien_news_api.models.media.Media(
                                content_length = 56, 
                                format = 'BMP', 
                                height = 56, 
                                type = 'image', 
                                url = '0', 
                                width = 56, )
                            ], 
                        paragraphs_count = 56, 
                        published_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        sentences_count = 56, 
                        sentiment = aylien_news_api.models.sentiments.Sentiments(), 
                        social_shares_count = aylien_news_api.models.share_counts.ShareCounts(
                            facebook = [
                                aylien_news_api.models.share_count.ShareCount(
                                    count = 56, 
                                    fetched_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            google_plus = [
                                aylien_news_api.models.share_count.ShareCount(
                                    count = 56, 
                                    fetched_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            linkedin = [
                                aylien_news_api.models.share_count.ShareCount(
                                    count = 56, 
                                    fetched_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            reddit = [
                                aylien_news_api.models.share_count.ShareCount(
                                    count = 56, 
                                    fetched_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], ), 
                        source = aylien_news_api.models.source.Source(
                            description = '0', 
                            domain = '0', 
                            home_page_url = '0', 
                            id = 56, 
                            links_in_count = 56, 
                            locations = [
                                aylien_news_api.models.location.Location(
                                    city = '0', 
                                    country = '0', 
                                    state = '0', )
                                ], 
                            logo_url = '0', 
                            name = '0', 
                            rankings = aylien_news_api.models.rankings.Rankings(
                                alexa = [
                                    aylien_news_api.models.rank.Rank(
                                        country = '0', 
                                        fetched_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        rank = 56, )
                                    ], ), 
                            scopes = [
                                aylien_news_api.models.scope.Scope(
                                    city = '0', 
                                    country = '0', 
                                    level = 'international', 
                                    state = '0', )
                                ], ), 
                        summary = aylien_news_api.models.summary.Summary(
                            sentences = [
                                '0'
                                ], ), 
                        title = '0', 
                        translations = aylien_news_api.models.story_translations.StoryTranslations(
                            en = aylien_news_api.models.story_translation.StoryTranslation(), ), 
                        words_count = 56, 
                        license_type = 56, )
                    ], 
                published_at_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                published_at_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                warnings = [
                    aylien_news_api.models.warning.Warning(
                        id = '0', 
                        links = aylien_news_api.models.error_links.ErrorLinks(
                            about = '0', 
                            docs = '0', ), 
                        detail = '0', )
                    ]
            )
        else :
            return Stories(
        )

    def testStories(self):
        """Test Stories"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
