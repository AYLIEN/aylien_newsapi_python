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
from aylien_news_api.models.story import Story  # noqa: E501
from aylien_news_api.rest import ApiException

class TestStory(unittest.TestCase):
    """Story unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Story
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aylien_news_api.models.story.Story()  # noqa: E501
        if include_optional :
            return Story(
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
                entities = [
                    aylien_news_api.models.entity.Entity(
                        id = '0', 
                        links = aylien_news_api.models.entity_links.EntityLinks(
                            dbpedia = '0', 
                            wikipedia = '0', 
                            wikidata = '0', ), 
                        stock_tickers = [
                            '0'
                            ], 
                        types = [
                            '0'
                            ], 
                        overall_sentiment = aylien_news_api.models.entity_sentiment.EntitySentiment(
                            polarity = 'positive', 
                            confidence = 0, ), 
                        overall_prominence = 0, 
                        overall_frequency = 0, 
                        body = aylien_news_api.models.entity_in_text.EntityInText(
                            sentiment = aylien_news_api.models.entity_sentiment.EntitySentiment(
                                confidence = 0, ), 
                            surface_forms = [
                                aylien_news_api.models.entity_surface_form.EntitySurfaceForm(
                                    text = '0', 
                                    frequency = 0, 
                                    mentions = [
                                        aylien_news_api.models.entity_mention.EntityMention(
                                            index = aylien_news_api.models.entity_mention_index.EntityMentionIndex(
                                                start = 0, 
                                                end = 1, ), )
                                        ], )
                                ], ), 
                        title = aylien_news_api.models.entity_in_text.EntityInText(), )
                    ], 
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
                    related_stories = '0', 
                    clusters = '0', ), 
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
                sentiment = aylien_news_api.models.sentiments.Sentiments(
                    body = aylien_news_api.models.sentiment.Sentiment(
                        polarity = 'positive', 
                        score = 0, ), 
                    title = aylien_news_api.models.sentiment.Sentiment(
                        score = 0, ), ), 
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
                        ], 
                    title = '0', ), 
                summary = aylien_news_api.models.summary.Summary(
                    sentences = [
                        '0'
                        ], ), 
                title = '0', 
                translations = aylien_news_api.models.story_translations.StoryTranslations(
                    en = aylien_news_api.models.story_translation.StoryTranslation(
                        body = '0', 
                        title = '0', ), ), 
                words_count = 56, 
                license_type = 56
            )
        else :
            return Story(
        )

    def testStory(self):
        """Test Story"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
