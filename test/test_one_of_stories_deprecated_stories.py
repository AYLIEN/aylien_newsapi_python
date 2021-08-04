"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import aylien_news_api
from aylien_news_api.model.deprecated_stories import DeprecatedStories
from aylien_news_api.model.deprecated_story import DeprecatedStory
from aylien_news_api.model.stories import Stories
from aylien_news_api.model.warning import Warning
globals()['DeprecatedStories'] = DeprecatedStories
globals()['DeprecatedStory'] = DeprecatedStory
globals()['Stories'] = Stories
globals()['Warning'] = Warning
from aylien_news_api.model.one_of_stories_deprecated_stories import OneOfStoriesDeprecatedStories


class TestOneOfStoriesDeprecatedStories(unittest.TestCase):
    """OneOfStoriesDeprecatedStories unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOneOfStoriesDeprecatedStories(self):
        """Test OneOfStoriesDeprecatedStories"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OneOfStoriesDeprecatedStories()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()