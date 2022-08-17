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


class Media(object):
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
        'content_length': 'int',
        'format': 'MediaFormat',
        'height': 'int',
        'type': 'MediaType',
        'url': 'str',
        'width': 'int'
    }

    attribute_map = {
        'content_length': 'content_length',
        'format': 'format',
        'height': 'height',
        'type': 'type',
        'url': 'url',
        'width': 'width'
    }

    def __init__(self, content_length=None, format=None, height=None, type=None, url=None, width=None, local_vars_configuration=None):  # noqa: E501
        """Media - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content_length = None
        self._format = None
        self._height = None
        self._type = None
        self._url = None
        self._width = None
        self.discriminator = None

        if content_length is not None:
            self.content_length = content_length
        if format is not None:
            self.format = format
        if height is not None:
            self.height = height
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if width is not None:
            self.width = width

    @property
    def content_length(self):
        """Gets the content_length of this Media.  # noqa: E501

        The content length of media  # noqa: E501

        :return: The content_length of this Media.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this Media.

        The content length of media  # noqa: E501

        :param content_length: The content_length of this Media.  # noqa: E501
        :type content_length: int
        """

        self._content_length = content_length

    @property
    def format(self):
        """Gets the format of this Media.  # noqa: E501


        :return: The format of this Media.  # noqa: E501
        :rtype: MediaFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Media.


        :param format: The format of this Media.  # noqa: E501
        :type format: MediaFormat
        """

        self._format = format

    @property
    def height(self):
        """Gets the height of this Media.  # noqa: E501

        The height of media  # noqa: E501

        :return: The height of this Media.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Media.

        The height of media  # noqa: E501

        :param height: The height of this Media.  # noqa: E501
        :type height: int
        """

        self._height = height

    @property
    def type(self):
        """Gets the type of this Media.  # noqa: E501


        :return: The type of this Media.  # noqa: E501
        :rtype: MediaType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Media.


        :param type: The type of this Media.  # noqa: E501
        :type type: MediaType
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this Media.  # noqa: E501

        A URL which points to the media file  # noqa: E501

        :return: The url of this Media.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Media.

        A URL which points to the media file  # noqa: E501

        :param url: The url of this Media.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def width(self):
        """Gets the width of this Media.  # noqa: E501

        The width of media  # noqa: E501

        :return: The width of this Media.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Media.

        The width of media  # noqa: E501

        :param width: The width of this Media.  # noqa: E501
        :type width: int
        """

        self._width = width

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
        if not isinstance(other, Media):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Media):
            return True

        return self.to_dict() != other.to_dict()
