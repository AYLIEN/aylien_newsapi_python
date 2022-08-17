# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.2.2
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class ShareCounts(object):
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
        'facebook': 'list[ShareCount]',
        'google_plus': 'list[ShareCount]',
        'linkedin': 'list[ShareCount]',
        'reddit': 'list[ShareCount]'
    }

    attribute_map = {
        'facebook': 'facebook',
        'google_plus': 'google_plus',
        'linkedin': 'linkedin',
        'reddit': 'reddit'
    }

    def __init__(self, facebook=None, google_plus=None, linkedin=None, reddit=None, local_vars_configuration=None):  # noqa: E501
        """ShareCounts - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._facebook = None
        self._google_plus = None
        self._linkedin = None
        self._reddit = None
        self.discriminator = None

        if facebook is not None:
            self.facebook = facebook
        if google_plus is not None:
            self.google_plus = google_plus
        if linkedin is not None:
            self.linkedin = linkedin
        if reddit is not None:
            self.reddit = reddit

    @property
    def facebook(self):
        """Gets the facebook of this ShareCounts.  # noqa: E501

        Facebook shares count  # noqa: E501

        :return: The facebook of this ShareCounts.  # noqa: E501
        :rtype: list[ShareCount]
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """Sets the facebook of this ShareCounts.

        Facebook shares count  # noqa: E501

        :param facebook: The facebook of this ShareCounts.  # noqa: E501
        :type facebook: list[ShareCount]
        """

        self._facebook = facebook

    @property
    def google_plus(self):
        """Gets the google_plus of this ShareCounts.  # noqa: E501

        Google Plus shares count  # noqa: E501

        :return: The google_plus of this ShareCounts.  # noqa: E501
        :rtype: list[ShareCount]
        """
        return self._google_plus

    @google_plus.setter
    def google_plus(self, google_plus):
        """Sets the google_plus of this ShareCounts.

        Google Plus shares count  # noqa: E501

        :param google_plus: The google_plus of this ShareCounts.  # noqa: E501
        :type google_plus: list[ShareCount]
        """

        self._google_plus = google_plus

    @property
    def linkedin(self):
        """Gets the linkedin of this ShareCounts.  # noqa: E501

        LinkedIn shares count  # noqa: E501

        :return: The linkedin of this ShareCounts.  # noqa: E501
        :rtype: list[ShareCount]
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """Sets the linkedin of this ShareCounts.

        LinkedIn shares count  # noqa: E501

        :param linkedin: The linkedin of this ShareCounts.  # noqa: E501
        :type linkedin: list[ShareCount]
        """

        self._linkedin = linkedin

    @property
    def reddit(self):
        """Gets the reddit of this ShareCounts.  # noqa: E501

        Reddit shares count  # noqa: E501

        :return: The reddit of this ShareCounts.  # noqa: E501
        :rtype: list[ShareCount]
        """
        return self._reddit

    @reddit.setter
    def reddit(self, reddit):
        """Sets the reddit of this ShareCounts.

        Reddit shares count  # noqa: E501

        :param reddit: The reddit of this ShareCounts.  # noqa: E501
        :type reddit: list[ShareCount]
        """

        self._reddit = reddit

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
        if not isinstance(other, ShareCounts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ShareCounts):
            return True

        return self.to_dict() != other.to_dict()
