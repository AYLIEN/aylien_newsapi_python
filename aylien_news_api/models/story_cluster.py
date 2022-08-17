# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.1
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class StoryCluster(object):
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
        'id': 'int',
        'phrases': 'list[str]',
        'score': 'float',
        'size': 'int',
        'stories': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'phrases': 'phrases',
        'score': 'score',
        'size': 'size',
        'stories': 'stories'
    }

    def __init__(self, id=None, phrases=None, score=None, size=None, stories=None, local_vars_configuration=None):  # noqa: E501
        """StoryCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._phrases = None
        self._score = None
        self._size = None
        self._stories = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if phrases is not None:
            self.phrases = phrases
        if score is not None:
            self.score = score
        if size is not None:
            self.size = size
        if stories is not None:
            self.stories = stories

    @property
    def id(self):
        """Gets the id of this StoryCluster.  # noqa: E501

        A unique identification for the cluster  # noqa: E501

        :return: The id of this StoryCluster.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoryCluster.

        A unique identification for the cluster  # noqa: E501

        :param id: The id of this StoryCluster.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def phrases(self):
        """Gets the phrases of this StoryCluster.  # noqa: E501

        Suggested labels for the cluster  # noqa: E501

        :return: The phrases of this StoryCluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._phrases

    @phrases.setter
    def phrases(self, phrases):
        """Sets the phrases of this StoryCluster.

        Suggested labels for the cluster  # noqa: E501

        :param phrases: The phrases of this StoryCluster.  # noqa: E501
        :type phrases: list[str]
        """

        self._phrases = phrases

    @property
    def score(self):
        """Gets the score of this StoryCluster.  # noqa: E501

        The cluster score  # noqa: E501

        :return: The score of this StoryCluster.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this StoryCluster.

        The cluster score  # noqa: E501

        :param score: The score of this StoryCluster.  # noqa: E501
        :type score: float
        """

        self._score = score

    @property
    def size(self):
        """Gets the size of this StoryCluster.  # noqa: E501

        Size of the cluster  # noqa: E501

        :return: The size of this StoryCluster.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this StoryCluster.

        Size of the cluster  # noqa: E501

        :param size: The size of this StoryCluster.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def stories(self):
        """Gets the stories of this StoryCluster.  # noqa: E501

        Story ids which are in the cluster  # noqa: E501

        :return: The stories of this StoryCluster.  # noqa: E501
        :rtype: list[int]
        """
        return self._stories

    @stories.setter
    def stories(self, stories):
        """Sets the stories of this StoryCluster.

        Story ids which are in the cluster  # noqa: E501

        :param stories: The stories of this StoryCluster.  # noqa: E501
        :type stories: list[int]
        """

        self._stories = stories

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
        if not isinstance(other, StoryCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StoryCluster):
            return True

        return self.to_dict() != other.to_dict()
