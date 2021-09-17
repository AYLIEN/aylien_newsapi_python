# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Query(object):
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
        'eq': 'OneOfstringnumber',
        'text': 'OneOfstringnumber',
        '_in': 'list[OneOfstringnumber]',
        'gt': 'float',
        'gte': 'float',
        'lt': 'float',
        'lte': 'float',
        'boost': 'float'
    }

    attribute_map = {
        'eq': '$eq',
        'text': '$text',
        '_in': '$in',
        'gt': '$gt',
        'gte': '$gte',
        'lt': '$lt',
        'lte': '$lte',
        'boost': '$boost'
    }

    def __init__(self, eq=None, text=None, _in=None, gt=None, gte=None, lt=None, lte=None, boost=None, local_vars_configuration=None):  # noqa: E501
        """Query - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._eq = None
        self._text = None
        self.__in = None
        self._gt = None
        self._gte = None
        self._lt = None
        self._lte = None
        self._boost = None
        self.discriminator = None

        if eq is not None:
            self.eq = eq
        if text is not None:
            self.text = text
        if _in is not None:
            self._in = _in
        if gt is not None:
            self.gt = gt
        if gte is not None:
            self.gte = gte
        if lt is not None:
            self.lt = lt
        if lte is not None:
            self.lte = lte
        if boost is not None:
            self.boost = boost

    @property
    def eq(self):
        """Gets the eq of this Query.  # noqa: E501


        :return: The eq of this Query.  # noqa: E501
        :rtype: OneOfstringnumber
        """
        return self._eq

    @eq.setter
    def eq(self, eq):
        """Sets the eq of this Query.


        :param eq: The eq of this Query.  # noqa: E501
        :type eq: OneOfstringnumber
        """

        self._eq = eq

    @property
    def text(self):
        """Gets the text of this Query.  # noqa: E501


        :return: The text of this Query.  # noqa: E501
        :rtype: OneOfstringnumber
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Query.


        :param text: The text of this Query.  # noqa: E501
        :type text: OneOfstringnumber
        """

        self._text = text

    @property
    def _in(self):
        """Gets the _in of this Query.  # noqa: E501


        :return: The _in of this Query.  # noqa: E501
        :rtype: list[OneOfstringnumber]
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this Query.


        :param _in: The _in of this Query.  # noqa: E501
        :type _in: list[OneOfstringnumber]
        """

        self.__in = _in

    @property
    def gt(self):
        """Gets the gt of this Query.  # noqa: E501


        :return: The gt of this Query.  # noqa: E501
        :rtype: float
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """Sets the gt of this Query.


        :param gt: The gt of this Query.  # noqa: E501
        :type gt: float
        """

        self._gt = gt

    @property
    def gte(self):
        """Gets the gte of this Query.  # noqa: E501


        :return: The gte of this Query.  # noqa: E501
        :rtype: float
        """
        return self._gte

    @gte.setter
    def gte(self, gte):
        """Sets the gte of this Query.


        :param gte: The gte of this Query.  # noqa: E501
        :type gte: float
        """

        self._gte = gte

    @property
    def lt(self):
        """Gets the lt of this Query.  # noqa: E501


        :return: The lt of this Query.  # noqa: E501
        :rtype: float
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this Query.


        :param lt: The lt of this Query.  # noqa: E501
        :type lt: float
        """

        self._lt = lt

    @property
    def lte(self):
        """Gets the lte of this Query.  # noqa: E501


        :return: The lte of this Query.  # noqa: E501
        :rtype: float
        """
        return self._lte

    @lte.setter
    def lte(self, lte):
        """Sets the lte of this Query.


        :param lte: The lte of this Query.  # noqa: E501
        :type lte: float
        """

        self._lte = lte

    @property
    def boost(self):
        """Gets the boost of this Query.  # noqa: E501


        :return: The boost of this Query.  # noqa: E501
        :rtype: float
        """
        return self._boost

    @boost.setter
    def boost(self, boost):
        """Sets the boost of this Query.


        :param boost: The boost of this Query.  # noqa: E501
        :type boost: float
        """

        self._boost = boost

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
        if not isinstance(other, Query):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Query):
            return True

        return self.to_dict() != other.to_dict()
