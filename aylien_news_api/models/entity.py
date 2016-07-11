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


class Entity(object):
    def __init__(self, text=None, score=None, types=None, links=None, indices=None):
        """
        Entity - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'text': 'str',
            'score': 'float',
            'types': 'list[str]',
            'links': 'EntityLinks',
            'indices': 'list[list[int]]'
        }

        self.attribute_map = {
            'text': 'text',
            'score': 'score',
            'types': 'types',
            'links': 'links',
            'indices': 'indices'
        }

        self._text = text
        self._score = score
        self._types = types
        self._links = links
        self._indices = indices

    @property
    def text(self):
        """
        Gets the text of this Entity.
        The entity text

        :return: The text of this Entity.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Entity.
        The entity text

        :param text: The text of this Entity.
        :type: str
        """

        self._text = text

    @property
    def score(self):
        """
        Gets the score of this Entity.
        The entity score

        :return: The score of this Entity.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this Entity.
        The entity score

        :param score: The score of this Entity.
        :type: float
        """

        if not score:
            raise ValueError("Invalid value for `score`, must not be `None`")
        if score > 1.0:
            raise ValueError("Invalid value for `score`, must be a value less than or equal to `1.0`")
        if score < 0.0:
            raise ValueError("Invalid value for `score`, must be a value greater than or equal to `0.0`")

        self._score = score

    @property
    def types(self):
        """
        Gets the types of this Entity.
        An array of the dbpedia types

        :return: The types of this Entity.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this Entity.
        An array of the dbpedia types

        :param types: The types of this Entity.
        :type: list[str]
        """

        self._types = types

    @property
    def links(self):
        """
        Gets the links of this Entity.
        Related links to the entity

        :return: The links of this Entity.
        :rtype: EntityLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Entity.
        Related links to the entity

        :param links: The links of this Entity.
        :type: EntityLinks
        """

        self._links = links

    @property
    def indices(self):
        """
        Gets the indices of this Entity.
        The indices of the entity text

        :return: The indices of this Entity.
        :rtype: list[list[int]]
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        """
        Sets the indices of this Entity.
        The indices of the entity text

        :param indices: The indices of this Entity.
        :type: list[list[int]]
        """

        self._indices = indices

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
