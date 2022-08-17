# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 4.7.2
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class ShareCount(object):
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
        'count': 'int',
        'fetched_at': 'datetime'
    }

    attribute_map = {
        'count': 'count',
        'fetched_at': 'fetched_at'
    }

    def __init__(self, count=None, fetched_at=None, local_vars_configuration=None):  # noqa: E501
        """ShareCount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._fetched_at = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if fetched_at is not None:
            self.fetched_at = fetched_at

    @property
    def count(self):
        """Gets the count of this ShareCount.  # noqa: E501

        The number of shares  # noqa: E501

        :return: The count of this ShareCount.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShareCount.

        The number of shares  # noqa: E501

        :param count: The count of this ShareCount.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def fetched_at(self):
        """Gets the fetched_at of this ShareCount.  # noqa: E501

        The fetched date of the shares  # noqa: E501

        :return: The fetched_at of this ShareCount.  # noqa: E501
        :rtype: datetime
        """
        return self._fetched_at

    @fetched_at.setter
    def fetched_at(self, fetched_at):
        """Sets the fetched_at of this ShareCount.

        The fetched date of the shares  # noqa: E501

        :param fetched_at: The fetched_at of this ShareCount.  # noqa: E501
        :type fetched_at: datetime
        """

        self._fetched_at = fetched_at

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
        if not isinstance(other, ShareCount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShareCount):
            return True

        return self.to_dict() != other.to_dict()
