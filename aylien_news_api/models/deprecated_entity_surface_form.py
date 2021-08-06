# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 4.6
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class DeprecatedEntitySurfaceForm(object):
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
        'text': 'str',
        'indices': 'list[list[int]]',
        'frequency': 'int'
    }

    attribute_map = {
        'text': 'text',
        'indices': 'indices',
        'frequency': 'frequency'
    }

    def __init__(self, text=None, indices=None, frequency=None, local_vars_configuration=None):  # noqa: E501
        """DeprecatedEntitySurfaceForm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._text = None
        self._indices = None
        self._frequency = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if indices is not None:
            self.indices = indices
        if frequency is not None:
            self.frequency = frequency

    @property
    def text(self):
        """Gets the text of this DeprecatedEntitySurfaceForm.  # noqa: E501

        The entity text  # noqa: E501

        :return: The text of this DeprecatedEntitySurfaceForm.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this DeprecatedEntitySurfaceForm.

        The entity text  # noqa: E501

        :param text: The text of this DeprecatedEntitySurfaceForm.  # noqa: E501
        :type text: str
        """

        self._text = text

    @property
    def indices(self):
        """Gets the indices of this DeprecatedEntitySurfaceForm.  # noqa: E501

        The indices of the entity text  # noqa: E501

        :return: The indices of this DeprecatedEntitySurfaceForm.  # noqa: E501
        :rtype: list[list[int]]
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        """Sets the indices of this DeprecatedEntitySurfaceForm.

        The indices of the entity text  # noqa: E501

        :param indices: The indices of this DeprecatedEntitySurfaceForm.  # noqa: E501
        :type indices: list[list[int]]
        """

        self._indices = indices

    @property
    def frequency(self):
        """Gets the frequency of this DeprecatedEntitySurfaceForm.  # noqa: E501

        Amount of entity surface form mentions in the article  # noqa: E501

        :return: The frequency of this DeprecatedEntitySurfaceForm.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this DeprecatedEntitySurfaceForm.

        Amount of entity surface form mentions in the article  # noqa: E501

        :param frequency: The frequency of this DeprecatedEntitySurfaceForm.  # noqa: E501
        :type frequency: int
        """
        if (self.local_vars_configuration.client_side_validation and
                frequency is not None and frequency < 0):  # noqa: E501
            raise ValueError("Invalid value for `frequency`, must be a value greater than or equal to `0`")  # noqa: E501

        self._frequency = frequency

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
        if not isinstance(other, DeprecatedEntitySurfaceForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeprecatedEntitySurfaceForm):
            return True

        return self.to_dict() != other.to_dict()
