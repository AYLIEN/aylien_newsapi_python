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


class Stories(object):
    def __init__(self, stories=None, clusters=None, next_page_cursor=None):
        """
        Stories - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'stories': 'list[Story]',
            'clusters': 'list[StoryCluster]',
            'next_page_cursor': 'str'
        }

        self.attribute_map = {
            'stories': 'stories',
            'clusters': 'clusters',
            'next_page_cursor': 'next_page_cursor'
        }

        self._stories = stories
        self._clusters = clusters
        self._next_page_cursor = next_page_cursor

    @property
    def stories(self):
        """
        Gets the stories of this Stories.
        An array of stories

        :return: The stories of this Stories.
        :rtype: list[Story]
        """
        return self._stories

    @stories.setter
    def stories(self, stories):
        """
        Sets the stories of this Stories.
        An array of stories

        :param stories: The stories of this Stories.
        :type: list[Story]
        """

        self._stories = stories

    @property
    def clusters(self):
        """
        Gets the clusters of this Stories.
        An array of clusters

        :return: The clusters of this Stories.
        :rtype: list[StoryCluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """
        Sets the clusters of this Stories.
        An array of clusters

        :param clusters: The clusters of this Stories.
        :type: list[StoryCluster]
        """

        self._clusters = clusters

    @property
    def next_page_cursor(self):
        """
        Gets the next_page_cursor of this Stories.
        The next page cursor

        :return: The next_page_cursor of this Stories.
        :rtype: str
        """
        return self._next_page_cursor

    @next_page_cursor.setter
    def next_page_cursor(self, next_page_cursor):
        """
        Sets the next_page_cursor of this Stories.
        The next page cursor

        :param next_page_cursor: The next_page_cursor of this Stories.
        :type: str
        """

        self._next_page_cursor = next_page_cursor

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
