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


class Scope(object):
    def __init__(self, country=None, state=None, city=None, level=None):
        """
        Scope - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'country': 'str',
            'state': 'str',
            'city': 'str',
            'level': 'str'
        }

        self.attribute_map = {
            'country': 'country',
            'state': 'state',
            'city': 'city',
            'level': 'level'
        }

        self._country = country
        self._state = state
        self._city = city
        self._level = level

    @property
    def country(self):
        """
        Gets the country of this Scope.
        The source scope by country code. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes.

        :return: The country of this Scope.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Scope.
        The source scope by country code. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes.

        :param country: The country of this Scope.
        :type: str
        """

        self._country = country

    @property
    def state(self):
        """
        Gets the state of this Scope.
        The scope by state

        :return: The state of this Scope.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Scope.
        The scope by state

        :param state: The state of this Scope.
        :type: str
        """

        self._state = state

    @property
    def city(self):
        """
        Gets the city of this Scope.
        The scope by city

        :return: The city of this Scope.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Scope.
        The scope by city

        :param city: The city of this Scope.
        :type: str
        """

        self._city = city

    @property
    def level(self):
        """
        Gets the level of this Scope.
        The scope by level

        :return: The level of this Scope.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """
        Sets the level of this Scope.
        The scope by level

        :param level: The level of this Scope.
        :type: str
        """
        allowed_values = ["international", "national", "local"]
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level`, must be one of {0}"
                .format(allowed_values)
            )

        self._level = level

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
