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


class Sentiment(object):
    def __init__(self, polarity=None, score=None):
        """
        Sentiment - a model defined in News API

        :param dict apiTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.api_types = {
            'polarity': 'str',
            'score': 'float'
        }

        self.attribute_map = {
            'polarity': 'polarity',
            'score': 'score'
        }

        self._polarity = polarity
        self._score = score

    @property
    def polarity(self):
        """
        Gets the polarity of this Sentiment.
        Polarity of the sentiment

        :return: The polarity of this Sentiment.
        :rtype: str
        """
        return self._polarity

    @polarity.setter
    def polarity(self, polarity):
        """
        Sets the polarity of this Sentiment.
        Polarity of the sentiment

        :param polarity: The polarity of this Sentiment.
        :type: str
        """
        allowed_values = ["positive", "neutral", "negative"]
        if polarity not in allowed_values:
            raise ValueError(
                "Invalid value for `polarity`, must be one of {0}"
                .format(allowed_values)
            )

        self._polarity = polarity

    @property
    def score(self):
        """
        Gets the score of this Sentiment.
        Polarity score of the sentiment

        :return: The score of this Sentiment.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this Sentiment.
        Polarity score of the sentiment

        :param score: The score of this Sentiment.
        :type: float
        """

        if not score:
            raise ValueError("Invalid value for `score`, must not be `None`")
        if score > 1.0:
            raise ValueError("Invalid value for `score`, must be a value less than or equal to `1.0`")
        if score < 0.0:
            raise ValueError("Invalid value for `score`, must be a value greater than or equal to `0.0`")

        self._score = score

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
