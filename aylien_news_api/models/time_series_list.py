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


class TimeSeriesList(object):
    def __init__(self, time_series=None, period=None, published_at_start=None, published_at_end=None):
        """
        TimeSeriesList - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'time_series': 'list[TimeSeries]',
            'period': 'str',
            'published_at_start': 'datetime',
            'published_at_end': 'datetime'
        }

        self.attribute_map = {
            'time_series': 'time_series',
            'period': 'period',
            'published_at_start': 'published_at.start',
            'published_at_end': 'published_at.end'
        }

        self._time_series = time_series
        self._period = period
        self._published_at_start = published_at_start
        self._published_at_end = published_at_end

    @property
    def time_series(self):
        """
        Gets the time_series of this TimeSeriesList.
        An array of time series

        :return: The time_series of this TimeSeriesList.
        :rtype: list[TimeSeries]
        """
        return self._time_series

    @time_series.setter
    def time_series(self, time_series):
        """
        Sets the time_series of this TimeSeriesList.
        An array of time series

        :param time_series: The time_series of this TimeSeriesList.
        :type: list[TimeSeries]
        """

        self._time_series = time_series

    @property
    def period(self):
        """
        Gets the period of this TimeSeriesList.
        The size of each date range expressed as an interval to be added to the lower bound.

        :return: The period of this TimeSeriesList.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this TimeSeriesList.
        The size of each date range expressed as an interval to be added to the lower bound.

        :param period: The period of this TimeSeriesList.
        :type: str
        """

        self._period = period

    @property
    def published_at_start(self):
        """
        Gets the published_at_start of this TimeSeriesList.
        The start published date of the time series

        :return: The published_at_start of this TimeSeriesList.
        :rtype: datetime
        """
        return self._published_at_start

    @published_at_start.setter
    def published_at_start(self, published_at_start):
        """
        Sets the published_at_start of this TimeSeriesList.
        The start published date of the time series

        :param published_at_start: The published_at_start of this TimeSeriesList.
        :type: datetime
        """

        self._published_at_start = published_at_start

    @property
    def published_at_end(self):
        """
        Gets the published_at_end of this TimeSeriesList.
        The end published date of the time series

        :return: The published_at_end of this TimeSeriesList.
        :rtype: datetime
        """
        return self._published_at_end

    @published_at_end.setter
    def published_at_end(self, published_at_end):
        """
        Sets the published_at_end of this TimeSeriesList.
        The end published date of the time series

        :param published_at_end: The published_at_end of this TimeSeriesList.
        :type: datetime
        """

        self._published_at_end = published_at_end

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
