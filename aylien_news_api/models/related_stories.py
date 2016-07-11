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


class RelatedStories(object):
    def __init__(self, story_title=None, story_body=None, story_language=None, related_stories=None, clusters=None):
        """
        RelatedStories - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'story_title': 'str',
            'story_body': 'str',
            'story_language': 'str',
            'related_stories': 'list[Story]',
            'clusters': 'list[StoryCluster]'
        }

        self.attribute_map = {
            'story_title': 'story_title',
            'story_body': 'story_body',
            'story_language': 'story_language',
            'related_stories': 'related_stories',
            'clusters': 'clusters'
        }

        self._story_title = story_title
        self._story_body = story_body
        self._story_language = story_language
        self._related_stories = related_stories
        self._clusters = clusters

    @property
    def story_title(self):
        """
        Gets the story_title of this RelatedStories.
        The input story title

        :return: The story_title of this RelatedStories.
        :rtype: str
        """
        return self._story_title

    @story_title.setter
    def story_title(self, story_title):
        """
        Sets the story_title of this RelatedStories.
        The input story title

        :param story_title: The story_title of this RelatedStories.
        :type: str
        """

        self._story_title = story_title

    @property
    def story_body(self):
        """
        Gets the story_body of this RelatedStories.
        The input story body

        :return: The story_body of this RelatedStories.
        :rtype: str
        """
        return self._story_body

    @story_body.setter
    def story_body(self, story_body):
        """
        Sets the story_body of this RelatedStories.
        The input story body

        :param story_body: The story_body of this RelatedStories.
        :type: str
        """

        self._story_body = story_body

    @property
    def story_language(self):
        """
        Gets the story_language of this RelatedStories.
        The input story language

        :return: The story_language of this RelatedStories.
        :rtype: str
        """
        return self._story_language

    @story_language.setter
    def story_language(self, story_language):
        """
        Sets the story_language of this RelatedStories.
        The input story language

        :param story_language: The story_language of this RelatedStories.
        :type: str
        """

        self._story_language = story_language

    @property
    def related_stories(self):
        """
        Gets the related_stories of this RelatedStories.
        An array of related stories for the input story

        :return: The related_stories of this RelatedStories.
        :rtype: list[Story]
        """
        return self._related_stories

    @related_stories.setter
    def related_stories(self, related_stories):
        """
        Sets the related_stories of this RelatedStories.
        An array of related stories for the input story

        :param related_stories: The related_stories of this RelatedStories.
        :type: list[Story]
        """

        self._related_stories = related_stories

    @property
    def clusters(self):
        """
        Gets the clusters of this RelatedStories.
        An array of clusters

        :return: The clusters of this RelatedStories.
        :rtype: list[StoryCluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """
        Sets the clusters of this RelatedStories.
        An array of clusters

        :param clusters: The clusters of this RelatedStories.
        :type: list[StoryCluster]
        """

        self._clusters = clusters

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
