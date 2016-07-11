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


class Histograms(object):
    def __init__(self, intervals=None, interval_start=None, interval_end=None, interval_width=None, field=None):
        """
        Histograms - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'intervals': 'list[HistogramInterval]',
            'interval_start': 'int',
            'interval_end': 'int',
            'interval_width': 'int',
            'field': 'str'
        }

        self.attribute_map = {
            'intervals': 'intervals',
            'interval_start': 'interval.start',
            'interval_end': 'interval.end',
            'interval_width': 'interval.width',
            'field': 'field'
        }

        self._intervals = intervals
        self._interval_start = interval_start
        self._interval_end = interval_end
        self._interval_width = interval_width
        self._field = field

    @property
    def intervals(self):
        """
        Gets the intervals of this Histograms.
        The intervals of the histograms

        :return: The intervals of this Histograms.
        :rtype: list[HistogramInterval]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """
        Sets the intervals of this Histograms.
        The intervals of the histograms

        :param intervals: The intervals of this Histograms.
        :type: list[HistogramInterval]
        """

        self._intervals = intervals

    @property
    def interval_start(self):
        """
        Gets the interval_start of this Histograms.
        The start interval of the histogram

        :return: The interval_start of this Histograms.
        :rtype: int
        """
        return self._interval_start

    @interval_start.setter
    def interval_start(self, interval_start):
        """
        Sets the interval_start of this Histograms.
        The start interval of the histogram

        :param interval_start: The interval_start of this Histograms.
        :type: int
        """

        self._interval_start = interval_start

    @property
    def interval_end(self):
        """
        Gets the interval_end of this Histograms.
        The end interval of the histogram

        :return: The interval_end of this Histograms.
        :rtype: int
        """
        return self._interval_end

    @interval_end.setter
    def interval_end(self, interval_end):
        """
        Sets the interval_end of this Histograms.
        The end interval of the histogram

        :param interval_end: The interval_end of this Histograms.
        :type: int
        """

        self._interval_end = interval_end

    @property
    def interval_width(self):
        """
        Gets the interval_width of this Histograms.
        The width of the histogram

        :return: The interval_width of this Histograms.
        :rtype: int
        """
        return self._interval_width

    @interval_width.setter
    def interval_width(self, interval_width):
        """
        Sets the interval_width of this Histograms.
        The width of the histogram

        :param interval_width: The interval_width of this Histograms.
        :type: int
        """

        self._interval_width = interval_width

    @property
    def field(self):
        """
        Gets the field of this Histograms.


        :return: The field of this Histograms.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this Histograms.


        :param field: The field of this Histograms.
        :type: str
        """

        self._field = field

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
