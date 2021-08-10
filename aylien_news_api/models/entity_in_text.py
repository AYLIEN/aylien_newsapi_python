# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class EntityInText(object):
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
        'sentiment': 'EntitySentiment',
        'surface_forms': 'list[EntitySurfaceForm]'
    }

    attribute_map = {
        'sentiment': 'sentiment',
        'surface_forms': 'surface_forms'
    }

    def __init__(self, sentiment=None, surface_forms=None, local_vars_configuration=None):  # noqa: E501
        """EntityInText - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sentiment = None
        self._surface_forms = None
        self.discriminator = None

        if sentiment is not None:
            self.sentiment = sentiment
        if surface_forms is not None:
            self.surface_forms = surface_forms

    @property
    def sentiment(self):
        """Gets the sentiment of this EntityInText.  # noqa: E501


        :return: The sentiment of this EntityInText.  # noqa: E501
        :rtype: EntitySentiment
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """Sets the sentiment of this EntityInText.


        :param sentiment: The sentiment of this EntityInText.  # noqa: E501
        :type sentiment: EntitySentiment
        """

        self._sentiment = sentiment

    @property
    def surface_forms(self):
        """Gets the surface_forms of this EntityInText.  # noqa: E501


        :return: The surface_forms of this EntityInText.  # noqa: E501
        :rtype: list[EntitySurfaceForm]
        """
        return self._surface_forms

    @surface_forms.setter
    def surface_forms(self, surface_forms):
        """Sets the surface_forms of this EntityInText.


        :param surface_forms: The surface_forms of this EntityInText.  # noqa: E501
        :type surface_forms: list[EntitySurfaceForm]
        """

        self._surface_forms = surface_forms

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
        if not isinstance(other, EntityInText):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntityInText):
            return True

        return self.to_dict() != other.to_dict()
