# coding: utf-8

"""
Copyright 2017 Aylien, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class Media(object):
    def __init__(self, type=None, url=None, format=None, content_length=None, width=None, height=None):
        """
        Media - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'type': 'str',
            'url': 'str',
            'format': 'str',
            'content_length': 'int',
            'width': 'int',
            'height': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'url': 'url',
            'format': 'format',
            'content_length': 'content_length',
            'width': 'width',
            'height': 'height'
        }

        self._type = type
        self._url = url
        self._format = format
        self._content_length = content_length
        self._width = width
        self._height = height

    @property
    def type(self):
        """
        Gets the type of this Media.
        The type of media

        :return: The type of this Media.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Media.
        The type of media

        :param type: The type of this Media.
        :type: str
        """
        allowed_values = ["image", "video"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def url(self):
        """
        Gets the url of this Media.
        A URL which points to the media file

        :return: The url of this Media.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Media.
        A URL which points to the media file

        :param url: The url of this Media.
        :type: str
        """

        self._url = url

    @property
    def format(self):
        """
        Gets the format of this Media.
        The format of media

        :return: The format of this Media.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this Media.
        The format of media

        :param format: The format of this Media.
        :type: str
        """
        allowed_values = ["BMP", "GIF", "JPEG", "PNG", "TIFF", "PSD", "ICO", "CUR", "WEBP", "SVG"]
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def content_length(self):
        """
        Gets the content_length of this Media.
        The content length of media

        :return: The content_length of this Media.
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """
        Sets the content_length of this Media.
        The content length of media

        :param content_length: The content_length of this Media.
        :type: int
        """

        self._content_length = content_length

    @property
    def width(self):
        """
        Gets the width of this Media.
        The width of media

        :return: The width of this Media.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this Media.
        The width of media

        :param width: The width of this Media.
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this Media.
        The height of media

        :return: The height of this Media.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this Media.
        The height of media

        :param height: The height of this Media.
        :type: int
        """

        self._height = height

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.api_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Media):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
