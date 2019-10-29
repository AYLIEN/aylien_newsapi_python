# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 2.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Rank(object):
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
        'country': 'str',
        'fetched_at': 'datetime',
        'rank': 'int'
    }

    attribute_map = {
        'country': 'country',
        'fetched_at': 'fetched_at',
        'rank': 'rank'
    }

    def __init__(self, country=None, fetched_at=None, rank=None):  # noqa: E501
        """Rank - a model defined in OpenAPI"""  # noqa: E501

        self._country = None
        self._fetched_at = None
        self._rank = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if fetched_at is not None:
            self.fetched_at = fetched_at
        if rank is not None:
            self.rank = rank

    @property
    def country(self):
        """Gets the country of this Rank.  # noqa: E501

        The country code which the rank is in it  # noqa: E501

        :return: The country of this Rank.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Rank.

        The country code which the rank is in it  # noqa: E501

        :param country: The country of this Rank.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def fetched_at(self):
        """Gets the fetched_at of this Rank.  # noqa: E501

        The fetched date of the rank  # noqa: E501

        :return: The fetched_at of this Rank.  # noqa: E501
        :rtype: datetime
        """
        return self._fetched_at

    @fetched_at.setter
    def fetched_at(self, fetched_at):
        """Sets the fetched_at of this Rank.

        The fetched date of the rank  # noqa: E501

        :param fetched_at: The fetched_at of this Rank.  # noqa: E501
        :type: datetime
        """

        self._fetched_at = fetched_at

    @property
    def rank(self):
        """Gets the rank of this Rank.  # noqa: E501

        The rank  # noqa: E501

        :return: The rank of this Rank.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this Rank.

        The rank  # noqa: E501

        :param rank: The rank of this Rank.  # noqa: E501
        :type: int
        """

        self._rank = rank

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
        if not isinstance(other, Rank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
