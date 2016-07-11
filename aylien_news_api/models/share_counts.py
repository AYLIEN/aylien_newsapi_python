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


class ShareCounts(object):
    def __init__(self, facebook=None, google_plus=None, linkedin=None, reddit=None):
        """
        ShareCounts - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'facebook': 'list[ShareCount]',
            'google_plus': 'list[ShareCount]',
            'linkedin': 'list[ShareCount]',
            'reddit': 'list[ShareCount]'
        }

        self.attribute_map = {
            'facebook': 'facebook',
            'google_plus': 'google_plus',
            'linkedin': 'linkedin',
            'reddit': 'reddit'
        }

        self._facebook = facebook
        self._google_plus = google_plus
        self._linkedin = linkedin
        self._reddit = reddit

    @property
    def facebook(self):
        """
        Gets the facebook of this ShareCounts.
        Facebook shares count

        :return: The facebook of this ShareCounts.
        :rtype: list[ShareCount]
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """
        Sets the facebook of this ShareCounts.
        Facebook shares count

        :param facebook: The facebook of this ShareCounts.
        :type: list[ShareCount]
        """

        self._facebook = facebook

    @property
    def google_plus(self):
        """
        Gets the google_plus of this ShareCounts.
        Google Plus shares count

        :return: The google_plus of this ShareCounts.
        :rtype: list[ShareCount]
        """
        return self._google_plus

    @google_plus.setter
    def google_plus(self, google_plus):
        """
        Sets the google_plus of this ShareCounts.
        Google Plus shares count

        :param google_plus: The google_plus of this ShareCounts.
        :type: list[ShareCount]
        """

        self._google_plus = google_plus

    @property
    def linkedin(self):
        """
        Gets the linkedin of this ShareCounts.
        LinkedIn shares count

        :return: The linkedin of this ShareCounts.
        :rtype: list[ShareCount]
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """
        Sets the linkedin of this ShareCounts.
        LinkedIn shares count

        :param linkedin: The linkedin of this ShareCounts.
        :type: list[ShareCount]
        """

        self._linkedin = linkedin

    @property
    def reddit(self):
        """
        Gets the reddit of this ShareCounts.
        Reddit shares count

        :return: The reddit of this ShareCounts.
        :rtype: list[ShareCount]
        """
        return self._reddit

    @reddit.setter
    def reddit(self, reddit):
        """
        Sets the reddit of this ShareCounts.
        Reddit shares count

        :param reddit: The reddit of this ShareCounts.
        :type: list[ShareCount]
        """

        self._reddit = reddit

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
