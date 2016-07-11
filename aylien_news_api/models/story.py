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

from pprint import pformat
from six import iteritems
import re


class Story(object):
    def __init__(self, id=None, title=None, body=None, summary=None, source=None, author=None, entities=None, keywords=None, hashtags=None, characters_count=None, words_count=None, sentences_count=None, paragraphs_count=None, categories=None, social_shares_count=None, media=None, sentiment=None, language=None, published_at=None, links=None):
        """
        Story - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'id': 'int',
            'title': 'str',
            'body': 'str',
            'summary': 'Summary',
            'source': 'Source',
            'author': 'Author',
            'entities': 'Entities',
            'keywords': 'list[str]',
            'hashtags': 'list[str]',
            'characters_count': 'int',
            'words_count': 'int',
            'sentences_count': 'int',
            'paragraphs_count': 'int',
            'categories': 'list[Category]',
            'social_shares_count': 'ShareCounts',
            'media': 'list[Media]',
            'sentiment': 'Sentiments',
            'language': 'str',
            'published_at': 'datetime',
            'links': 'StoryLinks'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'body': 'body',
            'summary': 'summary',
            'source': 'source',
            'author': 'author',
            'entities': 'entities',
            'keywords': 'keywords',
            'hashtags': 'hashtags',
            'characters_count': 'characters_count',
            'words_count': 'words_count',
            'sentences_count': 'sentences_count',
            'paragraphs_count': 'paragraphs_count',
            'categories': 'categories',
            'social_shares_count': 'social_shares_count',
            'media': 'media',
            'sentiment': 'sentiment',
            'language': 'language',
            'published_at': 'published_at',
            'links': 'links'
        }

        self._id = id
        self._title = title
        self._body = body
        self._summary = summary
        self._source = source
        self._author = author
        self._entities = entities
        self._keywords = keywords
        self._hashtags = hashtags
        self._characters_count = characters_count
        self._words_count = words_count
        self._sentences_count = sentences_count
        self._paragraphs_count = paragraphs_count
        self._categories = categories
        self._social_shares_count = social_shares_count
        self._media = media
        self._sentiment = sentiment
        self._language = language
        self._published_at = published_at
        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Story.
        ID of the story which is a unique identification

        :return: The id of this Story.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Story.
        ID of the story which is a unique identification

        :param id: The id of this Story.
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this Story.
        Title of the story

        :return: The title of this Story.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Story.
        Title of the story

        :param title: The title of this Story.
        :type: str
        """

        self._title = title

    @property
    def body(self):
        """
        Gets the body of this Story.
        Body of the story

        :return: The body of this Story.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this Story.
        Body of the story

        :param body: The body of this Story.
        :type: str
        """

        self._body = body

    @property
    def summary(self):
        """
        Gets the summary of this Story.
        The suggested story summary

        :return: The summary of this Story.
        :rtype: Summary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this Story.
        The suggested story summary

        :param summary: The summary of this Story.
        :type: Summary
        """

        self._summary = summary

    @property
    def source(self):
        """
        Gets the source of this Story.
        The story source

        :return: The source of this Story.
        :rtype: Source
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Story.
        The story source

        :param source: The source of this Story.
        :type: Source
        """

        self._source = source

    @property
    def author(self):
        """
        Gets the author of this Story.
        The story author

        :return: The author of this Story.
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this Story.
        The story author

        :param author: The author of this Story.
        :type: Author
        """

        self._author = author

    @property
    def entities(self):
        """
        Gets the entities of this Story.
        Extracted entities from the story title or body

        :return: The entities of this Story.
        :rtype: Entities
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this Story.
        Extracted entities from the story title or body

        :param entities: The entities of this Story.
        :type: Entities
        """

        self._entities = entities

    @property
    def keywords(self):
        """
        Gets the keywords of this Story.
        Extracted keywords mentioned in the story title or body

        :return: The keywords of this Story.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this Story.
        Extracted keywords mentioned in the story title or body

        :param keywords: The keywords of this Story.
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def hashtags(self):
        """
        Gets the hashtags of this Story.
        An array of suggested Story hashtags

        :return: The hashtags of this Story.
        :rtype: list[str]
        """
        return self._hashtags

    @hashtags.setter
    def hashtags(self, hashtags):
        """
        Sets the hashtags of this Story.
        An array of suggested Story hashtags

        :param hashtags: The hashtags of this Story.
        :type: list[str]
        """

        self._hashtags = hashtags

    @property
    def characters_count(self):
        """
        Gets the characters_count of this Story.
        Character count of the story body

        :return: The characters_count of this Story.
        :rtype: int
        """
        return self._characters_count

    @characters_count.setter
    def characters_count(self, characters_count):
        """
        Sets the characters_count of this Story.
        Character count of the story body

        :param characters_count: The characters_count of this Story.
        :type: int
        """

        self._characters_count = characters_count

    @property
    def words_count(self):
        """
        Gets the words_count of this Story.
        Word count of the story body

        :return: The words_count of this Story.
        :rtype: int
        """
        return self._words_count

    @words_count.setter
    def words_count(self, words_count):
        """
        Sets the words_count of this Story.
        Word count of the story body

        :param words_count: The words_count of this Story.
        :type: int
        """

        self._words_count = words_count

    @property
    def sentences_count(self):
        """
        Gets the sentences_count of this Story.
        Sentence count of the story body

        :return: The sentences_count of this Story.
        :rtype: int
        """
        return self._sentences_count

    @sentences_count.setter
    def sentences_count(self, sentences_count):
        """
        Sets the sentences_count of this Story.
        Sentence count of the story body

        :param sentences_count: The sentences_count of this Story.
        :type: int
        """

        self._sentences_count = sentences_count

    @property
    def paragraphs_count(self):
        """
        Gets the paragraphs_count of this Story.
        Paragraph count of the story body

        :return: The paragraphs_count of this Story.
        :rtype: int
        """
        return self._paragraphs_count

    @paragraphs_count.setter
    def paragraphs_count(self, paragraphs_count):
        """
        Sets the paragraphs_count of this Story.
        Paragraph count of the story body

        :param paragraphs_count: The paragraphs_count of this Story.
        :type: int
        """

        self._paragraphs_count = paragraphs_count

    @property
    def categories(self):
        """
        Gets the categories of this Story.
        Suggested categories for the story

        :return: The categories of this Story.
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this Story.
        Suggested categories for the story

        :param categories: The categories of this Story.
        :type: list[Category]
        """

        self._categories = categories

    @property
    def social_shares_count(self):
        """
        Gets the social_shares_count of this Story.
        Social shares count for the story

        :return: The social_shares_count of this Story.
        :rtype: ShareCounts
        """
        return self._social_shares_count

    @social_shares_count.setter
    def social_shares_count(self, social_shares_count):
        """
        Sets the social_shares_count of this Story.
        Social shares count for the story

        :param social_shares_count: The social_shares_count of this Story.
        :type: ShareCounts
        """

        self._social_shares_count = social_shares_count

    @property
    def media(self):
        """
        Gets the media of this Story.
        An array of extracted media such as images and videos

        :return: The media of this Story.
        :rtype: list[Media]
        """
        return self._media

    @media.setter
    def media(self, media):
        """
        Sets the media of this Story.
        An array of extracted media such as images and videos

        :param media: The media of this Story.
        :type: list[Media]
        """

        self._media = media

    @property
    def sentiment(self):
        """
        Gets the sentiment of this Story.
        Suggested sentiments for the story title or body

        :return: The sentiment of this Story.
        :rtype: Sentiments
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """
        Sets the sentiment of this Story.
        Suggested sentiments for the story title or body

        :param sentiment: The sentiment of this Story.
        :type: Sentiments
        """

        self._sentiment = sentiment

    @property
    def language(self):
        """
        Gets the language of this Story.
        Language of the story

        :return: The language of this Story.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Story.
        Language of the story

        :param language: The language of this Story.
        :type: str
        """

        self._language = language

    @property
    def published_at(self):
        """
        Gets the published_at of this Story.
        Published date of the story

        :return: The published_at of this Story.
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """
        Sets the published_at of this Story.
        Published date of the story

        :param published_at: The published_at of this Story.
        :type: datetime
        """

        self._published_at = published_at

    @property
    def links(self):
        """
        Gets the links of this Story.
        Links which is related to the story

        :return: The links of this Story.
        :rtype: StoryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Story.
        Links which is related to the story

        :param links: The links of this Story.
        :type: StoryLinks
        """

        self._links = links

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.api_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
