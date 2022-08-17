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


class Autocompletes(object):
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
        'autocompletes': 'list[Autocomplete]'
    }

    attribute_map = {
        'autocompletes': 'autocompletes'
    }

    def __init__(self, autocompletes=None, local_vars_configuration=None):  # noqa: E501
        """Autocompletes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._autocompletes = None
        self.discriminator = None

        if autocompletes is not None:
            self.autocompletes = autocompletes

    @property
    def autocompletes(self):
        """Gets the autocompletes of this Autocompletes.  # noqa: E501

        An array of autocompletes  # noqa: E501

        :return: The autocompletes of this Autocompletes.  # noqa: E501
        :rtype: list[Autocomplete]
        """
        return self._autocompletes

    @autocompletes.setter
    def autocompletes(self, autocompletes):
        """Sets the autocompletes of this Autocompletes.

        An array of autocompletes  # noqa: E501

        :param autocompletes: The autocompletes of this Autocompletes.  # noqa: E501
        :type autocompletes: list[Autocomplete]
        """

        self._autocompletes = autocompletes

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
        if not isinstance(other, Autocompletes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Autocompletes):
            return True

        return self.to_dict() != other.to_dict()
