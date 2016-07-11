# coding: utf-8

"""
DefaultApi.py
Copyright 2016 Aylien, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list_autocompletes(self, type, term, **kwargs):
        """
        List autocompletes
        This endpoint is used for getting list of autocompletes by providing a specific term and type.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_autocompletes(type, term, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type: This parameter is used for defining the type of autocompletes. (required)
        :param str term: This parameter is used for finding autocomplete objects that contain the specified value. (required)
        :param str language: This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: Autocompletes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_autocompletes_with_http_info(type, term, **kwargs)
        else:
            (data) = self.list_autocompletes_with_http_info(type, term, **kwargs)
            return data

    def list_autocompletes_with_http_info(self, type, term, **kwargs):
        """
        List autocompletes
        This endpoint is used for getting list of autocompletes by providing a specific term and type.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_autocompletes_with_http_info(type, term, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type: This parameter is used for defining the type of autocompletes. (required)
        :param str term: This parameter is used for finding autocomplete objects that contain the specified value. (required)
        :param str language: This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: Autocompletes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'term', 'language', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_autocompletes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params) or (params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `list_autocompletes`")
        # verify the required parameter 'term' is set
        if ('term' not in params) or (params['term'] is None):
            raise ValueError("Missing the required parameter `term` when calling `list_autocompletes`")

        if 'term' in params and len(params['term']) < 1:
            raise ValueError("Invalid value for parameter `term` when calling `list_autocompletes`, length must be greater than or equal to `1`")
        if 'per_page' in params and params['per_page'] > 100.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_autocompletes`, must be a value less than or equal to  `100.0`")
        if 'per_page' in params and params['per_page'] < 1.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_autocompletes`, must be a value greater than or equal to `1.0`")
        resource_path = '/autocompletes'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
        if 'term' in params:
            query_params['term'] = params['term']
        if 'language' in params:
            query_params['language'] = params['language']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['app_key', 'app_id']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Autocompletes',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_coverages(self, **kwargs):
        """
        List coverages
        This endpoint is used for finding story coverages based on the parameters provided. The maximum number of related stories returned is 100.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_coverages(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param bool cluster: This parameter enables clustering for the returned stories.
        :param str cluster_algorithm: This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms.
        :param list[str] _return: This parameter is used for specifying return fields.
        :param int story_id: A story id
        :param str story_url: An article or webpage
        :param str story_title: Title of the article
        :param str story_body: Body of the article
        :param datetime story_published_at: Publish date of the article. If you use a url or title and body of an article for getting coverages, this parameter is required. The format used is a restricted form of the canonical representation of dateTime in the [XML Schema specification (ISO 8601)](https://www.w3.org/TR/xmlschema-2/#dateTime).
        :param str story_language: This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: Coverages
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_coverages_with_http_info(**kwargs)
        else:
            (data) = self.list_coverages_with_http_info(**kwargs)
            return data

    def list_coverages_with_http_info(self, **kwargs):
        """
        List coverages
        This endpoint is used for finding story coverages based on the parameters provided. The maximum number of related stories returned is 100.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_coverages_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param bool cluster: This parameter enables clustering for the returned stories.
        :param str cluster_algorithm: This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms.
        :param list[str] _return: This parameter is used for specifying return fields.
        :param int story_id: A story id
        :param str story_url: An article or webpage
        :param str story_title: Title of the article
        :param str story_body: Body of the article
        :param datetime story_published_at: Publish date of the article. If you use a url or title and body of an article for getting coverages, this parameter is required. The format used is a restricted form of the canonical representation of dateTime in the [XML Schema specification (ISO 8601)](https://www.w3.org/TR/xmlschema-2/#dateTime).
        :param str story_language: This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: Coverages
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'title', 'body', 'text', 'language', 'published_at_start', 'published_at_end', 'categories_taxonomy', 'categories_confident', 'categories_id', 'categories_level', 'entities_title_text', 'entities_title_type', 'entities_title_links_dbpedia', 'entities_body_text', 'entities_body_type', 'entities_body_links_dbpedia', 'sentiment_title_polarity', 'sentiment_body_polarity', 'media_images_count_min', 'media_images_count_max', 'media_videos_count_min', 'media_videos_count_max', 'author_id', 'author_name', 'source_id', 'source_name', 'source_domain', 'source_locations_country', 'source_locations_state', 'source_locations_city', 'source_scopes_country', 'source_scopes_state', 'source_scopes_city', 'source_scopes_level', 'cluster', 'cluster_algorithm', '_return', 'story_id', 'story_url', 'story_title', 'story_body', 'story_published_at', 'story_language', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_coverages" % key
                )
            params[key] = val
        del params['kwargs']

        if 'media_images_count_min' in params and params['media_images_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_min` when calling `list_coverages`, must be a value greater than or equal to `0.0`")
        if 'media_images_count_max' in params and params['media_images_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_max` when calling `list_coverages`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_min' in params and params['media_videos_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_min` when calling `list_coverages`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_max' in params and params['media_videos_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_max` when calling `list_coverages`, must be a value greater than or equal to `0.0`")
        if 'per_page' in params and params['per_page'] > 100.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_coverages`, must be a value less than or equal to  `100.0`")
        if 'per_page' in params and params['per_page'] < 1.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_coverages`, must be a value greater than or equal to `1.0`")
        resource_path = '/coverages'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id[]', params['id']))
        if 'title' in params:
            form_params.append(('title', params['title']))
        if 'body' in params:
            form_params.append(('body', params['body']))
        if 'text' in params:
            form_params.append(('text', params['text']))
        if 'language' in params:
            form_params.append(('language[]', params['language']))
        if 'published_at_start' in params:
            form_params.append(('published_at.start', params['published_at_start']))
        if 'published_at_end' in params:
            form_params.append(('published_at.end', params['published_at_end']))
        if 'categories_taxonomy' in params:
            form_params.append(('categories.taxonomy', params['categories_taxonomy']))
        if 'categories_confident' in params:
            form_params.append(('categories.confident', params['categories_confident']))
        if 'categories_id' in params:
            form_params.append(('categories.id[]', params['categories_id']))
        if 'categories_level' in params:
            form_params.append(('categories.level[]', params['categories_level']))
        if 'entities_title_text' in params:
            form_params.append(('entities.title.text[]', params['entities_title_text']))
        if 'entities_title_type' in params:
            form_params.append(('entities.title.type[]', params['entities_title_type']))
        if 'entities_title_links_dbpedia' in params:
            form_params.append(('entities.title.links.dbpedia[]', params['entities_title_links_dbpedia']))
        if 'entities_body_text' in params:
            form_params.append(('entities.body.text[]', params['entities_body_text']))
        if 'entities_body_type' in params:
            form_params.append(('entities.body.type[]', params['entities_body_type']))
        if 'entities_body_links_dbpedia' in params:
            form_params.append(('entities.body.links.dbpedia[]', params['entities_body_links_dbpedia']))
        if 'sentiment_title_polarity' in params:
            form_params.append(('sentiment.title.polarity', params['sentiment_title_polarity']))
        if 'sentiment_body_polarity' in params:
            form_params.append(('sentiment.body.polarity', params['sentiment_body_polarity']))
        if 'media_images_count_min' in params:
            form_params.append(('media.images.count.min', params['media_images_count_min']))
        if 'media_images_count_max' in params:
            form_params.append(('media.images.count.max', params['media_images_count_max']))
        if 'media_videos_count_min' in params:
            form_params.append(('media.videos.count.min', params['media_videos_count_min']))
        if 'media_videos_count_max' in params:
            form_params.append(('media.videos.count.max', params['media_videos_count_max']))
        if 'author_id' in params:
            form_params.append(('author.id[]', params['author_id']))
        if 'author_name' in params:
            form_params.append(('author.name', params['author_name']))
        if 'source_id' in params:
            form_params.append(('source.id[]', params['source_id']))
        if 'source_name' in params:
            form_params.append(('source.name[]', params['source_name']))
        if 'source_domain' in params:
            form_params.append(('source.domain[]', params['source_domain']))
        if 'source_locations_country' in params:
            form_params.append(('source.locations.country[]', params['source_locations_country']))
        if 'source_locations_state' in params:
            form_params.append(('source.locations.state[]', params['source_locations_state']))
        if 'source_locations_city' in params:
            form_params.append(('source.locations.city[]', params['source_locations_city']))
        if 'source_scopes_country' in params:
            form_params.append(('source.scopes.country[]', params['source_scopes_country']))
        if 'source_scopes_state' in params:
            form_params.append(('source.scopes.state[]', params['source_scopes_state']))
        if 'source_scopes_city' in params:
            form_params.append(('source.scopes.city[]', params['source_scopes_city']))
        if 'source_scopes_level' in params:
            form_params.append(('source.scopes.level[]', params['source_scopes_level']))
        if 'cluster' in params:
            form_params.append(('cluster', params['cluster']))
        if 'cluster_algorithm' in params:
            form_params.append(('cluster.algorithm', params['cluster_algorithm']))
        if '_return' in params:
            form_params.append(('return[]', params['_return']))
        if 'story_id' in params:
            form_params.append(('story_id', params['story_id']))
        if 'story_url' in params:
            form_params.append(('story_url', params['story_url']))
        if 'story_title' in params:
            form_params.append(('story_title', params['story_title']))
        if 'story_body' in params:
            form_params.append(('story_body', params['story_body']))
        if 'story_published_at' in params:
            form_params.append(('story_published_at', params['story_published_at']))
        if 'story_language' in params:
            form_params.append(('story_language', params['story_language']))
        if 'per_page' in params:
            form_params.append(('per_page', params['per_page']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['app_key', 'app_id']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Coverages',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_histograms(self, **kwargs):
        """
        List histograms
        This endpoint is used for getting histograms based on the `field` parameter passed to the API.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_histograms(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param int interval_start: This parameter is used for setting the start data point of histogram intervals.
        :param int interval_end: This parameter is used for setting the end data point of histogram intervals.
        :param int interval_width: This parameter is used for setting the width of histogram intervals.
        :param str field: This parameter is used for specifying the y-axis variable for the histogram.
        :return: Histograms
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_histograms_with_http_info(**kwargs)
        else:
            (data) = self.list_histograms_with_http_info(**kwargs)
            return data

    def list_histograms_with_http_info(self, **kwargs):
        """
        List histograms
        This endpoint is used for getting histograms based on the `field` parameter passed to the API.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_histograms_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param int interval_start: This parameter is used for setting the start data point of histogram intervals.
        :param int interval_end: This parameter is used for setting the end data point of histogram intervals.
        :param int interval_width: This parameter is used for setting the width of histogram intervals.
        :param str field: This parameter is used for specifying the y-axis variable for the histogram.
        :return: Histograms
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'title', 'body', 'text', 'language', 'published_at_start', 'published_at_end', 'categories_taxonomy', 'categories_confident', 'categories_id', 'categories_level', 'entities_title_text', 'entities_title_type', 'entities_title_links_dbpedia', 'entities_body_text', 'entities_body_type', 'entities_body_links_dbpedia', 'sentiment_title_polarity', 'sentiment_body_polarity', 'media_images_count_min', 'media_images_count_max', 'media_videos_count_min', 'media_videos_count_max', 'author_id', 'author_name', 'source_id', 'source_name', 'source_domain', 'source_locations_country', 'source_locations_state', 'source_locations_city', 'source_scopes_country', 'source_scopes_state', 'source_scopes_city', 'source_scopes_level', 'interval_start', 'interval_end', 'interval_width', 'field']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_histograms" % key
                )
            params[key] = val
        del params['kwargs']

        if 'media_images_count_min' in params and params['media_images_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_min` when calling `list_histograms`, must be a value greater than or equal to `0.0`")
        if 'media_images_count_max' in params and params['media_images_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_max` when calling `list_histograms`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_min' in params and params['media_videos_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_min` when calling `list_histograms`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_max' in params and params['media_videos_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_max` when calling `list_histograms`, must be a value greater than or equal to `0.0`")
        resource_path = '/histograms'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id[]'] = params['id']
        if 'title' in params:
            query_params['title'] = params['title']
        if 'body' in params:
            query_params['body'] = params['body']
        if 'text' in params:
            query_params['text'] = params['text']
        if 'language' in params:
            query_params['language[]'] = params['language']
        if 'published_at_start' in params:
            query_params['published_at.start'] = params['published_at_start']
        if 'published_at_end' in params:
            query_params['published_at.end'] = params['published_at_end']
        if 'categories_taxonomy' in params:
            query_params['categories.taxonomy'] = params['categories_taxonomy']
        if 'categories_confident' in params:
            query_params['categories.confident'] = params['categories_confident']
        if 'categories_id' in params:
            query_params['categories.id[]'] = params['categories_id']
        if 'categories_level' in params:
            query_params['categories.level[]'] = params['categories_level']
        if 'entities_title_text' in params:
            query_params['entities.title.text[]'] = params['entities_title_text']
        if 'entities_title_type' in params:
            query_params['entities.title.type[]'] = params['entities_title_type']
        if 'entities_title_links_dbpedia' in params:
            query_params['entities.title.links.dbpedia[]'] = params['entities_title_links_dbpedia']
        if 'entities_body_text' in params:
            query_params['entities.body.text[]'] = params['entities_body_text']
        if 'entities_body_type' in params:
            query_params['entities.body.type[]'] = params['entities_body_type']
        if 'entities_body_links_dbpedia' in params:
            query_params['entities.body.links.dbpedia[]'] = params['entities_body_links_dbpedia']
        if 'sentiment_title_polarity' in params:
            query_params['sentiment.title.polarity'] = params['sentiment_title_polarity']
        if 'sentiment_body_polarity' in params:
            query_params['sentiment.body.polarity'] = params['sentiment_body_polarity']
        if 'media_images_count_min' in params:
            query_params['media.images.count.min'] = params['media_images_count_min']
        if 'media_images_count_max' in params:
            query_params['media.images.count.max'] = params['media_images_count_max']
        if 'media_videos_count_min' in params:
            query_params['media.videos.count.min'] = params['media_videos_count_min']
        if 'media_videos_count_max' in params:
            query_params['media.videos.count.max'] = params['media_videos_count_max']
        if 'author_id' in params:
            query_params['author.id[]'] = params['author_id']
        if 'author_name' in params:
            query_params['author.name'] = params['author_name']
        if 'source_id' in params:
            query_params['source.id[]'] = params['source_id']
        if 'source_name' in params:
            query_params['source.name[]'] = params['source_name']
        if 'source_domain' in params:
            query_params['source.domain[]'] = params['source_domain']
        if 'source_locations_country' in params:
            query_params['source.locations.country[]'] = params['source_locations_country']
        if 'source_locations_state' in params:
            query_params['source.locations.state[]'] = params['source_locations_state']
        if 'source_locations_city' in params:
            query_params['source.locations.city[]'] = params['source_locations_city']
        if 'source_scopes_country' in params:
            query_params['source.scopes.country[]'] = params['source_scopes_country']
        if 'source_scopes_state' in params:
            query_params['source.scopes.state[]'] = params['source_scopes_state']
        if 'source_scopes_city' in params:
            query_params['source.scopes.city[]'] = params['source_scopes_city']
        if 'source_scopes_level' in params:
            query_params['source.scopes.level[]'] = params['source_scopes_level']
        if 'interval_start' in params:
            query_params['interval.start'] = params['interval_start']
        if 'interval_end' in params:
            query_params['interval.end'] = params['interval_end']
        if 'interval_width' in params:
            query_params['interval.width'] = params['interval_width']
        if 'field' in params:
            query_params['field'] = params['field']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['app_key', 'app_id']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Histograms',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_related_stories(self, **kwargs):
        """
        List related stories
        This endpoint is used for finding related stories based on the parameters provided. The maximum number of related stories returned is 100.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_related_stories(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param bool cluster: This parameter enables clustering for the returned stories.
        :param str cluster_algorithm: This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms.
        :param list[str] _return: This parameter is used for specifying return fields.
        :param int story_id: A story id
        :param str story_url: An article or webpage
        :param str story_title: Title of the article
        :param str story_body: Body of the article
        :param str boost_by: This parameter is used for boosting the result by the specified value.
        :param str story_language: This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: RelatedStories
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_related_stories_with_http_info(**kwargs)
        else:
            (data) = self.list_related_stories_with_http_info(**kwargs)
            return data

    def list_related_stories_with_http_info(self, **kwargs):
        """
        List related stories
        This endpoint is used for finding related stories based on the parameters provided. The maximum number of related stories returned is 100.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_related_stories_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param bool cluster: This parameter enables clustering for the returned stories.
        :param str cluster_algorithm: This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms.
        :param list[str] _return: This parameter is used for specifying return fields.
        :param int story_id: A story id
        :param str story_url: An article or webpage
        :param str story_title: Title of the article
        :param str story_body: Body of the article
        :param str boost_by: This parameter is used for boosting the result by the specified value.
        :param str story_language: This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: RelatedStories
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'title', 'body', 'text', 'language', 'published_at_start', 'published_at_end', 'categories_taxonomy', 'categories_confident', 'categories_id', 'categories_level', 'entities_title_text', 'entities_title_type', 'entities_title_links_dbpedia', 'entities_body_text', 'entities_body_type', 'entities_body_links_dbpedia', 'sentiment_title_polarity', 'sentiment_body_polarity', 'media_images_count_min', 'media_images_count_max', 'media_videos_count_min', 'media_videos_count_max', 'author_id', 'author_name', 'source_id', 'source_name', 'source_domain', 'source_locations_country', 'source_locations_state', 'source_locations_city', 'source_scopes_country', 'source_scopes_state', 'source_scopes_city', 'source_scopes_level', 'cluster', 'cluster_algorithm', '_return', 'story_id', 'story_url', 'story_title', 'story_body', 'boost_by', 'story_language', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_related_stories" % key
                )
            params[key] = val
        del params['kwargs']

        if 'media_images_count_min' in params and params['media_images_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_min` when calling `list_related_stories`, must be a value greater than or equal to `0.0`")
        if 'media_images_count_max' in params and params['media_images_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_max` when calling `list_related_stories`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_min' in params and params['media_videos_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_min` when calling `list_related_stories`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_max' in params and params['media_videos_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_max` when calling `list_related_stories`, must be a value greater than or equal to `0.0`")
        if 'per_page' in params and params['per_page'] > 100.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_related_stories`, must be a value less than or equal to  `100.0`")
        if 'per_page' in params and params['per_page'] < 1.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_related_stories`, must be a value greater than or equal to `1.0`")
        resource_path = '/related_stories'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id[]', params['id']))
        if 'title' in params:
            form_params.append(('title', params['title']))
        if 'body' in params:
            form_params.append(('body', params['body']))
        if 'text' in params:
            form_params.append(('text', params['text']))
        if 'language' in params:
            form_params.append(('language[]', params['language']))
        if 'published_at_start' in params:
            form_params.append(('published_at.start', params['published_at_start']))
        if 'published_at_end' in params:
            form_params.append(('published_at.end', params['published_at_end']))
        if 'categories_taxonomy' in params:
            form_params.append(('categories.taxonomy', params['categories_taxonomy']))
        if 'categories_confident' in params:
            form_params.append(('categories.confident', params['categories_confident']))
        if 'categories_id' in params:
            form_params.append(('categories.id[]', params['categories_id']))
        if 'categories_level' in params:
            form_params.append(('categories.level[]', params['categories_level']))
        if 'entities_title_text' in params:
            form_params.append(('entities.title.text[]', params['entities_title_text']))
        if 'entities_title_type' in params:
            form_params.append(('entities.title.type[]', params['entities_title_type']))
        if 'entities_title_links_dbpedia' in params:
            form_params.append(('entities.title.links.dbpedia[]', params['entities_title_links_dbpedia']))
        if 'entities_body_text' in params:
            form_params.append(('entities.body.text[]', params['entities_body_text']))
        if 'entities_body_type' in params:
            form_params.append(('entities.body.type[]', params['entities_body_type']))
        if 'entities_body_links_dbpedia' in params:
            form_params.append(('entities.body.links.dbpedia[]', params['entities_body_links_dbpedia']))
        if 'sentiment_title_polarity' in params:
            form_params.append(('sentiment.title.polarity', params['sentiment_title_polarity']))
        if 'sentiment_body_polarity' in params:
            form_params.append(('sentiment.body.polarity', params['sentiment_body_polarity']))
        if 'media_images_count_min' in params:
            form_params.append(('media.images.count.min', params['media_images_count_min']))
        if 'media_images_count_max' in params:
            form_params.append(('media.images.count.max', params['media_images_count_max']))
        if 'media_videos_count_min' in params:
            form_params.append(('media.videos.count.min', params['media_videos_count_min']))
        if 'media_videos_count_max' in params:
            form_params.append(('media.videos.count.max', params['media_videos_count_max']))
        if 'author_id' in params:
            form_params.append(('author.id[]', params['author_id']))
        if 'author_name' in params:
            form_params.append(('author.name', params['author_name']))
        if 'source_id' in params:
            form_params.append(('source.id[]', params['source_id']))
        if 'source_name' in params:
            form_params.append(('source.name[]', params['source_name']))
        if 'source_domain' in params:
            form_params.append(('source.domain[]', params['source_domain']))
        if 'source_locations_country' in params:
            form_params.append(('source.locations.country[]', params['source_locations_country']))
        if 'source_locations_state' in params:
            form_params.append(('source.locations.state[]', params['source_locations_state']))
        if 'source_locations_city' in params:
            form_params.append(('source.locations.city[]', params['source_locations_city']))
        if 'source_scopes_country' in params:
            form_params.append(('source.scopes.country[]', params['source_scopes_country']))
        if 'source_scopes_state' in params:
            form_params.append(('source.scopes.state[]', params['source_scopes_state']))
        if 'source_scopes_city' in params:
            form_params.append(('source.scopes.city[]', params['source_scopes_city']))
        if 'source_scopes_level' in params:
            form_params.append(('source.scopes.level[]', params['source_scopes_level']))
        if 'cluster' in params:
            form_params.append(('cluster', params['cluster']))
        if 'cluster_algorithm' in params:
            form_params.append(('cluster.algorithm', params['cluster_algorithm']))
        if '_return' in params:
            form_params.append(('return[]', params['_return']))
        if 'story_id' in params:
            form_params.append(('story_id', params['story_id']))
        if 'story_url' in params:
            form_params.append(('story_url', params['story_url']))
        if 'story_title' in params:
            form_params.append(('story_title', params['story_title']))
        if 'story_body' in params:
            form_params.append(('story_body', params['story_body']))
        if 'boost_by' in params:
            form_params.append(('boost_by', params['boost_by']))
        if 'story_language' in params:
            form_params.append(('story_language', params['story_language']))
        if 'per_page' in params:
            form_params.append(('per_page', params['per_page']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['app_key', 'app_id']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RelatedStories',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_stories(self, **kwargs):
        """
        List Stories
        This endpoint is used for getting a list of stories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_stories(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param bool cluster: This parameter enables clustering for the returned stories.
        :param str cluster_algorithm: This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms.
        :param list[str] _return: This parameter is used for specifying return fields.
        :param str sort_by: This parameter is used for changing the order column of the results.
        :param str sort_direction: This parameter is used for changing the order direction of the result.
        :param str cursor: This parameter is used for finding a specific page.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: Stories
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_stories_with_http_info(**kwargs)
        else:
            (data) = self.list_stories_with_http_info(**kwargs)
            return data

    def list_stories_with_http_info(self, **kwargs):
        """
        List Stories
        This endpoint is used for getting a list of stories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_stories_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param bool cluster: This parameter enables clustering for the returned stories.
        :param str cluster_algorithm: This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms.
        :param list[str] _return: This parameter is used for specifying return fields.
        :param str sort_by: This parameter is used for changing the order column of the results.
        :param str sort_direction: This parameter is used for changing the order direction of the result.
        :param str cursor: This parameter is used for finding a specific page.
        :param int per_page: This parameter is used for specifying number of items in each page.
        :return: Stories
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'title', 'body', 'text', 'language', 'published_at_start', 'published_at_end', 'categories_taxonomy', 'categories_confident', 'categories_id', 'categories_level', 'entities_title_text', 'entities_title_type', 'entities_title_links_dbpedia', 'entities_body_text', 'entities_body_type', 'entities_body_links_dbpedia', 'sentiment_title_polarity', 'sentiment_body_polarity', 'media_images_count_min', 'media_images_count_max', 'media_videos_count_min', 'media_videos_count_max', 'author_id', 'author_name', 'source_id', 'source_name', 'source_domain', 'source_locations_country', 'source_locations_state', 'source_locations_city', 'source_scopes_country', 'source_scopes_state', 'source_scopes_city', 'source_scopes_level', 'cluster', 'cluster_algorithm', '_return', 'sort_by', 'sort_direction', 'cursor', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_stories" % key
                )
            params[key] = val
        del params['kwargs']

        if 'media_images_count_min' in params and params['media_images_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_min` when calling `list_stories`, must be a value greater than or equal to `0.0`")
        if 'media_images_count_max' in params and params['media_images_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_max` when calling `list_stories`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_min' in params and params['media_videos_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_min` when calling `list_stories`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_max' in params and params['media_videos_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_max` when calling `list_stories`, must be a value greater than or equal to `0.0`")
        if 'per_page' in params and params['per_page'] > 100.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_stories`, must be a value less than or equal to  `100.0`")
        if 'per_page' in params and params['per_page'] < 1.0:
            raise ValueError("Invalid value for parameter `per_page` when calling `list_stories`, must be a value greater than or equal to `1.0`")
        resource_path = '/stories'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id[]'] = params['id']
        if 'title' in params:
            query_params['title'] = params['title']
        if 'body' in params:
            query_params['body'] = params['body']
        if 'text' in params:
            query_params['text'] = params['text']
        if 'language' in params:
            query_params['language[]'] = params['language']
        if 'published_at_start' in params:
            query_params['published_at.start'] = params['published_at_start']
        if 'published_at_end' in params:
            query_params['published_at.end'] = params['published_at_end']
        if 'categories_taxonomy' in params:
            query_params['categories.taxonomy'] = params['categories_taxonomy']
        if 'categories_confident' in params:
            query_params['categories.confident'] = params['categories_confident']
        if 'categories_id' in params:
            query_params['categories.id[]'] = params['categories_id']
        if 'categories_level' in params:
            query_params['categories.level[]'] = params['categories_level']
        if 'entities_title_text' in params:
            query_params['entities.title.text[]'] = params['entities_title_text']
        if 'entities_title_type' in params:
            query_params['entities.title.type[]'] = params['entities_title_type']
        if 'entities_title_links_dbpedia' in params:
            query_params['entities.title.links.dbpedia[]'] = params['entities_title_links_dbpedia']
        if 'entities_body_text' in params:
            query_params['entities.body.text[]'] = params['entities_body_text']
        if 'entities_body_type' in params:
            query_params['entities.body.type[]'] = params['entities_body_type']
        if 'entities_body_links_dbpedia' in params:
            query_params['entities.body.links.dbpedia[]'] = params['entities_body_links_dbpedia']
        if 'sentiment_title_polarity' in params:
            query_params['sentiment.title.polarity'] = params['sentiment_title_polarity']
        if 'sentiment_body_polarity' in params:
            query_params['sentiment.body.polarity'] = params['sentiment_body_polarity']
        if 'media_images_count_min' in params:
            query_params['media.images.count.min'] = params['media_images_count_min']
        if 'media_images_count_max' in params:
            query_params['media.images.count.max'] = params['media_images_count_max']
        if 'media_videos_count_min' in params:
            query_params['media.videos.count.min'] = params['media_videos_count_min']
        if 'media_videos_count_max' in params:
            query_params['media.videos.count.max'] = params['media_videos_count_max']
        if 'author_id' in params:
            query_params['author.id[]'] = params['author_id']
        if 'author_name' in params:
            query_params['author.name'] = params['author_name']
        if 'source_id' in params:
            query_params['source.id[]'] = params['source_id']
        if 'source_name' in params:
            query_params['source.name[]'] = params['source_name']
        if 'source_domain' in params:
            query_params['source.domain[]'] = params['source_domain']
        if 'source_locations_country' in params:
            query_params['source.locations.country[]'] = params['source_locations_country']
        if 'source_locations_state' in params:
            query_params['source.locations.state[]'] = params['source_locations_state']
        if 'source_locations_city' in params:
            query_params['source.locations.city[]'] = params['source_locations_city']
        if 'source_scopes_country' in params:
            query_params['source.scopes.country[]'] = params['source_scopes_country']
        if 'source_scopes_state' in params:
            query_params['source.scopes.state[]'] = params['source_scopes_state']
        if 'source_scopes_city' in params:
            query_params['source.scopes.city[]'] = params['source_scopes_city']
        if 'source_scopes_level' in params:
            query_params['source.scopes.level[]'] = params['source_scopes_level']
        if 'cluster' in params:
            query_params['cluster'] = params['cluster']
        if 'cluster_algorithm' in params:
            query_params['cluster.algorithm'] = params['cluster_algorithm']
        if '_return' in params:
            query_params['return[]'] = params['_return']
        if 'sort_by' in params:
            query_params['sort_by'] = params['sort_by']
        if 'sort_direction' in params:
            query_params['sort_direction'] = params['sort_direction']
        if 'cursor' in params:
            query_params['cursor'] = params['cursor']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['app_key', 'app_id']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Stories',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_time_series(self, **kwargs):
        """
        List time series
        This endpoint is used for getting time series by stories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_time_series(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param str published_at_start: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str period: The size of each date range is expressed as an interval to be added to the lower bound. It supports Date Math Syntax. Valid options are `+` following an integer number greater than 0 and one of the Date Math keywords. e.g. `+1DAY`, `+2MINUTES` and `+1MONTH`. Here are [Supported keywords](https://newsapi.aylien.com/docs/working-with-dates#date-math).
        :return: TimeSeriesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_time_series_with_http_info(**kwargs)
        else:
            (data) = self.list_time_series_with_http_info(**kwargs)
            return data

    def list_time_series_with_http_info(self, **kwargs):
        """
        List time series
        This endpoint is used for getting time series by stories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_time_series_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param str published_at_start: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str period: The size of each date range is expressed as an interval to be added to the lower bound. It supports Date Math Syntax. Valid options are `+` following an integer number greater than 0 and one of the Date Math keywords. e.g. `+1DAY`, `+2MINUTES` and `+1MONTH`. Here are [Supported keywords](https://newsapi.aylien.com/docs/working-with-dates#date-math).
        :return: TimeSeriesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'title', 'body', 'text', 'language', 'categories_taxonomy', 'categories_confident', 'categories_id', 'categories_level', 'entities_title_text', 'entities_title_type', 'entities_title_links_dbpedia', 'entities_body_text', 'entities_body_type', 'entities_body_links_dbpedia', 'sentiment_title_polarity', 'sentiment_body_polarity', 'media_images_count_min', 'media_images_count_max', 'media_videos_count_min', 'media_videos_count_max', 'author_id', 'author_name', 'source_id', 'source_name', 'source_domain', 'source_locations_country', 'source_locations_state', 'source_locations_city', 'source_scopes_country', 'source_scopes_state', 'source_scopes_city', 'source_scopes_level', 'published_at_start', 'published_at_end', 'period']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_time_series" % key
                )
            params[key] = val
        del params['kwargs']

        if 'media_images_count_min' in params and params['media_images_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_min` when calling `list_time_series`, must be a value greater than or equal to `0.0`")
        if 'media_images_count_max' in params and params['media_images_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_max` when calling `list_time_series`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_min' in params and params['media_videos_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_min` when calling `list_time_series`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_max' in params and params['media_videos_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_max` when calling `list_time_series`, must be a value greater than or equal to `0.0`")
        resource_path = '/time_series'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id[]'] = params['id']
        if 'title' in params:
            query_params['title'] = params['title']
        if 'body' in params:
            query_params['body'] = params['body']
        if 'text' in params:
            query_params['text'] = params['text']
        if 'language' in params:
            query_params['language[]'] = params['language']
        if 'categories_taxonomy' in params:
            query_params['categories.taxonomy'] = params['categories_taxonomy']
        if 'categories_confident' in params:
            query_params['categories.confident'] = params['categories_confident']
        if 'categories_id' in params:
            query_params['categories.id[]'] = params['categories_id']
        if 'categories_level' in params:
            query_params['categories.level[]'] = params['categories_level']
        if 'entities_title_text' in params:
            query_params['entities.title.text[]'] = params['entities_title_text']
        if 'entities_title_type' in params:
            query_params['entities.title.type[]'] = params['entities_title_type']
        if 'entities_title_links_dbpedia' in params:
            query_params['entities.title.links.dbpedia[]'] = params['entities_title_links_dbpedia']
        if 'entities_body_text' in params:
            query_params['entities.body.text[]'] = params['entities_body_text']
        if 'entities_body_type' in params:
            query_params['entities.body.type[]'] = params['entities_body_type']
        if 'entities_body_links_dbpedia' in params:
            query_params['entities.body.links.dbpedia[]'] = params['entities_body_links_dbpedia']
        if 'sentiment_title_polarity' in params:
            query_params['sentiment.title.polarity'] = params['sentiment_title_polarity']
        if 'sentiment_body_polarity' in params:
            query_params['sentiment.body.polarity'] = params['sentiment_body_polarity']
        if 'media_images_count_min' in params:
            query_params['media.images.count.min'] = params['media_images_count_min']
        if 'media_images_count_max' in params:
            query_params['media.images.count.max'] = params['media_images_count_max']
        if 'media_videos_count_min' in params:
            query_params['media.videos.count.min'] = params['media_videos_count_min']
        if 'media_videos_count_max' in params:
            query_params['media.videos.count.max'] = params['media_videos_count_max']
        if 'author_id' in params:
            query_params['author.id[]'] = params['author_id']
        if 'author_name' in params:
            query_params['author.name'] = params['author_name']
        if 'source_id' in params:
            query_params['source.id[]'] = params['source_id']
        if 'source_name' in params:
            query_params['source.name[]'] = params['source_name']
        if 'source_domain' in params:
            query_params['source.domain[]'] = params['source_domain']
        if 'source_locations_country' in params:
            query_params['source.locations.country[]'] = params['source_locations_country']
        if 'source_locations_state' in params:
            query_params['source.locations.state[]'] = params['source_locations_state']
        if 'source_locations_city' in params:
            query_params['source.locations.city[]'] = params['source_locations_city']
        if 'source_scopes_country' in params:
            query_params['source.scopes.country[]'] = params['source_scopes_country']
        if 'source_scopes_state' in params:
            query_params['source.scopes.state[]'] = params['source_scopes_state']
        if 'source_scopes_city' in params:
            query_params['source.scopes.city[]'] = params['source_scopes_city']
        if 'source_scopes_level' in params:
            query_params['source.scopes.level[]'] = params['source_scopes_level']
        if 'published_at_start' in params:
            query_params['published_at.start'] = params['published_at_start']
        if 'published_at_end' in params:
            query_params['published_at.end'] = params['published_at_end']
        if 'period' in params:
            query_params['period'] = params['period']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['app_key', 'app_id']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='TimeSeriesList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def list_trends(self, **kwargs):
        """
        List trends
        This endpoint is used for finding trends based on stories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_trends(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param str field: This parameter is used to specify the trend field.
        :return: Trends
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_trends_with_http_info(**kwargs)
        else:
            (data) = self.list_trends_with_http_info(**kwargs)
            return data

    def list_trends_with_http_info(self, **kwargs):
        """
        List trends
        This endpoint is used for finding trends based on stories.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_trends_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[int] id: This parameter is used for finding stroies by story id.
        :param str title: This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str body: This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param str text: This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).
        :param list[str] language: This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.
        :param str published_at_start: This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str published_at_end: This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).
        :param str categories_taxonomy: This parameter is used for defining the type of the taxonomy for the rest of the categories queries.
        :param bool categories_confident: This parameter is used for finding stories whose categories are confident.
        :param list[str] categories_id: This parameter is used for finding stories by categories id.
        :param list[int] categories_level: This parameter is used for finding stories by categories level.
        :param list[str] entities_title_text: This parameter is used to find stories based on the specified entities `text` in story titles.
        :param list[str] entities_title_type: This parameter is used to find stories based on the specified entities `type` in story titles.
        :param list[str] entities_title_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in story titles.
        :param list[str] entities_body_text: This parameter is used to find stories based on the specified entities `text` in the body of stories.
        :param list[str] entities_body_type: This parameter is used to find stories based on the specified entities `type` in the body of stories.
        :param list[str] entities_body_links_dbpedia: This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories.
        :param str sentiment_title_polarity: This parameter is used for finding stories whose title sentiment is the specified value.
        :param str sentiment_body_polarity: This parameter is used for finding stories whose body sentiment is the specified value.
        :param int media_images_count_min: This parameter is used for finding stories whose number of images is greater than or equal to the specified value.
        :param int media_images_count_max: This parameter is used for finding stories whose number of images is less than or equal to the specified value.
        :param int media_videos_count_min: This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.
        :param int media_videos_count_max: This parameter is used for finding stories whose number of videos is less than or equal to the specified value.
        :param list[int] author_id: This parameter is used for finding stories whose author id is the specified value.
        :param str author_name: This parameter is used for finding stories whose author full name contains the specified value.
        :param list[int] source_id: This parameter is used for finding stories whose source id is the specified value.
        :param list[str] source_name: This parameter is used for finding stories whose source name contains the specified value.
        :param list[str] source_domain: This parameter is used for finding stories whose source domain is the specified value.
        :param list[str] source_locations_country: This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_state: This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_locations_city: This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_country: This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_state: This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_city: This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param list[str] source_scopes_level: This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).
        :param str field: This parameter is used to specify the trend field.
        :return: Trends
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'title', 'body', 'text', 'language', 'published_at_start', 'published_at_end', 'categories_taxonomy', 'categories_confident', 'categories_id', 'categories_level', 'entities_title_text', 'entities_title_type', 'entities_title_links_dbpedia', 'entities_body_text', 'entities_body_type', 'entities_body_links_dbpedia', 'sentiment_title_polarity', 'sentiment_body_polarity', 'media_images_count_min', 'media_images_count_max', 'media_videos_count_min', 'media_videos_count_max', 'author_id', 'author_name', 'source_id', 'source_name', 'source_domain', 'source_locations_country', 'source_locations_state', 'source_locations_city', 'source_scopes_country', 'source_scopes_state', 'source_scopes_city', 'source_scopes_level', 'field']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_trends" % key
                )
            params[key] = val
        del params['kwargs']

        if 'media_images_count_min' in params and params['media_images_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_min` when calling `list_trends`, must be a value greater than or equal to `0.0`")
        if 'media_images_count_max' in params and params['media_images_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_images_count_max` when calling `list_trends`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_min' in params and params['media_videos_count_min'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_min` when calling `list_trends`, must be a value greater than or equal to `0.0`")
        if 'media_videos_count_max' in params and params['media_videos_count_max'] < 0.0:
            raise ValueError("Invalid value for parameter `media_videos_count_max` when calling `list_trends`, must be a value greater than or equal to `0.0`")
        resource_path = '/trends'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id[]'] = params['id']
        if 'title' in params:
            query_params['title'] = params['title']
        if 'body' in params:
            query_params['body'] = params['body']
        if 'text' in params:
            query_params['text'] = params['text']
        if 'language' in params:
            query_params['language[]'] = params['language']
        if 'published_at_start' in params:
            query_params['published_at.start'] = params['published_at_start']
        if 'published_at_end' in params:
            query_params['published_at.end'] = params['published_at_end']
        if 'categories_taxonomy' in params:
            query_params['categories.taxonomy'] = params['categories_taxonomy']
        if 'categories_confident' in params:
            query_params['categories.confident'] = params['categories_confident']
        if 'categories_id' in params:
            query_params['categories.id[]'] = params['categories_id']
        if 'categories_level' in params:
            query_params['categories.level[]'] = params['categories_level']
        if 'entities_title_text' in params:
            query_params['entities.title.text[]'] = params['entities_title_text']
        if 'entities_title_type' in params:
            query_params['entities.title.type[]'] = params['entities_title_type']
        if 'entities_title_links_dbpedia' in params:
            query_params['entities.title.links.dbpedia[]'] = params['entities_title_links_dbpedia']
        if 'entities_body_text' in params:
            query_params['entities.body.text[]'] = params['entities_body_text']
        if 'entities_body_type' in params:
            query_params['entities.body.type[]'] = params['entities_body_type']
        if 'entities_body_links_dbpedia' in params:
            query_params['entities.body.links.dbpedia[]'] = params['entities_body_links_dbpedia']
        if 'sentiment_title_polarity' in params:
            query_params['sentiment.title.polarity'] = params['sentiment_title_polarity']
        if 'sentiment_body_polarity' in params:
            query_params['sentiment.body.polarity'] = params['sentiment_body_polarity']
        if 'media_images_count_min' in params:
            query_params['media.images.count.min'] = params['media_images_count_min']
        if 'media_images_count_max' in params:
            query_params['media.images.count.max'] = params['media_images_count_max']
        if 'media_videos_count_min' in params:
            query_params['media.videos.count.min'] = params['media_videos_count_min']
        if 'media_videos_count_max' in params:
            query_params['media.videos.count.max'] = params['media_videos_count_max']
        if 'author_id' in params:
            query_params['author.id[]'] = params['author_id']
        if 'author_name' in params:
            query_params['author.name'] = params['author_name']
        if 'source_id' in params:
            query_params['source.id[]'] = params['source_id']
        if 'source_name' in params:
            query_params['source.name[]'] = params['source_name']
        if 'source_domain' in params:
            query_params['source.domain[]'] = params['source_domain']
        if 'source_locations_country' in params:
            query_params['source.locations.country[]'] = params['source_locations_country']
        if 'source_locations_state' in params:
            query_params['source.locations.state[]'] = params['source_locations_state']
        if 'source_locations_city' in params:
            query_params['source.locations.city[]'] = params['source_locations_city']
        if 'source_scopes_country' in params:
            query_params['source.scopes.country[]'] = params['source_scopes_country']
        if 'source_scopes_state' in params:
            query_params['source.scopes.state[]'] = params['source_scopes_state']
        if 'source_scopes_city' in params:
            query_params['source.scopes.city[]'] = params['source_scopes_city']
        if 'source_scopes_level' in params:
            query_params['source.scopes.level[]'] = params['source_scopes_level']
        if 'field' in params:
            query_params['field'] = params['field']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/xml'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['app_key', 'app_id']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Trends',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
