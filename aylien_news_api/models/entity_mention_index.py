# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class EntityMentionIndex(object):
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
        'start': 'int',
        'end': 'int'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, start=None, end=None, local_vars_configuration=None):  # noqa: E501
        """EntityMentionIndex - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start = None
        self._end = None
        self.discriminator = None

        self.start = start
        self.end = end

    @property
    def start(self):
        """Gets the start of this EntityMentionIndex.  # noqa: E501

        Start index of a single entity mention in the text (counting from 0)  # noqa: E501

        :return: The start of this EntityMentionIndex.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this EntityMentionIndex.

        Start index of a single entity mention in the text (counting from 0)  # noqa: E501

        :param start: The start of this EntityMentionIndex.  # noqa: E501
        :type start: int
        """
        if self.local_vars_configuration.client_side_validation and start is None:  # noqa: E501
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                start is not None and start < 0):  # noqa: E501
            raise ValueError("Invalid value for `start`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this EntityMentionIndex.  # noqa: E501

        End index of a single entity mention in the text (counting from 0)  # noqa: E501

        :return: The end of this EntityMentionIndex.  # noqa: E501
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this EntityMentionIndex.

        End index of a single entity mention in the text (counting from 0)  # noqa: E501

        :param end: The end of this EntityMentionIndex.  # noqa: E501
        :type end: int
        """
        if self.local_vars_configuration.client_side_validation and end is None:  # noqa: E501
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                end is not None and end < 1):  # noqa: E501
            raise ValueError("Invalid value for `end`, must be a value greater than or equal to `1`")  # noqa: E501

        self._end = end

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
        if not isinstance(other, EntityMentionIndex):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityMentionIndex):
            return True

        return self.to_dict() != other.to_dict()
