# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.3
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class EntityLinks(object):
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
        'dbpedia': 'str',
        'wikipedia': 'str',
        'wikidata': 'str'
    }

    attribute_map = {
        'dbpedia': 'dbpedia',
        'wikipedia': 'wikipedia',
        'wikidata': 'wikidata'
    }

    def __init__(self, dbpedia=None, wikipedia=None, wikidata=None, local_vars_configuration=None):  # noqa: E501
        """EntityLinks - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dbpedia = None
        self._wikipedia = None
        self._wikidata = None
        self.discriminator = None

        if dbpedia is not None:
            self.dbpedia = dbpedia
        if wikipedia is not None:
            self.wikipedia = wikipedia
        if wikidata is not None:
            self.wikidata = wikidata

    @property
    def dbpedia(self):
        """Gets the dbpedia of this EntityLinks.  # noqa: E501

        A dbpedia resource URL (deprecated)  # noqa: E501

        :return: The dbpedia of this EntityLinks.  # noqa: E501
        :rtype: str
        """
        return self._dbpedia

    @dbpedia.setter
    def dbpedia(self, dbpedia):
        """Sets the dbpedia of this EntityLinks.

        A dbpedia resource URL (deprecated)  # noqa: E501

        :param dbpedia: The dbpedia of this EntityLinks.  # noqa: E501
        :type dbpedia: str
        """

        self._dbpedia = dbpedia

    @property
    def wikipedia(self):
        """Gets the wikipedia of this EntityLinks.  # noqa: E501

        A wikipedia resource URL  # noqa: E501

        :return: The wikipedia of this EntityLinks.  # noqa: E501
        :rtype: str
        """
        return self._wikipedia

    @wikipedia.setter
    def wikipedia(self, wikipedia):
        """Sets the wikipedia of this EntityLinks.

        A wikipedia resource URL  # noqa: E501

        :param wikipedia: The wikipedia of this EntityLinks.  # noqa: E501
        :type wikipedia: str
        """

        self._wikipedia = wikipedia

    @property
    def wikidata(self):
        """Gets the wikidata of this EntityLinks.  # noqa: E501

        A wikidata resource URL  # noqa: E501

        :return: The wikidata of this EntityLinks.  # noqa: E501
        :rtype: str
        """
        return self._wikidata

    @wikidata.setter
    def wikidata(self, wikidata):
        """Sets the wikidata of this EntityLinks.

        A wikidata resource URL  # noqa: E501

        :param wikidata: The wikidata of this EntityLinks.  # noqa: E501
        :type wikidata: str
        """

        self._wikidata = wikidata

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
        if not isinstance(other, EntityLinks):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityLinks):
            return True

        return self.to_dict() != other.to_dict()
