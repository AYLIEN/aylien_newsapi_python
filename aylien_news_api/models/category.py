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


class Category(object):
    def __init__(self, id=None, taxonomy=None, level=None, score=None, confident=None, links=None):
        """
        Category - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'id': 'str',
            'taxonomy': 'str',
            'level': 'int',
            'score': 'float',
            'confident': 'bool',
            'links': 'CategoryLinks'
        }

        self.attribute_map = {
            'id': 'id',
            'taxonomy': 'taxonomy',
            'level': 'level',
            'score': 'score',
            'confident': 'confident',
            'links': 'links'
        }

        self._id = id
        self._taxonomy = taxonomy
        self._level = level
        self._score = score
        self._confident = confident
        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Category.
        The ID of the category

        :return: The id of this Category.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Category.
        The ID of the category

        :param id: The id of this Category.
        :type: str
        """

        self._id = id

    @property
    def taxonomy(self):
        """
        Gets the taxonomy of this Category.
        The taxonomy of the category

        :return: The taxonomy of this Category.
        :rtype: str
        """
        return self._taxonomy

    @taxonomy.setter
    def taxonomy(self, taxonomy):
        """
        Sets the taxonomy of this Category.
        The taxonomy of the category

        :param taxonomy: The taxonomy of this Category.
        :type: str
        """
        allowed_values = ["iab-qag", "iptc-subjectcode"]
        if taxonomy not in allowed_values:
            raise ValueError(
                "Invalid value for `taxonomy`, must be one of {0}"
                .format(allowed_values)
            )

        self._taxonomy = taxonomy

    @property
    def level(self):
        """
        Gets the level of this Category.
        The level of the category

        :return: The level of this Category.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this Category.
        The level of the category

        :param level: The level of this Category.
        :type: int
        """

        self._level = level

    @property
    def score(self):
        """
        Gets the score of this Category.
        The score of the category

        :return: The score of this Category.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this Category.
        The score of the category

        :param score: The score of this Category.
        :type: float
        """

        self._score = score

    @property
    def confident(self):
        """
        Gets the confident of this Category.
        It defines whether the extracted category is confident or not

        :return: The confident of this Category.
        :rtype: bool
        """
        return self._confident

    @confident.setter
    def confident(self, confident):
        """
        Sets the confident of this Category.
        It defines whether the extracted category is confident or not

        :param confident: The confident of this Category.
        :type: bool
        """

        self._confident = confident

    @property
    def links(self):
        """
        Gets the links of this Category.
        Related links for the category

        :return: The links of this Category.
        :rtype: CategoryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Category.
        Related links for the category

        :param links: The links of this Category.
        :type: CategoryLinks
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
