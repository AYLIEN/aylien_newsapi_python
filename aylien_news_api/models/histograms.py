# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 4.7
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Histograms(object):
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
        'field': 'str',
        'interval_end': 'int',
        'interval_start': 'int',
        'interval_width': 'int',
        'intervals': 'list[HistogramInterval]',
        'published_at_end': 'datetime',
        'published_at_start': 'datetime'
    }

    attribute_map = {
        'field': 'field',
        'interval_end': 'interval.end',
        'interval_start': 'interval.start',
        'interval_width': 'interval.width',
        'intervals': 'intervals',
        'published_at_end': 'published_at.end',
        'published_at_start': 'published_at.start'
    }

    def __init__(self, field=None, interval_end=None, interval_start=None, interval_width=None, intervals=None, published_at_end=None, published_at_start=None, local_vars_configuration=None):  # noqa: E501
        """Histograms - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._field = None
        self._interval_end = None
        self._interval_start = None
        self._interval_width = None
        self._intervals = None
        self._published_at_end = None
        self._published_at_start = None
        self.discriminator = None

        if field is not None:
            self.field = field
        if interval_end is not None:
            self.interval_end = interval_end
        if interval_start is not None:
            self.interval_start = interval_start
        if interval_width is not None:
            self.interval_width = interval_width
        if intervals is not None:
            self.intervals = intervals
        if published_at_end is not None:
            self.published_at_end = published_at_end
        if published_at_start is not None:
            self.published_at_start = published_at_start

    @property
    def field(self):
        """Gets the field of this Histograms.  # noqa: E501


        :return: The field of this Histograms.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Histograms.


        :param field: The field of this Histograms.  # noqa: E501
        :type field: str
        """

        self._field = field

    @property
    def interval_end(self):
        """Gets the interval_end of this Histograms.  # noqa: E501

        The end interval of the histogram  # noqa: E501

        :return: The interval_end of this Histograms.  # noqa: E501
        :rtype: int
        """
        return self._interval_end

    @interval_end.setter
    def interval_end(self, interval_end):
        """Sets the interval_end of this Histograms.

        The end interval of the histogram  # noqa: E501

        :param interval_end: The interval_end of this Histograms.  # noqa: E501
        :type interval_end: int
        """

        self._interval_end = interval_end

    @property
    def interval_start(self):
        """Gets the interval_start of this Histograms.  # noqa: E501

        The start interval of the histogram  # noqa: E501

        :return: The interval_start of this Histograms.  # noqa: E501
        :rtype: int
        """
        return self._interval_start

    @interval_start.setter
    def interval_start(self, interval_start):
        """Sets the interval_start of this Histograms.

        The start interval of the histogram  # noqa: E501

        :param interval_start: The interval_start of this Histograms.  # noqa: E501
        :type interval_start: int
        """

        self._interval_start = interval_start

    @property
    def interval_width(self):
        """Gets the interval_width of this Histograms.  # noqa: E501

        The width of the histogram  # noqa: E501

        :return: The interval_width of this Histograms.  # noqa: E501
        :rtype: int
        """
        return self._interval_width

    @interval_width.setter
    def interval_width(self, interval_width):
        """Sets the interval_width of this Histograms.

        The width of the histogram  # noqa: E501

        :param interval_width: The interval_width of this Histograms.  # noqa: E501
        :type interval_width: int
        """

        self._interval_width = interval_width

    @property
    def intervals(self):
        """Gets the intervals of this Histograms.  # noqa: E501

        The intervals of the histograms  # noqa: E501

        :return: The intervals of this Histograms.  # noqa: E501
        :rtype: list[HistogramInterval]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this Histograms.

        The intervals of the histograms  # noqa: E501

        :param intervals: The intervals of this Histograms.  # noqa: E501
        :type intervals: list[HistogramInterval]
        """

        self._intervals = intervals

    @property
    def published_at_end(self):
        """Gets the published_at_end of this Histograms.  # noqa: E501

        The end of a period in which searched stories were published  # noqa: E501

        :return: The published_at_end of this Histograms.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at_end

    @published_at_end.setter
    def published_at_end(self, published_at_end):
        """Sets the published_at_end of this Histograms.

        The end of a period in which searched stories were published  # noqa: E501

        :param published_at_end: The published_at_end of this Histograms.  # noqa: E501
        :type published_at_end: datetime
        """

        self._published_at_end = published_at_end

    @property
    def published_at_start(self):
        """Gets the published_at_start of this Histograms.  # noqa: E501

        The start of a period in which searched stories were published  # noqa: E501

        :return: The published_at_start of this Histograms.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at_start

    @published_at_start.setter
    def published_at_start(self, published_at_start):
        """Sets the published_at_start of this Histograms.

        The start of a period in which searched stories were published  # noqa: E501

        :param published_at_start: The published_at_start of this Histograms.  # noqa: E501
        :type published_at_start: datetime
        """

        self._published_at_start = published_at_start

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
        if not isinstance(other, Histograms):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Histograms):
            return True

        return self.to_dict() != other.to_dict()
