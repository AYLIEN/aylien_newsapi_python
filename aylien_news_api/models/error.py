# coding: utf-8

# Copyright 2016 Aylien, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pprint import pformat
from six import iteritems
import re


class Error(object):
    def __init__(self, id=None, links=None, status=None, code=None, title=None, detail=None):
        """
        Error - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'id': 'str',
            'links': 'ErrorLinks',
            'status': 'str',
            'code': 'str',
            'title': 'str',
            'detail': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'links': 'links',
            'status': 'status',
            'code': 'code',
            'title': 'title',
            'detail': 'detail'
        }

        self._id = id
        self._links = links
        self._status = status
        self._code = code
        self._title = title
        self._detail = detail

    @property
    def id(self):
        """
        Gets the id of this Error.


        :return: The id of this Error.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Error.


        :param id: The id of this Error.
        :type: str
        """

        self._id = id

    @property
    def links(self):
        """
        Gets the links of this Error.


        :return: The links of this Error.
        :rtype: ErrorLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Error.


        :param links: The links of this Error.
        :type: ErrorLinks
        """

        self._links = links

    @property
    def status(self):
        """
        Gets the status of this Error.


        :return: The status of this Error.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Error.


        :param status: The status of this Error.
        :type: str
        """

        self._status = status

    @property
    def code(self):
        """
        Gets the code of this Error.


        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Error.


        :param code: The code of this Error.
        :type: str
        """

        self._code = code

    @property
    def title(self):
        """
        Gets the title of this Error.


        :return: The title of this Error.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Error.


        :param title: The title of this Error.
        :type: str
        """

        self._title = title

    @property
    def detail(self):
        """
        Gets the detail of this Error.


        :return: The detail of this Error.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """
        Sets the detail of this Error.


        :param detail: The detail of this Error.
        :type: str
        """

        self._detail = detail

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
