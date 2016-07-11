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


class StoryLinks(object):
    def __init__(self, permalink=None, related_stories=None, coverages=None):
        """
        StoryLinks - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'permalink': 'str',
            'related_stories': 'str',
            'coverages': 'str'
        }

        self.attribute_map = {
            'permalink': 'permalink',
            'related_stories': 'related_stories',
            'coverages': 'coverages'
        }

        self._permalink = permalink
        self._related_stories = related_stories
        self._coverages = coverages

    @property
    def permalink(self):
        """
        Gets the permalink of this StoryLinks.
        The story permalink URL

        :return: The permalink of this StoryLinks.
        :rtype: str
        """
        return self._permalink

    @permalink.setter
    def permalink(self, permalink):
        """
        Sets the permalink of this StoryLinks.
        The story permalink URL

        :param permalink: The permalink of this StoryLinks.
        :type: str
        """

        self._permalink = permalink

    @property
    def related_stories(self):
        """
        Gets the related_stories of this StoryLinks.
        The related stories URL

        :return: The related_stories of this StoryLinks.
        :rtype: str
        """
        return self._related_stories

    @related_stories.setter
    def related_stories(self, related_stories):
        """
        Sets the related_stories of this StoryLinks.
        The related stories URL

        :param related_stories: The related_stories of this StoryLinks.
        :type: str
        """

        self._related_stories = related_stories

    @property
    def coverages(self):
        """
        Gets the coverages of this StoryLinks.
        The coverages URL

        :return: The coverages of this StoryLinks.
        :rtype: str
        """
        return self._coverages

    @coverages.setter
    def coverages(self, coverages):
        """
        Sets the coverages of this StoryLinks.
        The coverages URL

        :param coverages: The coverages of this StoryLinks.
        :type: str
        """

        self._coverages = coverages

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
