# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 4.7.4
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Source(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'description': 'str',
        'domain': 'str',
        'home_page_url': 'str',
        'id': 'int',
        'links_in_count': 'int',
        'locations': 'list[Location]',
        'logo_url': 'str',
        'name': 'str',
        'rankings': 'Rankings',
        'scopes': 'list[Scope]',
        'title': 'str'
    }

    attribute_map = {
        'description': 'description',
        'domain': 'domain',
        'home_page_url': 'home_page_url',
        'id': 'id',
        'links_in_count': 'links_in_count',
        'locations': 'locations',
        'logo_url': 'logo_url',
        'name': 'name',
        'rankings': 'rankings',
        'scopes': 'scopes',
        'title': 'title'
    }

    def __init__(self, description=None, domain=None, home_page_url=None, id=None, links_in_count=None, locations=None, logo_url=None, name=None, rankings=None, scopes=None, title=None, local_vars_configuration=None):  # noqa: E501
        """Source - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._domain = None
        self._home_page_url = None
        self._id = None
        self._links_in_count = None
        self._locations = None
        self._logo_url = None
        self._name = None
        self._rankings = None
        self._scopes = None
        self._title = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if domain is not None:
            self.domain = domain
        if home_page_url is not None:
            self.home_page_url = home_page_url
        if id is not None:
            self.id = id
        if links_in_count is not None:
            self.links_in_count = links_in_count
        if locations is not None:
            self.locations = locations
        if logo_url is not None:
            self.logo_url = logo_url
        if name is not None:
            self.name = name
        if rankings is not None:
            self.rankings = rankings
        if scopes is not None:
            self.scopes = scopes
        if title is not None:
            self.title = title

    @property
    def description(self):
        """Gets the description of this Source.  # noqa: E501

        A general explanation about the source  # noqa: E501

        :return: The description of this Source.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Source.

        A general explanation about the source  # noqa: E501

        :param description: The description of this Source.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def domain(self):
        """Gets the domain of this Source.  # noqa: E501

        The domain name of the source which is extracted from the source URL  # noqa: E501

        :return: The domain of this Source.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Source.

        The domain name of the source which is extracted from the source URL  # noqa: E501

        :param domain: The domain of this Source.  # noqa: E501
        :type domain: str
        """

        self._domain = domain

    @property
    def home_page_url(self):
        """Gets the home_page_url of this Source.  # noqa: E501

        The home page URL of the source  # noqa: E501

        :return: The home_page_url of this Source.  # noqa: E501
        :rtype: str
        """
        return self._home_page_url

    @home_page_url.setter
    def home_page_url(self, home_page_url):
        """Sets the home_page_url of this Source.

        The home page URL of the source  # noqa: E501

        :param home_page_url: The home_page_url of this Source.  # noqa: E501
        :type home_page_url: str
        """

        self._home_page_url = home_page_url

    @property
    def id(self):
        """Gets the id of this Source.  # noqa: E501

        The source id which is a unique value  # noqa: E501

        :return: The id of this Source.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Source.

        The source id which is a unique value  # noqa: E501

        :param id: The id of this Source.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def links_in_count(self):
        """Gets the links_in_count of this Source.  # noqa: E501

        The number of websites that link to the source  # noqa: E501

        :return: The links_in_count of this Source.  # noqa: E501
        :rtype: int
        """
        return self._links_in_count

    @links_in_count.setter
    def links_in_count(self, links_in_count):
        """Sets the links_in_count of this Source.

        The number of websites that link to the source  # noqa: E501

        :param links_in_count: The links_in_count of this Source.  # noqa: E501
        :type links_in_count: int
        """

        self._links_in_count = links_in_count

    @property
    def locations(self):
        """Gets the locations of this Source.  # noqa: E501

        The source locations which are tend to be the physical locations of the source, e.g. BBC headquarter is located in London.   # noqa: E501

        :return: The locations of this Source.  # noqa: E501
        :rtype: list[Location]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this Source.

        The source locations which are tend to be the physical locations of the source, e.g. BBC headquarter is located in London.   # noqa: E501

        :param locations: The locations of this Source.  # noqa: E501
        :type locations: list[Location]
        """

        self._locations = locations

    @property
    def logo_url(self):
        """Gets the logo_url of this Source.  # noqa: E501

        A URL which points to the source logo  # noqa: E501

        :return: The logo_url of this Source.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Source.

        A URL which points to the source logo  # noqa: E501

        :param logo_url: The logo_url of this Source.  # noqa: E501
        :type logo_url: str
        """

        self._logo_url = logo_url

    @property
    def name(self):
        """Gets the name of this Source.  # noqa: E501

        The source name  # noqa: E501

        :return: The name of this Source.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Source.

        The source name  # noqa: E501

        :param name: The name of this Source.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def rankings(self):
        """Gets the rankings of this Source.  # noqa: E501


        :return: The rankings of this Source.  # noqa: E501
        :rtype: Rankings
        """
        return self._rankings

    @rankings.setter
    def rankings(self, rankings):
        """Sets the rankings of this Source.


        :param rankings: The rankings of this Source.  # noqa: E501
        :type rankings: Rankings
        """

        self._rankings = rankings

    @property
    def scopes(self):
        """Gets the scopes of this Source.  # noqa: E501

        The source scopes which is tend to be scope locations of the source, e.g. BBC scopes is international.   # noqa: E501

        :return: The scopes of this Source.  # noqa: E501
        :rtype: list[Scope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this Source.

        The source scopes which is tend to be scope locations of the source, e.g. BBC scopes is international.   # noqa: E501

        :param scopes: The scopes of this Source.  # noqa: E501
        :type scopes: list[Scope]
        """

        self._scopes = scopes

    @property
    def title(self):
        """Gets the title of this Source.  # noqa: E501

        The title of the home page URL  # noqa: E501

        :return: The title of this Source.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Source.

        The title of the home page URL  # noqa: E501

        :param title: The title of this Source.  # noqa: E501
        :type title: str
        """

        self._title = title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Source):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Source):
            return True

        return self.to_dict() != other.to_dict()
