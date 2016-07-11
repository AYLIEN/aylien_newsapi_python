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


class StoryCluster(object):
    def __init__(self, id=None, phrases=None, size=None, stories=None, score=None):
        """
        StoryCluster - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'id': 'int',
            'phrases': 'list[str]',
            'size': 'int',
            'stories': 'list[int]',
            'score': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'phrases': 'phrases',
            'size': 'size',
            'stories': 'stories',
            'score': 'score'
        }

        self._id = id
        self._phrases = phrases
        self._size = size
        self._stories = stories
        self._score = score

    @property
    def id(self):
        """
        Gets the id of this StoryCluster.
        A unique identification for the cluster

        :return: The id of this StoryCluster.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StoryCluster.
        A unique identification for the cluster

        :param id: The id of this StoryCluster.
        :type: int
        """

        self._id = id

    @property
    def phrases(self):
        """
        Gets the phrases of this StoryCluster.
        Suggested labels for the cluster

        :return: The phrases of this StoryCluster.
        :rtype: list[str]
        """
        return self._phrases

    @phrases.setter
    def phrases(self, phrases):
        """
        Sets the phrases of this StoryCluster.
        Suggested labels for the cluster

        :param phrases: The phrases of this StoryCluster.
        :type: list[str]
        """

        self._phrases = phrases

    @property
    def size(self):
        """
        Gets the size of this StoryCluster.
        Size of the cluster

        :return: The size of this StoryCluster.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this StoryCluster.
        Size of the cluster

        :param size: The size of this StoryCluster.
        :type: int
        """

        self._size = size

    @property
    def stories(self):
        """
        Gets the stories of this StoryCluster.
        Story ids which are in the cluster

        :return: The stories of this StoryCluster.
        :rtype: list[int]
        """
        return self._stories

    @stories.setter
    def stories(self, stories):
        """
        Sets the stories of this StoryCluster.
        Story ids which are in the cluster

        :param stories: The stories of this StoryCluster.
        :type: list[int]
        """

        self._stories = stories

    @property
    def score(self):
        """
        Gets the score of this StoryCluster.
        The cluster score

        :return: The score of this StoryCluster.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this StoryCluster.
        The cluster score

        :param score: The score of this StoryCluster.
        :type: float
        """

        self._score = score

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
