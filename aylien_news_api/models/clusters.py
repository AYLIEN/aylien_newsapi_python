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


class Clusters(object):
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
        'cluster_count': 'int',
        'clusters': 'list[Cluster]',
        'next_page_cursor': 'str'
    }

    attribute_map = {
        'cluster_count': 'cluster_count',
        'clusters': 'clusters',
        'next_page_cursor': 'next_page_cursor'
    }

    def __init__(self, cluster_count=None, clusters=None, next_page_cursor=None, local_vars_configuration=None):  # noqa: E501
        """Clusters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_count = None
        self._clusters = None
        self._next_page_cursor = None
        self.discriminator = None

        if cluster_count is not None:
            self.cluster_count = cluster_count
        if clusters is not None:
            self.clusters = clusters
        if next_page_cursor is not None:
            self.next_page_cursor = next_page_cursor

    @property
    def cluster_count(self):
        """Gets the cluster_count of this Clusters.  # noqa: E501

        The total number of clusters  # noqa: E501

        :return: The cluster_count of this Clusters.  # noqa: E501
        :rtype: int
        """
        return self._cluster_count

    @cluster_count.setter
    def cluster_count(self, cluster_count):
        """Sets the cluster_count of this Clusters.

        The total number of clusters  # noqa: E501

        :param cluster_count: The cluster_count of this Clusters.  # noqa: E501
        :type cluster_count: int
        """

        self._cluster_count = cluster_count

    @property
    def clusters(self):
        """Gets the clusters of this Clusters.  # noqa: E501

        An array of clusters  # noqa: E501

        :return: The clusters of this Clusters.  # noqa: E501
        :rtype: list[Cluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this Clusters.

        An array of clusters  # noqa: E501

        :param clusters: The clusters of this Clusters.  # noqa: E501
        :type clusters: list[Cluster]
        """

        self._clusters = clusters

    @property
    def next_page_cursor(self):
        """Gets the next_page_cursor of this Clusters.  # noqa: E501

        The next page cursor  # noqa: E501

        :return: The next_page_cursor of this Clusters.  # noqa: E501
        :rtype: str
        """
        return self._next_page_cursor

    @next_page_cursor.setter
    def next_page_cursor(self, next_page_cursor):
        """Sets the next_page_cursor of this Clusters.

        The next page cursor  # noqa: E501

        :param next_page_cursor: The next_page_cursor of this Clusters.  # noqa: E501
        :type next_page_cursor: str
        """

        self._next_page_cursor = next_page_cursor

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
        if not isinstance(other, Clusters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Clusters):
            return True

        return self.to_dict() != other.to_dict()
