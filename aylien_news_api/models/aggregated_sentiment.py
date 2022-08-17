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


class AggregatedSentiment(object):
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
        'positive': 'int',
        'neutral': 'int',
        'negative': 'int'
    }

    attribute_map = {
        'positive': 'positive',
        'neutral': 'neutral',
        'negative': 'negative'
    }

    def __init__(self, positive=None, neutral=None, negative=None, local_vars_configuration=None):  # noqa: E501
        """AggregatedSentiment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._positive = None
        self._neutral = None
        self._negative = None
        self.discriminator = None

        if positive is not None:
            self.positive = positive
        if neutral is not None:
            self.neutral = neutral
        if negative is not None:
            self.negative = negative

    @property
    def positive(self):
        """Gets the positive of this AggregatedSentiment.  # noqa: E501

        Positive sentiments count  # noqa: E501

        :return: The positive of this AggregatedSentiment.  # noqa: E501
        :rtype: int
        """
        return self._positive

    @positive.setter
    def positive(self, positive):
        """Sets the positive of this AggregatedSentiment.

        Positive sentiments count  # noqa: E501

        :param positive: The positive of this AggregatedSentiment.  # noqa: E501
        :type positive: int
        """

        self._positive = positive

    @property
    def neutral(self):
        """Gets the neutral of this AggregatedSentiment.  # noqa: E501

        Neutral sentiments count  # noqa: E501

        :return: The neutral of this AggregatedSentiment.  # noqa: E501
        :rtype: int
        """
        return self._neutral

    @neutral.setter
    def neutral(self, neutral):
        """Sets the neutral of this AggregatedSentiment.

        Neutral sentiments count  # noqa: E501

        :param neutral: The neutral of this AggregatedSentiment.  # noqa: E501
        :type neutral: int
        """

        self._neutral = neutral

    @property
    def negative(self):
        """Gets the negative of this AggregatedSentiment.  # noqa: E501

        Negative sentiments count  # noqa: E501

        :return: The negative of this AggregatedSentiment.  # noqa: E501
        :rtype: int
        """
        return self._negative

    @negative.setter
    def negative(self, negative):
        """Sets the negative of this AggregatedSentiment.

        Negative sentiments count  # noqa: E501

        :param negative: The negative of this AggregatedSentiment.  # noqa: E501
        :type negative: int
        """

        self._negative = negative

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
        if not isinstance(other, AggregatedSentiment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregatedSentiment):
            return True

        return self.to_dict() != other.to_dict()
