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


class Trends(object):
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
        'field': 'str',
        'trends': 'list[Trend]',
        'published_at_end': 'datetime',
        'published_at_start': 'datetime'
    }

    attribute_map = {
        'field': 'field',
        'trends': 'trends',
        'published_at_end': 'published_at.end',
        'published_at_start': 'published_at.start'
    }

    def __init__(self, field=None, trends=None, published_at_end=None, published_at_start=None, local_vars_configuration=None):  # noqa: E501
        """Trends - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._trends = None
        self._published_at_end = None
        self._published_at_start = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if trends is not None:
            self.trends = trends
        if published_at_end is not None:
            self.published_at_end = published_at_end
        if published_at_start is not None:
            self.published_at_start = published_at_start

    @property
    def field(self):
        """Gets the field of this Trends.  # noqa: E501

        The field of trends  # noqa: E501

        :return: The field of this Trends.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Trends.

        The field of trends  # noqa: E501

        :param field: The field of this Trends.  # noqa: E501
        :type field: str
        """

        self._field = field

    @property
    def trends(self):
        """Gets the trends of this Trends.  # noqa: E501

        An array of trends  # noqa: E501

        :return: The trends of this Trends.  # noqa: E501
        :rtype: list[Trend]
        """
        return self._trends

    @trends.setter
    def trends(self, trends):
        """Sets the trends of this Trends.

        An array of trends  # noqa: E501

        :param trends: The trends of this Trends.  # noqa: E501
        :type trends: list[Trend]
        """

        self._trends = trends

    @property
    def published_at_end(self):
        """Gets the published_at_end of this Trends.  # noqa: E501

        The end of a period in which searched stories were published  # noqa: E501

        :return: The published_at_end of this Trends.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at_end

    @published_at_end.setter
    def published_at_end(self, published_at_end):
        """Sets the published_at_end of this Trends.

        The end of a period in which searched stories were published  # noqa: E501

        :param published_at_end: The published_at_end of this Trends.  # noqa: E501
        :type published_at_end: datetime
        """

        self._published_at_end = published_at_end

    @property
    def published_at_start(self):
        """Gets the published_at_start of this Trends.  # noqa: E501

        The start of a period in which searched stories were published  # noqa: E501

        :return: The published_at_start of this Trends.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at_start

    @published_at_start.setter
    def published_at_start(self, published_at_start):
        """Sets the published_at_start of this Trends.

        The start of a period in which searched stories were published  # noqa: E501

        :param published_at_start: The published_at_start of this Trends.  # noqa: E501
        :type published_at_start: datetime
        """

        self._published_at_start = published_at_start

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
        if not isinstance(other, Trends):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trends):
            return True

        return self.to_dict() != other.to_dict()
