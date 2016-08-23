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
    def __init__(self, id=None, name=None, title=None, description=None, links_in_count=None, home_page_url=None, domain=None, logo_url=None, locations=None, scopes=None, rankings=None):
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
            'title': 'str',
            'description': 'str',
            'links_in_count': 'int',
            'home_page_url': 'str',
            'domain': 'str',
            'logo_url': 'str',
            'locations': 'list[Location]',
            'scopes': 'list[Scope]',
            'rankings': 'Rankings'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'title': 'title',
            'description': 'description',
            'links_in_count': 'links_in_count',
            'home_page_url': 'home_page_url',
            'domain': 'domain',
            'logo_url': 'logo_url',
            'locations': 'locations',
            'scopes': 'scopes',
            'rankings': 'rankings'
        }

        self._id = id
        self._name = name
        self._title = title
        self._description = description
        self._links_in_count = links_in_count
        self._home_page_url = home_page_url
        self._domain = domain
        self._logo_url = logo_url
        self._locations = locations
        self._scopes = scopes
        self._rankings = rankings


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
    def title(self):
        """
        Gets the title of this Source.
        The title of the home page URL

        :return: The title of this Source.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Source.
        The title of the home page URL

        :param title: The title of this Source.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this Source.
        A general explanation about the source

        :return: The description of this Source.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Source.
        A general explanation about the source

        :param description: The description of this Source.
        :type: str
        """

        self._description = description

    @property
    def links_in_count(self):
        """
        Gets the links_in_count of this Source.
        The number of websites that link to the source

        :return: The links_in_count of this Source.
        :rtype: int
        """
        return self._links_in_count

    @links_in_count.setter
    def links_in_count(self, links_in_count):
        """
        Sets the links_in_count of this Source.
        The number of websites that link to the source

        :param links_in_count: The links_in_count of this Source.
        :type: int
        """

        self._links_in_count = links_in_count

    @property
    def home_page_url(self):
        """
        Gets the home_page_url of this Source.
        The home page URL of the source

        :return: The home_page_url of this Source.
        :rtype: str
        """
        return self._home_page_url

    @home_page_url.setter
    def home_page_url(self, home_page_url):
        """
        Sets the home_page_url of this Source.
        The home page URL of the source

        :param home_page_url: The home_page_url of this Source.
        :type: str
        """

        self._home_page_url = home_page_url

    @property
    def domain(self):
        """
        Gets the domain of this Source.
        The domain name of the source which is extracted from the source URL

        :return: The domain of this Source.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this Source.
        The domain name of the source which is extracted from the source URL

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

    @property
    def rankings(self):
        """
        Gets the rankings of this Source.
        The web rankings of the source

        :return: The rankings of this Source.
        :rtype: Rankings
        """
        return self._rankings

    @rankings.setter
    def rankings(self, rankings):
        """
        Sets the rankings of this Source.
        The web rankings of the source

        :param rankings: The rankings of this Source.
        :type: Rankings
        """

        self._rankings = rankings

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
