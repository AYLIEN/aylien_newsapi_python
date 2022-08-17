# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.2
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Trend(object):
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
        'value': 'str',
        'sentiment': 'AggregatedSentiment'
    }

    attribute_map = {
        'count': 'count',
        'value': 'value',
        'sentiment': 'sentiment'
    }

    def __init__(self, count=None, value=None, sentiment=None, local_vars_configuration=None):  # noqa: E501
        """Trend - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._value = None
        self._sentiment = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if value is not None:
            self.value = value
        if sentiment is not None:
            self.sentiment = sentiment

    @property
    def count(self):
        """Gets the count of this Trend.  # noqa: E501

        The count of the trend  # noqa: E501

        :return: The count of this Trend.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Trend.

        The count of the trend  # noqa: E501

        :param count: The count of this Trend.  # noqa: E501
        :type count: int
        """

        self._count = count

    @property
    def value(self):
        """Gets the value of this Trend.  # noqa: E501

        The value of the trend  # noqa: E501

        :return: The value of this Trend.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Trend.

        The value of the trend  # noqa: E501

        :param value: The value of this Trend.  # noqa: E501
        :type value: str
        """

        self._value = value

    @property
    def sentiment(self):
        """Gets the sentiment of this Trend.  # noqa: E501


        :return: The sentiment of this Trend.  # noqa: E501
        :rtype: AggregatedSentiment
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this Trend.


        :param sentiment: The sentiment of this Trend.  # noqa: E501
        :type sentiment: AggregatedSentiment
        """

        self._sentiment = sentiment

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
        if not isinstance(other, Trend):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trend):
            return True

        return self.to_dict() != other.to_dict()
