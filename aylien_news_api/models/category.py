# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Category(object):
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
        'confident': 'bool',
        'id': 'str',
        'label': 'str',
        'level': 'int',
        'links': 'CategoryLinks',
        'score': 'float',
        'taxonomy': 'CategoryTaxonomy'
    }

    attribute_map = {
        'confident': 'confident',
        'id': 'id',
        'label': 'label',
        'level': 'level',
        'links': 'links',
        'score': 'score',
        'taxonomy': 'taxonomy'
    }

    def __init__(self, confident=None, id=None, label=None, level=None, links=None, score=None, taxonomy=None, local_vars_configuration=None):  # noqa: E501
        """Category - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._confident = None
        self._id = None
        self._label = None
        self._level = None
        self._links = None
        self._score = None
        self._taxonomy = None
        self.discriminator = None

        if confident is not None:
            self.confident = confident
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if level is not None:
            self.level = level
        if links is not None:
            self.links = links
        if score is not None:
            self.score = score
        if taxonomy is not None:
            self.taxonomy = taxonomy

    @property
    def confident(self):
        """Gets the confident of this Category.  # noqa: E501

        It defines whether the extracted category is confident or not  # noqa: E501

        :return: The confident of this Category.  # noqa: E501
        :rtype: bool
        """
        return self._confident

    @confident.setter
    def confident(self, confident):
        """Sets the confident of this Category.

        It defines whether the extracted category is confident or not  # noqa: E501

        :param confident: The confident of this Category.  # noqa: E501
        :type confident: bool
        """

        self._confident = confident

    @property
    def id(self):
        """Gets the id of this Category.  # noqa: E501

        The ID of the category  # noqa: E501

        :return: The id of this Category.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Category.

        The ID of the category  # noqa: E501

        :param id: The id of this Category.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Category.  # noqa: E501

        The label of the category  # noqa: E501

        :return: The label of this Category.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Category.

        The label of the category  # noqa: E501

        :param label: The label of this Category.  # noqa: E501
        :type label: str
        """

        self._label = label

    @property
    def level(self):
        """Gets the level of this Category.  # noqa: E501

        The level of the category  # noqa: E501

        :return: The level of this Category.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Category.

        The level of the category  # noqa: E501

        :param level: The level of this Category.  # noqa: E501
        :type level: int
        """

        self._level = level

    @property
    def links(self):
        """Gets the links of this Category.  # noqa: E501


        :return: The links of this Category.  # noqa: E501
        :rtype: CategoryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Category.


        :param links: The links of this Category.  # noqa: E501
        :type links: CategoryLinks
        """

        self._links = links

    @property
    def score(self):
        """Gets the score of this Category.  # noqa: E501

        The score of the category  # noqa: E501

        :return: The score of this Category.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Category.

        The score of the category  # noqa: E501

        :param score: The score of this Category.  # noqa: E501
        :type score: float
        """

        self._score = score

    @property
    def taxonomy(self):
        """Gets the taxonomy of this Category.  # noqa: E501


        :return: The taxonomy of this Category.  # noqa: E501
        :rtype: CategoryTaxonomy
        """
        return self._taxonomy

    @taxonomy.setter
    def taxonomy(self, taxonomy):
        """Sets the taxonomy of this Category.


        :param taxonomy: The taxonomy of this Category.  # noqa: E501
        :type taxonomy: CategoryTaxonomy
        """

        self._taxonomy = taxonomy

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
        if not isinstance(other, Category):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Category):
            return True

        return self.to_dict() != other.to_dict()
