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


class Rank(object):
    def __init__(self, rank=None, country=None, fetched_at=None):
        """
        Rank - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'rank': 'int',
            'country': 'str',
            'fetched_at': 'datetime'
        }

        self.attribute_map = {
            'rank': 'rank',
            'country': 'country',
            'fetched_at': 'fetched_at'
        }

        self._rank = rank
        self._country = country
        self._fetched_at = fetched_at


    @property
    def rank(self):
        """
        Gets the rank of this Rank.
        The rank

        :return: The rank of this Rank.
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this Rank.
        The rank

        :param rank: The rank of this Rank.
        :type: int
        """

        self._rank = rank

    @property
    def country(self):
        """
        Gets the country of this Rank.
        The country code which the rank is in it

        :return: The country of this Rank.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Rank.
        The country code which the rank is in it

        :param country: The country of this Rank.
        :type: str
        """

        self._country = country

    @property
    def fetched_at(self):
        """
        Gets the fetched_at of this Rank.
        The fetched date of the rank

        :return: The fetched_at of this Rank.
        :rtype: datetime
        """
        return self._fetched_at

    @fetched_at.setter
    def fetched_at(self, fetched_at):
        """
        Sets the fetched_at of this Rank.
        The fetched date of the rank

        :param fetched_at: The fetched_at of this Rank.
        :type: datetime
        """

        self._fetched_at = fetched_at

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
