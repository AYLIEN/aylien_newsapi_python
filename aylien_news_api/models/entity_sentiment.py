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


class EntitySentiment(object):
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
        'polarity': 'SentimentPolarity',
        'confidence': 'float'
    }

    attribute_map = {
        'polarity': 'polarity',
        'confidence': 'confidence'
    }

    def __init__(self, polarity=None, confidence=None, local_vars_configuration=None):  # noqa: E501
        """EntitySentiment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._polarity = None
        self._confidence = None
        self.discriminator = None

        if polarity is not None:
            self.polarity = polarity
        if confidence is not None:
            self.confidence = confidence

    @property
    def polarity(self):
        """Gets the polarity of this EntitySentiment.  # noqa: E501


        :return: The polarity of this EntitySentiment.  # noqa: E501
        :rtype: SentimentPolarity
        """
        return self._polarity

    @polarity.setter
    def polarity(self, polarity):
        """Sets the polarity of this EntitySentiment.


        :param polarity: The polarity of this EntitySentiment.  # noqa: E501
        :type polarity: SentimentPolarity
        """

        self._polarity = polarity

    @property
    def confidence(self):
        """Gets the confidence of this EntitySentiment.  # noqa: E501

        Polarity confidence of the sentiment  # noqa: E501

        :return: The confidence of this EntitySentiment.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this EntitySentiment.

        Polarity confidence of the sentiment  # noqa: E501

        :param confidence: The confidence of this EntitySentiment.  # noqa: E501
        :type confidence: float
        """
        if (self.local_vars_configuration.client_side_validation and
                confidence is not None and confidence > 1):  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                confidence is not None and confidence < 0):  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

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
        if not isinstance(other, EntitySentiment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntitySentiment):
            return True

        return self.to_dict() != other.to_dict()
