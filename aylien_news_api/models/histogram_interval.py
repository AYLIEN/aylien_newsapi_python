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


class HistogramInterval(object):
    def __init__(self, bin=None, count=None):
        """
        HistogramInterval - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'bin': 'int',
            'count': 'int'
        }

        self.attribute_map = {
            'bin': 'bin',
            'count': 'count'
        }

        self._bin = bin
        self._count = count

    @property
    def bin(self):
        """
        Gets the bin of this HistogramInterval.
        Histogram bin

        :return: The bin of this HistogramInterval.
        :rtype: int
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """
        Sets the bin of this HistogramInterval.
        Histogram bin

        :param bin: The bin of this HistogramInterval.
        :type: int
        """

        self._bin = bin

    @property
    def count(self):
        """
        Gets the count of this HistogramInterval.
        Histogram bin size

        :return: The count of this HistogramInterval.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this HistogramInterval.
        Histogram bin size

        :param count: The count of this HistogramInterval.
        :type: int
        """

        self._count = count

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
