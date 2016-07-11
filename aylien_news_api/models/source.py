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


class Source(object):
    def __init__(self, id=None, name=None, domain=None, logo_url=None, locations=None, scopes=None):
        """
        Source - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'id': 'int',
            'name': 'str',
            'domain': 'str',
            'logo_url': 'str',
            'locations': 'list[Location]',
            'scopes': 'list[Scope]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'domain': 'domain',
            'logo_url': 'logo_url',
            'locations': 'locations',
            'scopes': 'scopes'
        }

        self._id = id
        self._name = name
        self._domain = domain
        self._logo_url = logo_url
        self._locations = locations
        self._scopes = scopes

    @property
    def id(self):
        """
        Gets the id of this Source.
        The source id which is a unique value

        :return: The id of this Source.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Source.
        The source id which is a unique value

        :param id: The id of this Source.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Source.
        The source name

        :return: The name of this Source.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Source.
        The source name

        :param name: The name of this Source.
        :type: str
        """

        self._name = name

    @property
    def domain(self):
        """
        Gets the domain of this Source.
        Domain name of the source which is extracted from the source URL

        :return: The domain of this Source.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this Source.
        Domain name of the source which is extracted from the source URL

        :param domain: The domain of this Source.
        :type: str
        """

        self._domain = domain

    @property
    def logo_url(self):
        """
        Gets the logo_url of this Source.
        A URL which points to the source logo

        :return: The logo_url of this Source.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """
        Sets the logo_url of this Source.
        A URL which points to the source logo

        :param logo_url: The logo_url of this Source.
        :type: str
        """

        self._logo_url = logo_url

    @property
    def locations(self):
        """
        Gets the locations of this Source.
        The source locations which are tend to be the physical locations of the source, e.g. BBC headquarter is located in London.

        :return: The locations of this Source.
        :rtype: list[Location]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this Source.
        The source locations which are tend to be the physical locations of the source, e.g. BBC headquarter is located in London.

        :param locations: The locations of this Source.
        :type: list[Location]
        """

        self._locations = locations

    @property
    def scopes(self):
        """
        Gets the scopes of this Source.
        The source scopes which is tend to be scope locations of the source, e.g. BBC scopes is international. 

        :return: The scopes of this Source.
        :rtype: list[Scope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this Source.
        The source scopes which is tend to be scope locations of the source, e.g. BBC scopes is international. 

        :param scopes: The scopes of this Source.
        :type: list[Scope]
        """

        self._scopes = scopes

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
