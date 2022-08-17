# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.3
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class TimeSeriesList(object):
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
        'period': 'str',
        'published_at_end': 'datetime',
        'published_at_start': 'datetime',
        'time_series': 'list[TimeSeries]'
    }

    attribute_map = {
        'period': 'period',
        'published_at_end': 'published_at.end',
        'published_at_start': 'published_at.start',
        'time_series': 'time_series'
    }

    def __init__(self, period=None, published_at_end=None, published_at_start=None, time_series=None, local_vars_configuration=None):  # noqa: E501
        """TimeSeriesList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._period = None
        self._published_at_end = None
        self._published_at_start = None
        self._time_series = None
        self.discriminator = None

        if period is not None:
            self.period = period
        if published_at_end is not None:
            self.published_at_end = published_at_end
        if published_at_start is not None:
            self.published_at_start = published_at_start
        if time_series is not None:
            self.time_series = time_series

    @property
    def period(self):
        """Gets the period of this TimeSeriesList.  # noqa: E501

        The size of each date range expressed as an interval to be added to the lower bound.   # noqa: E501

        :return: The period of this TimeSeriesList.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this TimeSeriesList.

        The size of each date range expressed as an interval to be added to the lower bound.   # noqa: E501

        :param period: The period of this TimeSeriesList.  # noqa: E501
        :type period: str
        """

        self._period = period

    @property
    def published_at_end(self):
        """Gets the published_at_end of this TimeSeriesList.  # noqa: E501

        The end published date of the time series  # noqa: E501

        :return: The published_at_end of this TimeSeriesList.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at_end

    @published_at_end.setter
    def published_at_end(self, published_at_end):
        """Sets the published_at_end of this TimeSeriesList.

        The end published date of the time series  # noqa: E501

        :param published_at_end: The published_at_end of this TimeSeriesList.  # noqa: E501
        :type published_at_end: datetime
        """

        self._published_at_end = published_at_end

    @property
    def published_at_start(self):
        """Gets the published_at_start of this TimeSeriesList.  # noqa: E501

        The start published date of the time series  # noqa: E501

        :return: The published_at_start of this TimeSeriesList.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at_start

    @published_at_start.setter
    def published_at_start(self, published_at_start):
        """Sets the published_at_start of this TimeSeriesList.

        The start published date of the time series  # noqa: E501

        :param published_at_start: The published_at_start of this TimeSeriesList.  # noqa: E501
        :type published_at_start: datetime
        """

        self._published_at_start = published_at_start

    @property
    def time_series(self):
        """Gets the time_series of this TimeSeriesList.  # noqa: E501

        An array of time series  # noqa: E501

        :return: The time_series of this TimeSeriesList.  # noqa: E501
        :rtype: list[TimeSeries]
        """
        return self._time_series

    @time_series.setter
    def time_series(self, time_series):
        """Sets the time_series of this TimeSeriesList.

        An array of time series  # noqa: E501

        :param time_series: The time_series of this TimeSeriesList.  # noqa: E501
        :type time_series: list[TimeSeries]
        """

        self._time_series = time_series

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
        if not isinstance(other, TimeSeriesList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimeSeriesList):
            return True

        return self.to_dict() != other.to_dict()
