# aylien_news_api.DefaultApi

All URIs are relative to *https://api.newsapi.aylien.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_autocompletes**](DefaultApi.md#list_autocompletes) | **GET** /autocompletes | List autocompletes
[**list_coverages**](DefaultApi.md#list_coverages) | **POST** /coverages | List coverages
[**list_histograms**](DefaultApi.md#list_histograms) | **GET** /histograms | List histograms
[**list_related_stories**](DefaultApi.md#list_related_stories) | **POST** /related_stories | List related stories
[**list_stories**](DefaultApi.md#list_stories) | **GET** /stories | List Stories
[**list_time_series**](DefaultApi.md#list_time_series) | **GET** /time_series | List time series
[**list_trends**](DefaultApi.md#list_trends) | **GET** /trends | List trends


# **list_autocompletes**
> Autocompletes list_autocompletes(type, term, language=language, per_page=per_page)

List autocompletes

This endpoint is used for getting list of autocompletes by providing a specific term and type.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

type = 'type_example'
term = 'term_example'

opts = { 
    'language': 'en',
    'per_page': 3
}

try: 
    # List autocompletes
    api_response = api_instance.list_autocompletes(type, term, **opts)
    pprint(api_response)
except ApiException as e:
    pprint("Exception when calling DefaultApi->list_autocompletes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| This parameter is used for defining the type of autocompletes. |  [enum: source_names, source_domains, entity_types, dbpedia_resources]
 **term** | **str**| This parameter is used for finding autocomplete objects that contain the specified value. | 
 **language** | **str**| This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] [default to en] [enum: en, de, fr, it, es, pt]
 **per_page** | **int**| This parameter is used for specifying number of items in each page. | [optional] [default to 3]

### Return type

[**Autocompletes**](Autocompletes.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_coverages**
> Coverages list_coverages(id=id, not_id=not_id, title=title, body=body, text=text, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_level=categories_level, not_categories_level=not_categories_level, entities_title_text=entities_title_text, not_entities_title_text=not_entities_title_text, entities_title_type=entities_title_type, not_entities_title_type=not_entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, not_entities_title_links_dbpedia=not_entities_title_links_dbpedia, entities_body_text=entities_body_text, not_entities_body_text=not_entities_body_text, entities_body_type=entities_body_type, not_entities_body_type=not_entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, not_entities_body_links_dbpedia=not_entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, story_published_at=story_published_at, story_language=story_language, per_page=per_page)

List coverages

This endpoint is used for finding story coverages based on the parameters provided. The maximum number of related stories returned is 100.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()


opts = { 
    'id': [56],
    'not_id': [56],
    'title': 'title_example',
    'body': 'body_example',
    'text': 'text_example',
    'language': ['language_example'],
    'not_language': ['not_language_example'],
    'published_at_start': 'published_at_start_example',
    'published_at_end': 'published_at_end_example',
    'categories_taxonomy': 'categories_taxonomy_example',
    'categories_confident': true,
    'categories_id': ['categories_id_example'],
    'not_categories_id': ['not_categories_id_example'],
    'categories_level': [56],
    'not_categories_level': [56],
    'entities_title_text': ['entities_title_text_example'],
    'not_entities_title_text': ['not_entities_title_text_example'],
    'entities_title_type': ['entities_title_type_example'],
    'not_entities_title_type': ['not_entities_title_type_example'],
    'entities_title_links_dbpedia': ['entities_title_links_dbpedia_example'],
    'not_entities_title_links_dbpedia': ['not_entities_title_links_dbpedia_example'],
    'entities_body_text': ['entities_body_text_example'],
    'not_entities_body_text': ['not_entities_body_text_example'],
    'entities_body_type': ['entities_body_type_example'],
    'not_entities_body_type': ['not_entities_body_type_example'],
    'entities_body_links_dbpedia': ['entities_body_links_dbpedia_example'],
    'not_entities_body_links_dbpedia': ['not_entities_body_links_dbpedia_example'],
    'sentiment_title_polarity': 'sentiment_title_polarity_example',
    'not_sentiment_title_polarity': 'not_sentiment_title_polarity_example',
    'sentiment_body_polarity': 'sentiment_body_polarity_example',
    'not_sentiment_body_polarity': 'not_sentiment_body_polarity_example',
    'media_images_count_min': 56,
    'media_images_count_max': 56,
    'media_images_width_min': 56,
    'media_images_width_max': 56,
    'media_images_height_min': 56,
    'media_images_height_max': 56,
    'media_images_content_length_min': 56,
    'media_images_content_length_max': 56,
    'media_images_format': ['media_images_format_example'],
    'not_media_images_format': ['not_media_images_format_example'],
    'media_videos_count_min': 56,
    'media_videos_count_max': 56,
    'author_id': [56],
    'not_author_id': [56],
    'author_name': 'author_name_example',
    'not_author_name': 'not_author_name_example',
    'source_id': [56],
    'not_source_id': [56],
    'source_name': ['source_name_example'],
    'not_source_name': ['not_source_name_example'],
    'source_domain': ['source_domain_example'],
    'not_source_domain': ['not_source_domain_example'],
    'source_locations_country': ['source_locations_country_example'],
    'not_source_locations_country': ['not_source_locations_country_example'],
    'source_locations_state': ['source_locations_state_example'],
    'not_source_locations_state': ['not_source_locations_state_example'],
    'source_locations_city': ['source_locations_city_example'],
    'not_source_locations_city': ['not_source_locations_city_example'],
    'source_scopes_country': ['source_scopes_country_example'],
    'not_source_scopes_country': ['not_source_scopes_country_example'],
    'source_scopes_state': ['source_scopes_state_example'],
    'not_source_scopes_state': ['not_source_scopes_state_example'],
    'source_scopes_city': ['source_scopes_city_example'],
    'not_source_scopes_city': ['not_source_scopes_city_example'],
    'source_scopes_level': ['source_scopes_level_example'],
    'not_source_scopes_level': ['not_source_scopes_level_example'],
    'source_links_in_count_min': 56,
    'source_links_in_count_max': 56,
    'source_rankings_alexa_rank_min': 56,
    'source_rankings_alexa_rank_max': 56,
    'source_rankings_alexa_country': ['source_rankings_alexa_country_example'],
    'social_shares_count_facebook_min': 56,
    'social_shares_count_facebook_max': 56,
    'social_shares_count_google_plus_min': 56,
    'social_shares_count_google_plus_max': 56,
    'social_shares_count_linkedin_min': 56,
    'social_shares_count_linkedin_max': 56,
    'social_shares_count_reddit_min': 56,
    'social_shares_count_reddit_max': 56,
    'cluster': false,
    'cluster_algorithm': 'lingo',
    '_return': ['_return_example'],
    'story_id': 789,
    'story_url': 'story_url_example',
    'story_title': 'story_title_example',
    'story_body': 'story_body_example',
    'story_published_at': '2013-10-20T19:20:30+01:00',
    'story_language': 'auto',
    'per_page': 3
}

try: 
    # List coverages
    api_response = api_instance.list_coverages(**opts)
    pprint(api_response)
except ApiException as e:
    pprint("Exception when calling DefaultApi->list_coverages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **list[int]**| This parameter is used for finding stories by story id. | [optional] 
 **not_id** | **list[int]**| This parameter is used for excluding stories by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | **list[str]**| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **not_language** | **list[str]**| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional]  [enum: iab-qag, iptc-subjectcode]
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] [default to true]
 **categories_id** | **list[str]**| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_id** | **list[str]**| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **categories_level** | **list[int]**| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_level** | **list[int]**| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **entities_title_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value. | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value. | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value. | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value. | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value. | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value. | [optional] 
 **media_images_format** | **list[str]**| This parameter is used for finding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **not_media_images_format** | **list[str]**| This parameter is used for excluding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | **list[int]**| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **not_author_id** | **list[int]**| This parameter is used for excluding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value. | [optional] 
 **source_id** | **list[int]**| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **not_source_id** | **list[int]**| This parameter is used for excluding stories whose source id is the specified value. | [optional] 
 **source_name** | **list[str]**| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **not_source_name** | **list[str]**| This parameter is used for excluding stories whose source name contains the specified value. | [optional] 
 **source_domain** | **list[str]**| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **not_source_domain** | **list[str]**| This parameter is used for excluding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | **list[str]**| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_country** | **list[str]**| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | **list[str]**| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_state** | **list[str]**| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | **list[str]**| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_city** | **list[str]**| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | **list[str]**| This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_country** | **list[str]**| This parameter is used for excluding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_state** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_city** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | **list[str]**| This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **not_source_scopes_level** | **list[str]**| This parameter is used for excluding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | **list[str]**| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value. | [optional] 
 **cluster** | **bool**| This parameter enables clustering for the returned stories. You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering). | [optional] [default to false]
 **cluster_algorithm** | **str**| This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering). | [optional] [default to lingo] [enum: stc, lingo, kmeans]
 **_return** | **list[str]**| This parameter is used for specifying return fields. | [optional]  [enum: id, title, body, summary, source, author, entities, keywords, hashtags, characters_count, words_count, sentences_count, paragraphs_count, categories, social_shares_count, media, sentiment, language, published_at, links]
 **story_id** | **int**| A story id | [optional] 
 **story_url** | **str**| An article or webpage | [optional] 
 **story_title** | **str**| Title of the article | [optional] 
 **story_body** | **str**| Body of the article | [optional] 
 **story_published_at** | **datetime**| Publish date of the article. If you use a url or title and body of an article for getting coverages, this parameter is required. The format used is a restricted form of the canonical representation of dateTime in the [XML Schema specification (ISO 8601)](https://www.w3.org/TR/xmlschema-2/#dateTime). | [optional] 
 **story_language** | **str**| This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] [default to auto] [enum: auto, en, de, fr, it, es, pt]
 **per_page** | **int**| This parameter is used for specifying number of items in each page. | [optional] [default to 3]

### Return type

[**Coverages**](Coverages.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_histograms**
> Histograms list_histograms(id=id, not_id=not_id, title=title, body=body, text=text, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_level=categories_level, not_categories_level=not_categories_level, entities_title_text=entities_title_text, not_entities_title_text=not_entities_title_text, entities_title_type=entities_title_type, not_entities_title_type=not_entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, not_entities_title_links_dbpedia=not_entities_title_links_dbpedia, entities_body_text=entities_body_text, not_entities_body_text=not_entities_body_text, entities_body_type=entities_body_type, not_entities_body_type=not_entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, not_entities_body_links_dbpedia=not_entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, interval_start=interval_start, interval_end=interval_end, interval_width=interval_width, field=field)

List histograms

This endpoint is used for getting histograms based on the `field` parameter passed to the API.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()


opts = { 
    'id': [56],
    'not_id': [56],
    'title': 'title_example',
    'body': 'body_example',
    'text': 'text_example',
    'language': ['language_example'],
    'not_language': ['not_language_example'],
    'published_at_start': 'published_at_start_example',
    'published_at_end': 'published_at_end_example',
    'categories_taxonomy': 'categories_taxonomy_example',
    'categories_confident': true,
    'categories_id': ['categories_id_example'],
    'not_categories_id': ['not_categories_id_example'],
    'categories_level': [56],
    'not_categories_level': [56],
    'entities_title_text': ['entities_title_text_example'],
    'not_entities_title_text': ['not_entities_title_text_example'],
    'entities_title_type': ['entities_title_type_example'],
    'not_entities_title_type': ['not_entities_title_type_example'],
    'entities_title_links_dbpedia': ['entities_title_links_dbpedia_example'],
    'not_entities_title_links_dbpedia': ['not_entities_title_links_dbpedia_example'],
    'entities_body_text': ['entities_body_text_example'],
    'not_entities_body_text': ['not_entities_body_text_example'],
    'entities_body_type': ['entities_body_type_example'],
    'not_entities_body_type': ['not_entities_body_type_example'],
    'entities_body_links_dbpedia': ['entities_body_links_dbpedia_example'],
    'not_entities_body_links_dbpedia': ['not_entities_body_links_dbpedia_example'],
    'sentiment_title_polarity': 'sentiment_title_polarity_example',
    'not_sentiment_title_polarity': 'not_sentiment_title_polarity_example',
    'sentiment_body_polarity': 'sentiment_body_polarity_example',
    'not_sentiment_body_polarity': 'not_sentiment_body_polarity_example',
    'media_images_count_min': 56,
    'media_images_count_max': 56,
    'media_images_width_min': 56,
    'media_images_width_max': 56,
    'media_images_height_min': 56,
    'media_images_height_max': 56,
    'media_images_content_length_min': 56,
    'media_images_content_length_max': 56,
    'media_images_format': ['media_images_format_example'],
    'not_media_images_format': ['not_media_images_format_example'],
    'media_videos_count_min': 56,
    'media_videos_count_max': 56,
    'author_id': [56],
    'not_author_id': [56],
    'author_name': 'author_name_example',
    'not_author_name': 'not_author_name_example',
    'source_id': [56],
    'not_source_id': [56],
    'source_name': ['source_name_example'],
    'not_source_name': ['not_source_name_example'],
    'source_domain': ['source_domain_example'],
    'not_source_domain': ['not_source_domain_example'],
    'source_locations_country': ['source_locations_country_example'],
    'not_source_locations_country': ['not_source_locations_country_example'],
    'source_locations_state': ['source_locations_state_example'],
    'not_source_locations_state': ['not_source_locations_state_example'],
    'source_locations_city': ['source_locations_city_example'],
    'not_source_locations_city': ['not_source_locations_city_example'],
    'source_scopes_country': ['source_scopes_country_example'],
    'not_source_scopes_country': ['not_source_scopes_country_example'],
    'source_scopes_state': ['source_scopes_state_example'],
    'not_source_scopes_state': ['not_source_scopes_state_example'],
    'source_scopes_city': ['source_scopes_city_example'],
    'not_source_scopes_city': ['not_source_scopes_city_example'],
    'source_scopes_level': ['source_scopes_level_example'],
    'not_source_scopes_level': ['not_source_scopes_level_example'],
    'source_links_in_count_min': 56,
    'source_links_in_count_max': 56,
    'source_rankings_alexa_rank_min': 56,
    'source_rankings_alexa_rank_max': 56,
    'source_rankings_alexa_country': ['source_rankings_alexa_country_example'],
    'social_shares_count_facebook_min': 56,
    'social_shares_count_facebook_max': 56,
    'social_shares_count_google_plus_min': 56,
    'social_shares_count_google_plus_max': 56,
    'social_shares_count_linkedin_min': 56,
    'social_shares_count_linkedin_max': 56,
    'social_shares_count_reddit_min': 56,
    'social_shares_count_reddit_max': 56,
    'interval_start': 56,
    'interval_end': 56,
    'interval_width': 56,
    'field': 'social_shares_count'
}

try: 
    # List histograms
    api_response = api_instance.list_histograms(**opts)
    pprint(api_response)
except ApiException as e:
    pprint("Exception when calling DefaultApi->list_histograms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **list[int]**| This parameter is used for finding stories by story id. | [optional] 
 **not_id** | **list[int]**| This parameter is used for excluding stories by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | **list[str]**| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **not_language** | **list[str]**| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional]  [enum: iab-qag, iptc-subjectcode]
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] [default to true]
 **categories_id** | **list[str]**| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_id** | **list[str]**| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **categories_level** | **list[int]**| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_level** | **list[int]**| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **entities_title_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value. | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value. | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value. | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value. | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value. | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value. | [optional] 
 **media_images_format** | **list[str]**| This parameter is used for finding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **not_media_images_format** | **list[str]**| This parameter is used for excluding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | **list[int]**| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **not_author_id** | **list[int]**| This parameter is used for excluding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value. | [optional] 
 **source_id** | **list[int]**| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **not_source_id** | **list[int]**| This parameter is used for excluding stories whose source id is the specified value. | [optional] 
 **source_name** | **list[str]**| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **not_source_name** | **list[str]**| This parameter is used for excluding stories whose source name contains the specified value. | [optional] 
 **source_domain** | **list[str]**| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **not_source_domain** | **list[str]**| This parameter is used for excluding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | **list[str]**| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_country** | **list[str]**| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | **list[str]**| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_state** | **list[str]**| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | **list[str]**| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_city** | **list[str]**| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_country** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_state** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_city** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **not_source_scopes_level** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | **list[str]**| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value. | [optional] 
 **interval_start** | **int**| This parameter is used for setting the start data point of histogram intervals. | [optional] 
 **interval_end** | **int**| This parameter is used for setting the end data point of histogram intervals. | [optional] 
 **interval_width** | **int**| This parameter is used for setting the width of histogram intervals. | [optional] 
 **field** | **str**| This parameter is used for specifying the y-axis variable for the histogram. | [optional] [default to social_shares_count] [enum: social_shares_count, social_shares_count.facebook, social_shares_count.linkedin, social_shares_count.reddit, social_shares_count.google_plus, characters_count, words_count, sentences_count, paragraphs_count, media.images.count, media.videos.count, source.links_in_count, source.rankings.alexa.rank, source.rankings.alexa.rank.AF, source.rankings.alexa.rank.AX, source.rankings.alexa.rank.AL, source.rankings.alexa.rank.DZ, source.rankings.alexa.rank.AS, source.rankings.alexa.rank.AD, source.rankings.alexa.rank.AO, source.rankings.alexa.rank.AI, source.rankings.alexa.rank.AQ, source.rankings.alexa.rank.AG, source.rankings.alexa.rank.AR, source.rankings.alexa.rank.AM, source.rankings.alexa.rank.AW, source.rankings.alexa.rank.AU, source.rankings.alexa.rank.AT, source.rankings.alexa.rank.AZ, source.rankings.alexa.rank.BS, source.rankings.alexa.rank.BH, source.rankings.alexa.rank.BD, source.rankings.alexa.rank.BB, source.rankings.alexa.rank.BY, source.rankings.alexa.rank.BE, source.rankings.alexa.rank.BZ, source.rankings.alexa.rank.BJ, source.rankings.alexa.rank.BM, source.rankings.alexa.rank.BT, source.rankings.alexa.rank.BO, source.rankings.alexa.rank.BQ, source.rankings.alexa.rank.BA, source.rankings.alexa.rank.BW, source.rankings.alexa.rank.BV, source.rankings.alexa.rank.BR, source.rankings.alexa.rank.IO, source.rankings.alexa.rank.BN, source.rankings.alexa.rank.BG, source.rankings.alexa.rank.BF, source.rankings.alexa.rank.BI, source.rankings.alexa.rank.KH, source.rankings.alexa.rank.CM, source.rankings.alexa.rank.CA, source.rankings.alexa.rank.CV, source.rankings.alexa.rank.KY, source.rankings.alexa.rank.CF, source.rankings.alexa.rank.TD, source.rankings.alexa.rank.CL, source.rankings.alexa.rank.CN, source.rankings.alexa.rank.CX, source.rankings.alexa.rank.CC, source.rankings.alexa.rank.CO, source.rankings.alexa.rank.KM, source.rankings.alexa.rank.CG, source.rankings.alexa.rank.CD, source.rankings.alexa.rank.CK, source.rankings.alexa.rank.CR, source.rankings.alexa.rank.CI, source.rankings.alexa.rank.HR, source.rankings.alexa.rank.CU, source.rankings.alexa.rank.CW, source.rankings.alexa.rank.CY, source.rankings.alexa.rank.CZ, source.rankings.alexa.rank.DK, source.rankings.alexa.rank.DJ, source.rankings.alexa.rank.DM, source.rankings.alexa.rank.DO, source.rankings.alexa.rank.EC, source.rankings.alexa.rank.EG, source.rankings.alexa.rank.SV, source.rankings.alexa.rank.GQ, source.rankings.alexa.rank.ER, source.rankings.alexa.rank.EE, source.rankings.alexa.rank.ET, source.rankings.alexa.rank.FK, source.rankings.alexa.rank.FO, source.rankings.alexa.rank.FJ, source.rankings.alexa.rank.FI, source.rankings.alexa.rank.FR, source.rankings.alexa.rank.GF, source.rankings.alexa.rank.PF, source.rankings.alexa.rank.TF, source.rankings.alexa.rank.GA, source.rankings.alexa.rank.GM, source.rankings.alexa.rank.GE, source.rankings.alexa.rank.DE, source.rankings.alexa.rank.GH, source.rankings.alexa.rank.GI, source.rankings.alexa.rank.GR, source.rankings.alexa.rank.GL, source.rankings.alexa.rank.GD, source.rankings.alexa.rank.GP, source.rankings.alexa.rank.GU, source.rankings.alexa.rank.GT, source.rankings.alexa.rank.GG, source.rankings.alexa.rank.GN, source.rankings.alexa.rank.GW, source.rankings.alexa.rank.GY, source.rankings.alexa.rank.HT, source.rankings.alexa.rank.HM, source.rankings.alexa.rank.VA, source.rankings.alexa.rank.HN, source.rankings.alexa.rank.HK, source.rankings.alexa.rank.HU, source.rankings.alexa.rank.IS, source.rankings.alexa.rank.IN, source.rankings.alexa.rank.ID, source.rankings.alexa.rank.IR, source.rankings.alexa.rank.IQ, source.rankings.alexa.rank.IE, source.rankings.alexa.rank.IM, source.rankings.alexa.rank.IL, source.rankings.alexa.rank.IT, source.rankings.alexa.rank.JM, source.rankings.alexa.rank.JP, source.rankings.alexa.rank.JE, source.rankings.alexa.rank.JO, source.rankings.alexa.rank.KZ, source.rankings.alexa.rank.KE, source.rankings.alexa.rank.KI, source.rankings.alexa.rank.KP, source.rankings.alexa.rank.KR, source.rankings.alexa.rank.KW, source.rankings.alexa.rank.KG, source.rankings.alexa.rank.LA, source.rankings.alexa.rank.LV, source.rankings.alexa.rank.LB, source.rankings.alexa.rank.LS, source.rankings.alexa.rank.LR, source.rankings.alexa.rank.LY, source.rankings.alexa.rank.LI, source.rankings.alexa.rank.LT, source.rankings.alexa.rank.LU, source.rankings.alexa.rank.MO, source.rankings.alexa.rank.MK, source.rankings.alexa.rank.MG, source.rankings.alexa.rank.MW, source.rankings.alexa.rank.MY, source.rankings.alexa.rank.MV, source.rankings.alexa.rank.ML, source.rankings.alexa.rank.MT, source.rankings.alexa.rank.MH, source.rankings.alexa.rank.MQ, source.rankings.alexa.rank.MR, source.rankings.alexa.rank.MU, source.rankings.alexa.rank.YT, source.rankings.alexa.rank.MX, source.rankings.alexa.rank.FM, source.rankings.alexa.rank.MD, source.rankings.alexa.rank.MC, source.rankings.alexa.rank.MN, source.rankings.alexa.rank.ME, source.rankings.alexa.rank.MS, source.rankings.alexa.rank.MA, source.rankings.alexa.rank.MZ, source.rankings.alexa.rank.MM, source.rankings.alexa.rank.NA, source.rankings.alexa.rank.NR, source.rankings.alexa.rank.NP, source.rankings.alexa.rank.NL, source.rankings.alexa.rank.NC, source.rankings.alexa.rank.NZ, source.rankings.alexa.rank.NI, source.rankings.alexa.rank.NE, source.rankings.alexa.rank.NG, source.rankings.alexa.rank.NU, source.rankings.alexa.rank.NF, source.rankings.alexa.rank.MP, source.rankings.alexa.rank.NO, source.rankings.alexa.rank.OM, source.rankings.alexa.rank.PK, source.rankings.alexa.rank.PW, source.rankings.alexa.rank.PS, source.rankings.alexa.rank.PA, source.rankings.alexa.rank.PG, source.rankings.alexa.rank.PY, source.rankings.alexa.rank.PE, source.rankings.alexa.rank.PH, source.rankings.alexa.rank.PN, source.rankings.alexa.rank.PL, source.rankings.alexa.rank.PT, source.rankings.alexa.rank.PR, source.rankings.alexa.rank.QA, source.rankings.alexa.rank.RE, source.rankings.alexa.rank.RO, source.rankings.alexa.rank.RU, source.rankings.alexa.rank.RW, source.rankings.alexa.rank.BL, source.rankings.alexa.rank.SH, source.rankings.alexa.rank.KN, source.rankings.alexa.rank.LC, source.rankings.alexa.rank.MF, source.rankings.alexa.rank.PM, source.rankings.alexa.rank.VC, source.rankings.alexa.rank.WS, source.rankings.alexa.rank.SM, source.rankings.alexa.rank.ST, source.rankings.alexa.rank.SA, source.rankings.alexa.rank.SN, source.rankings.alexa.rank.RS, source.rankings.alexa.rank.SC, source.rankings.alexa.rank.SL, source.rankings.alexa.rank.SG, source.rankings.alexa.rank.SX, source.rankings.alexa.rank.SK, source.rankings.alexa.rank.SI, source.rankings.alexa.rank.SB, source.rankings.alexa.rank.SO, source.rankings.alexa.rank.ZA, source.rankings.alexa.rank.GS, source.rankings.alexa.rank.SS, source.rankings.alexa.rank.ES, source.rankings.alexa.rank.LK, source.rankings.alexa.rank.SD, source.rankings.alexa.rank.SR, source.rankings.alexa.rank.SJ, source.rankings.alexa.rank.SZ, source.rankings.alexa.rank.SE, source.rankings.alexa.rank.CH, source.rankings.alexa.rank.SY, source.rankings.alexa.rank.TW, source.rankings.alexa.rank.TJ, source.rankings.alexa.rank.TZ, source.rankings.alexa.rank.TH, source.rankings.alexa.rank.TL, source.rankings.alexa.rank.TG, source.rankings.alexa.rank.TK, source.rankings.alexa.rank.TO, source.rankings.alexa.rank.TT, source.rankings.alexa.rank.TN, source.rankings.alexa.rank.TR, source.rankings.alexa.rank.TM, source.rankings.alexa.rank.TC, source.rankings.alexa.rank.TV, source.rankings.alexa.rank.UG, source.rankings.alexa.rank.UA, source.rankings.alexa.rank.AE, source.rankings.alexa.rank.GB, source.rankings.alexa.rank.US, source.rankings.alexa.rank.UM, source.rankings.alexa.rank.UY, source.rankings.alexa.rank.UZ, source.rankings.alexa.rank.VU, source.rankings.alexa.rank.VE, source.rankings.alexa.rank.VN, source.rankings.alexa.rank.VG, source.rankings.alexa.rank.VI, source.rankings.alexa.rank.WF, source.rankings.alexa.rank.EH, source.rankings.alexa.rank.YE, source.rankings.alexa.rank.ZM, source.rankings.alexa.rank.ZW]

### Return type

[**Histograms**](Histograms.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_related_stories**
> RelatedStories list_related_stories(id=id, not_id=not_id, title=title, body=body, text=text, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_level=categories_level, not_categories_level=not_categories_level, entities_title_text=entities_title_text, not_entities_title_text=not_entities_title_text, entities_title_type=entities_title_type, not_entities_title_type=not_entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, not_entities_title_links_dbpedia=not_entities_title_links_dbpedia, entities_body_text=entities_body_text, not_entities_body_text=not_entities_body_text, entities_body_type=entities_body_type, not_entities_body_type=not_entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, not_entities_body_links_dbpedia=not_entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, boost_by=boost_by, story_language=story_language, per_page=per_page)

List related stories

This endpoint is used for finding related stories based on the parameters provided. The maximum number of related stories returned is 100.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()


opts = { 
    'id': [56],
    'not_id': [56],
    'title': 'title_example',
    'body': 'body_example',
    'text': 'text_example',
    'language': ['language_example'],
    'not_language': ['not_language_example'],
    'published_at_start': 'published_at_start_example',
    'published_at_end': 'published_at_end_example',
    'categories_taxonomy': 'categories_taxonomy_example',
    'categories_confident': true,
    'categories_id': ['categories_id_example'],
    'not_categories_id': ['not_categories_id_example'],
    'categories_level': [56],
    'not_categories_level': [56],
    'entities_title_text': ['entities_title_text_example'],
    'not_entities_title_text': ['not_entities_title_text_example'],
    'entities_title_type': ['entities_title_type_example'],
    'not_entities_title_type': ['not_entities_title_type_example'],
    'entities_title_links_dbpedia': ['entities_title_links_dbpedia_example'],
    'not_entities_title_links_dbpedia': ['not_entities_title_links_dbpedia_example'],
    'entities_body_text': ['entities_body_text_example'],
    'not_entities_body_text': ['not_entities_body_text_example'],
    'entities_body_type': ['entities_body_type_example'],
    'not_entities_body_type': ['not_entities_body_type_example'],
    'entities_body_links_dbpedia': ['entities_body_links_dbpedia_example'],
    'not_entities_body_links_dbpedia': ['not_entities_body_links_dbpedia_example'],
    'sentiment_title_polarity': 'sentiment_title_polarity_example',
    'not_sentiment_title_polarity': 'not_sentiment_title_polarity_example',
    'sentiment_body_polarity': 'sentiment_body_polarity_example',
    'not_sentiment_body_polarity': 'not_sentiment_body_polarity_example',
    'media_images_count_min': 56,
    'media_images_count_max': 56,
    'media_images_width_min': 56,
    'media_images_width_max': 56,
    'media_images_height_min': 56,
    'media_images_height_max': 56,
    'media_images_content_length_min': 56,
    'media_images_content_length_max': 56,
    'media_images_format': ['media_images_format_example'],
    'not_media_images_format': ['not_media_images_format_example'],
    'media_videos_count_min': 56,
    'media_videos_count_max': 56,
    'author_id': [56],
    'not_author_id': [56],
    'author_name': 'author_name_example',
    'not_author_name': 'not_author_name_example',
    'source_id': [56],
    'not_source_id': [56],
    'source_name': ['source_name_example'],
    'not_source_name': ['not_source_name_example'],
    'source_domain': ['source_domain_example'],
    'not_source_domain': ['not_source_domain_example'],
    'source_locations_country': ['source_locations_country_example'],
    'not_source_locations_country': ['not_source_locations_country_example'],
    'source_locations_state': ['source_locations_state_example'],
    'not_source_locations_state': ['not_source_locations_state_example'],
    'source_locations_city': ['source_locations_city_example'],
    'not_source_locations_city': ['not_source_locations_city_example'],
    'source_scopes_country': ['source_scopes_country_example'],
    'not_source_scopes_country': ['not_source_scopes_country_example'],
    'source_scopes_state': ['source_scopes_state_example'],
    'not_source_scopes_state': ['not_source_scopes_state_example'],
    'source_scopes_city': ['source_scopes_city_example'],
    'not_source_scopes_city': ['not_source_scopes_city_example'],
    'source_scopes_level': ['source_scopes_level_example'],
    'not_source_scopes_level': ['not_source_scopes_level_example'],
    'source_links_in_count_min': 56,
    'source_links_in_count_max': 56,
    'source_rankings_alexa_rank_min': 56,
    'source_rankings_alexa_rank_max': 56,
    'source_rankings_alexa_country': ['source_rankings_alexa_country_example'],
    'social_shares_count_facebook_min': 56,
    'social_shares_count_facebook_max': 56,
    'social_shares_count_google_plus_min': 56,
    'social_shares_count_google_plus_max': 56,
    'social_shares_count_linkedin_min': 56,
    'social_shares_count_linkedin_max': 56,
    'social_shares_count_reddit_min': 56,
    'social_shares_count_reddit_max': 56,
    'cluster': false,
    'cluster_algorithm': 'lingo',
    '_return': ['_return_example'],
    'story_id': 789,
    'story_url': 'story_url_example',
    'story_title': 'story_title_example',
    'story_body': 'story_body_example',
    'boost_by': 'boost_by_example',
    'story_language': 'auto',
    'per_page': 3
}

try: 
    # List related stories
    api_response = api_instance.list_related_stories(**opts)
    pprint(api_response)
except ApiException as e:
    pprint("Exception when calling DefaultApi->list_related_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **list[int]**| This parameter is used for finding stories by story id. | [optional] 
 **not_id** | **list[int]**| This parameter is used for excluding stories by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | **list[str]**| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **not_language** | **list[str]**| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional]  [enum: iab-qag, iptc-subjectcode]
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] [default to true]
 **categories_id** | **list[str]**| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_id** | **list[str]**| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **categories_level** | **list[int]**| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_level** | **list[int]**| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **entities_title_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value. | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value. | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value. | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value. | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value. | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value. | [optional] 
 **media_images_format** | **list[str]**| This parameter is used for finding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **not_media_images_format** | **list[str]**| This parameter is used for excluding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | **list[int]**| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **not_author_id** | **list[int]**| This parameter is used for excluding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value. | [optional] 
 **source_id** | **list[int]**| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **not_source_id** | **list[int]**| This parameter is used for excluding stories whose source id is the specified value. | [optional] 
 **source_name** | **list[str]**| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **not_source_name** | **list[str]**| This parameter is used for excluding stories whose source name contains the specified value. | [optional] 
 **source_domain** | **list[str]**| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **not_source_domain** | **list[str]**| This parameter is used for excluding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | **list[str]**| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_country** | **list[str]**| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | **list[str]**| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_state** | **list[str]**| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | **list[str]**| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_city** | **list[str]**| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | **list[str]**| This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_country** | **list[str]**| This parameter is used for excluding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_state** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_city** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | **list[str]**| This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **not_source_scopes_level** | **list[str]**| This parameter is used for excluding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | **list[str]**| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value. | [optional] 
 **cluster** | **bool**| This parameter enables clustering for the returned stories. You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering). | [optional] [default to false]
 **cluster_algorithm** | **str**| This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering). | [optional] [default to lingo] [enum: stc, lingo, kmeans]
 **_return** | **list[str]**| This parameter is used for specifying return fields. | [optional]  [enum: id, title, body, summary, source, author, entities, keywords, hashtags, characters_count, words_count, sentences_count, paragraphs_count, categories, social_shares_count, media, sentiment, language, published_at, links]
 **story_id** | **int**| A story id | [optional] 
 **story_url** | **str**| An article or webpage | [optional] 
 **story_title** | **str**| Title of the article | [optional] 
 **story_body** | **str**| Body of the article | [optional] 
 **boost_by** | **str**| This parameter is used for boosting the result by the specified value. | [optional]  [enum: recency, popularity]
 **story_language** | **str**| This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] [default to auto] [enum: auto, en, de, fr, it, es, pt]
 **per_page** | **int**| This parameter is used for specifying number of items in each page. | [optional] [default to 3]

### Return type

[**RelatedStories**](RelatedStories.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_stories**
> Stories list_stories(id=id, not_id=not_id, title=title, body=body, text=text, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_level=categories_level, not_categories_level=not_categories_level, entities_title_text=entities_title_text, not_entities_title_text=not_entities_title_text, entities_title_type=entities_title_type, not_entities_title_type=not_entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, not_entities_title_links_dbpedia=not_entities_title_links_dbpedia, entities_body_text=entities_body_text, not_entities_body_text=not_entities_body_text, entities_body_type=entities_body_type, not_entities_body_type=not_entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, not_entities_body_links_dbpedia=not_entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)

List Stories

This endpoint is used for getting a list of stories.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()


opts = { 
    'id': [56],
    'not_id': [56],
    'title': 'title_example',
    'body': 'body_example',
    'text': 'text_example',
    'language': ['language_example'],
    'not_language': ['not_language_example'],
    'published_at_start': 'published_at_start_example',
    'published_at_end': 'published_at_end_example',
    'categories_taxonomy': 'categories_taxonomy_example',
    'categories_confident': true,
    'categories_id': ['categories_id_example'],
    'not_categories_id': ['not_categories_id_example'],
    'categories_level': [56],
    'not_categories_level': [56],
    'entities_title_text': ['entities_title_text_example'],
    'not_entities_title_text': ['not_entities_title_text_example'],
    'entities_title_type': ['entities_title_type_example'],
    'not_entities_title_type': ['not_entities_title_type_example'],
    'entities_title_links_dbpedia': ['entities_title_links_dbpedia_example'],
    'not_entities_title_links_dbpedia': ['not_entities_title_links_dbpedia_example'],
    'entities_body_text': ['entities_body_text_example'],
    'not_entities_body_text': ['not_entities_body_text_example'],
    'entities_body_type': ['entities_body_type_example'],
    'not_entities_body_type': ['not_entities_body_type_example'],
    'entities_body_links_dbpedia': ['entities_body_links_dbpedia_example'],
    'not_entities_body_links_dbpedia': ['not_entities_body_links_dbpedia_example'],
    'sentiment_title_polarity': 'sentiment_title_polarity_example',
    'not_sentiment_title_polarity': 'not_sentiment_title_polarity_example',
    'sentiment_body_polarity': 'sentiment_body_polarity_example',
    'not_sentiment_body_polarity': 'not_sentiment_body_polarity_example',
    'media_images_count_min': 56,
    'media_images_count_max': 56,
    'media_images_width_min': 56,
    'media_images_width_max': 56,
    'media_images_height_min': 56,
    'media_images_height_max': 56,
    'media_images_content_length_min': 56,
    'media_images_content_length_max': 56,
    'media_images_format': ['media_images_format_example'],
    'not_media_images_format': ['not_media_images_format_example'],
    'media_videos_count_min': 56,
    'media_videos_count_max': 56,
    'author_id': [56],
    'not_author_id': [56],
    'author_name': 'author_name_example',
    'not_author_name': 'not_author_name_example',
    'source_id': [56],
    'not_source_id': [56],
    'source_name': ['source_name_example'],
    'not_source_name': ['not_source_name_example'],
    'source_domain': ['source_domain_example'],
    'not_source_domain': ['not_source_domain_example'],
    'source_locations_country': ['source_locations_country_example'],
    'not_source_locations_country': ['not_source_locations_country_example'],
    'source_locations_state': ['source_locations_state_example'],
    'not_source_locations_state': ['not_source_locations_state_example'],
    'source_locations_city': ['source_locations_city_example'],
    'not_source_locations_city': ['not_source_locations_city_example'],
    'source_scopes_country': ['source_scopes_country_example'],
    'not_source_scopes_country': ['not_source_scopes_country_example'],
    'source_scopes_state': ['source_scopes_state_example'],
    'not_source_scopes_state': ['not_source_scopes_state_example'],
    'source_scopes_city': ['source_scopes_city_example'],
    'not_source_scopes_city': ['not_source_scopes_city_example'],
    'source_scopes_level': ['source_scopes_level_example'],
    'not_source_scopes_level': ['not_source_scopes_level_example'],
    'source_links_in_count_min': 56,
    'source_links_in_count_max': 56,
    'source_rankings_alexa_rank_min': 56,
    'source_rankings_alexa_rank_max': 56,
    'source_rankings_alexa_country': ['source_rankings_alexa_country_example'],
    'social_shares_count_facebook_min': 56,
    'social_shares_count_facebook_max': 56,
    'social_shares_count_google_plus_min': 56,
    'social_shares_count_google_plus_max': 56,
    'social_shares_count_linkedin_min': 56,
    'social_shares_count_linkedin_max': 56,
    'social_shares_count_reddit_min': 56,
    'social_shares_count_reddit_max': 56,
    'cluster': false,
    'cluster_algorithm': 'lingo',
    '_return': ['_return_example'],
    'sort_by': 'published_at',
    'sort_direction': 'desc',
    'cursor': '*',
    'per_page': 10
}

try: 
    # List Stories
    api_response = api_instance.list_stories(**opts)
    pprint(api_response)
except ApiException as e:
    pprint("Exception when calling DefaultApi->list_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **list[int]**| This parameter is used for finding stories by story id. | [optional] 
 **not_id** | **list[int]**| This parameter is used for excluding stories by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | **list[str]**| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **not_language** | **list[str]**| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional]  [enum: iab-qag, iptc-subjectcode]
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] [default to true]
 **categories_id** | **list[str]**| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_id** | **list[str]**| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **categories_level** | **list[int]**| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_level** | **list[int]**| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **entities_title_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value. | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value. | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value. | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value. | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value. | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value. | [optional] 
 **media_images_format** | **list[str]**| This parameter is used for finding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **not_media_images_format** | **list[str]**| This parameter is used for excluding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | **list[int]**| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **not_author_id** | **list[int]**| This parameter is used for excluding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value. | [optional] 
 **source_id** | **list[int]**| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **not_source_id** | **list[int]**| This parameter is used for excluding stories whose source id is the specified value. | [optional] 
 **source_name** | **list[str]**| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **not_source_name** | **list[str]**| This parameter is used for excluding stories whose source name contains the specified value. | [optional] 
 **source_domain** | **list[str]**| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **not_source_domain** | **list[str]**| This parameter is used for excluding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | **list[str]**| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_country** | **list[str]**| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | **list[str]**| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_state** | **list[str]**| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | **list[str]**| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_city** | **list[str]**| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_country** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_state** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_city** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **not_source_scopes_level** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | **list[str]**| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value. | [optional] 
 **cluster** | **bool**| This parameter enables clustering for the returned stories. You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering). | [optional] [default to false]
 **cluster_algorithm** | **str**| This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering). | [optional] [default to lingo] [enum: stc, lingo, kmeans]
 **_return** | **list[str]**| This parameter is used for specifying return fields. | [optional]  [enum: id, title, body, summary, source, author, entities, keywords, hashtags, characters_count, words_count, sentences_count, paragraphs_count, categories, social_shares_count, media, sentiment, language, published_at, links]
 **sort_by** | **str**| This parameter is used for changing the order column of the results. | [optional] [default to published_at] [enum: relevance, recency, hotness, published_at, social_shares_count, social_shares_count.facebook, social_shares_count.linkedin, social_shares_count.google_plus, social_shares_count.reddit, media.images.count, media.videos.count, source.links_in_count, source.rankings.alexa.rank, source.rankings.alexa.rank.AF, source.rankings.alexa.rank.AX, source.rankings.alexa.rank.AL, source.rankings.alexa.rank.DZ, source.rankings.alexa.rank.AS, source.rankings.alexa.rank.AD, source.rankings.alexa.rank.AO, source.rankings.alexa.rank.AI, source.rankings.alexa.rank.AQ, source.rankings.alexa.rank.AG, source.rankings.alexa.rank.AR, source.rankings.alexa.rank.AM, source.rankings.alexa.rank.AW, source.rankings.alexa.rank.AU, source.rankings.alexa.rank.AT, source.rankings.alexa.rank.AZ, source.rankings.alexa.rank.BS, source.rankings.alexa.rank.BH, source.rankings.alexa.rank.BD, source.rankings.alexa.rank.BB, source.rankings.alexa.rank.BY, source.rankings.alexa.rank.BE, source.rankings.alexa.rank.BZ, source.rankings.alexa.rank.BJ, source.rankings.alexa.rank.BM, source.rankings.alexa.rank.BT, source.rankings.alexa.rank.BO, source.rankings.alexa.rank.BQ, source.rankings.alexa.rank.BA, source.rankings.alexa.rank.BW, source.rankings.alexa.rank.BV, source.rankings.alexa.rank.BR, source.rankings.alexa.rank.IO, source.rankings.alexa.rank.BN, source.rankings.alexa.rank.BG, source.rankings.alexa.rank.BF, source.rankings.alexa.rank.BI, source.rankings.alexa.rank.KH, source.rankings.alexa.rank.CM, source.rankings.alexa.rank.CA, source.rankings.alexa.rank.CV, source.rankings.alexa.rank.KY, source.rankings.alexa.rank.CF, source.rankings.alexa.rank.TD, source.rankings.alexa.rank.CL, source.rankings.alexa.rank.CN, source.rankings.alexa.rank.CX, source.rankings.alexa.rank.CC, source.rankings.alexa.rank.CO, source.rankings.alexa.rank.KM, source.rankings.alexa.rank.CG, source.rankings.alexa.rank.CD, source.rankings.alexa.rank.CK, source.rankings.alexa.rank.CR, source.rankings.alexa.rank.CI, source.rankings.alexa.rank.HR, source.rankings.alexa.rank.CU, source.rankings.alexa.rank.CW, source.rankings.alexa.rank.CY, source.rankings.alexa.rank.CZ, source.rankings.alexa.rank.DK, source.rankings.alexa.rank.DJ, source.rankings.alexa.rank.DM, source.rankings.alexa.rank.DO, source.rankings.alexa.rank.EC, source.rankings.alexa.rank.EG, source.rankings.alexa.rank.SV, source.rankings.alexa.rank.GQ, source.rankings.alexa.rank.ER, source.rankings.alexa.rank.EE, source.rankings.alexa.rank.ET, source.rankings.alexa.rank.FK, source.rankings.alexa.rank.FO, source.rankings.alexa.rank.FJ, source.rankings.alexa.rank.FI, source.rankings.alexa.rank.FR, source.rankings.alexa.rank.GF, source.rankings.alexa.rank.PF, source.rankings.alexa.rank.TF, source.rankings.alexa.rank.GA, source.rankings.alexa.rank.GM, source.rankings.alexa.rank.GE, source.rankings.alexa.rank.DE, source.rankings.alexa.rank.GH, source.rankings.alexa.rank.GI, source.rankings.alexa.rank.GR, source.rankings.alexa.rank.GL, source.rankings.alexa.rank.GD, source.rankings.alexa.rank.GP, source.rankings.alexa.rank.GU, source.rankings.alexa.rank.GT, source.rankings.alexa.rank.GG, source.rankings.alexa.rank.GN, source.rankings.alexa.rank.GW, source.rankings.alexa.rank.GY, source.rankings.alexa.rank.HT, source.rankings.alexa.rank.HM, source.rankings.alexa.rank.VA, source.rankings.alexa.rank.HN, source.rankings.alexa.rank.HK, source.rankings.alexa.rank.HU, source.rankings.alexa.rank.IS, source.rankings.alexa.rank.IN, source.rankings.alexa.rank.ID, source.rankings.alexa.rank.IR, source.rankings.alexa.rank.IQ, source.rankings.alexa.rank.IE, source.rankings.alexa.rank.IM, source.rankings.alexa.rank.IL, source.rankings.alexa.rank.IT, source.rankings.alexa.rank.JM, source.rankings.alexa.rank.JP, source.rankings.alexa.rank.JE, source.rankings.alexa.rank.JO, source.rankings.alexa.rank.KZ, source.rankings.alexa.rank.KE, source.rankings.alexa.rank.KI, source.rankings.alexa.rank.KP, source.rankings.alexa.rank.KR, source.rankings.alexa.rank.KW, source.rankings.alexa.rank.KG, source.rankings.alexa.rank.LA, source.rankings.alexa.rank.LV, source.rankings.alexa.rank.LB, source.rankings.alexa.rank.LS, source.rankings.alexa.rank.LR, source.rankings.alexa.rank.LY, source.rankings.alexa.rank.LI, source.rankings.alexa.rank.LT, source.rankings.alexa.rank.LU, source.rankings.alexa.rank.MO, source.rankings.alexa.rank.MK, source.rankings.alexa.rank.MG, source.rankings.alexa.rank.MW, source.rankings.alexa.rank.MY, source.rankings.alexa.rank.MV, source.rankings.alexa.rank.ML, source.rankings.alexa.rank.MT, source.rankings.alexa.rank.MH, source.rankings.alexa.rank.MQ, source.rankings.alexa.rank.MR, source.rankings.alexa.rank.MU, source.rankings.alexa.rank.YT, source.rankings.alexa.rank.MX, source.rankings.alexa.rank.FM, source.rankings.alexa.rank.MD, source.rankings.alexa.rank.MC, source.rankings.alexa.rank.MN, source.rankings.alexa.rank.ME, source.rankings.alexa.rank.MS, source.rankings.alexa.rank.MA, source.rankings.alexa.rank.MZ, source.rankings.alexa.rank.MM, source.rankings.alexa.rank.NA, source.rankings.alexa.rank.NR, source.rankings.alexa.rank.NP, source.rankings.alexa.rank.NL, source.rankings.alexa.rank.NC, source.rankings.alexa.rank.NZ, source.rankings.alexa.rank.NI, source.rankings.alexa.rank.NE, source.rankings.alexa.rank.NG, source.rankings.alexa.rank.NU, source.rankings.alexa.rank.NF, source.rankings.alexa.rank.MP, source.rankings.alexa.rank.NO, source.rankings.alexa.rank.OM, source.rankings.alexa.rank.PK, source.rankings.alexa.rank.PW, source.rankings.alexa.rank.PS, source.rankings.alexa.rank.PA, source.rankings.alexa.rank.PG, source.rankings.alexa.rank.PY, source.rankings.alexa.rank.PE, source.rankings.alexa.rank.PH, source.rankings.alexa.rank.PN, source.rankings.alexa.rank.PL, source.rankings.alexa.rank.PT, source.rankings.alexa.rank.PR, source.rankings.alexa.rank.QA, source.rankings.alexa.rank.RE, source.rankings.alexa.rank.RO, source.rankings.alexa.rank.RU, source.rankings.alexa.rank.RW, source.rankings.alexa.rank.BL, source.rankings.alexa.rank.SH, source.rankings.alexa.rank.KN, source.rankings.alexa.rank.LC, source.rankings.alexa.rank.MF, source.rankings.alexa.rank.PM, source.rankings.alexa.rank.VC, source.rankings.alexa.rank.WS, source.rankings.alexa.rank.SM, source.rankings.alexa.rank.ST, source.rankings.alexa.rank.SA, source.rankings.alexa.rank.SN, source.rankings.alexa.rank.RS, source.rankings.alexa.rank.SC, source.rankings.alexa.rank.SL, source.rankings.alexa.rank.SG, source.rankings.alexa.rank.SX, source.rankings.alexa.rank.SK, source.rankings.alexa.rank.SI, source.rankings.alexa.rank.SB, source.rankings.alexa.rank.SO, source.rankings.alexa.rank.ZA, source.rankings.alexa.rank.GS, source.rankings.alexa.rank.SS, source.rankings.alexa.rank.ES, source.rankings.alexa.rank.LK, source.rankings.alexa.rank.SD, source.rankings.alexa.rank.SR, source.rankings.alexa.rank.SJ, source.rankings.alexa.rank.SZ, source.rankings.alexa.rank.SE, source.rankings.alexa.rank.CH, source.rankings.alexa.rank.SY, source.rankings.alexa.rank.TW, source.rankings.alexa.rank.TJ, source.rankings.alexa.rank.TZ, source.rankings.alexa.rank.TH, source.rankings.alexa.rank.TL, source.rankings.alexa.rank.TG, source.rankings.alexa.rank.TK, source.rankings.alexa.rank.TO, source.rankings.alexa.rank.TT, source.rankings.alexa.rank.TN, source.rankings.alexa.rank.TR, source.rankings.alexa.rank.TM, source.rankings.alexa.rank.TC, source.rankings.alexa.rank.TV, source.rankings.alexa.rank.UG, source.rankings.alexa.rank.UA, source.rankings.alexa.rank.AE, source.rankings.alexa.rank.GB, source.rankings.alexa.rank.US, source.rankings.alexa.rank.UM, source.rankings.alexa.rank.UY, source.rankings.alexa.rank.UZ, source.rankings.alexa.rank.VU, source.rankings.alexa.rank.VE, source.rankings.alexa.rank.VN, source.rankings.alexa.rank.VG, source.rankings.alexa.rank.VI, source.rankings.alexa.rank.WF, source.rankings.alexa.rank.EH, source.rankings.alexa.rank.YE, source.rankings.alexa.rank.ZM, source.rankings.alexa.rank.ZW]
 **sort_direction** | **str**| This parameter is used for changing the order direction of the result. | [optional] [default to desc] [enum: asc, desc]
 **cursor** | **str**| This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results). | [optional] [default to *]
 **per_page** | **int**| This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results) | [optional] [default to 10]

### Return type

[**Stories**](Stories.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_time_series**
> TimeSeriesList list_time_series(id=id, not_id=not_id, title=title, body=body, text=text, language=language, not_language=not_language, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_level=categories_level, not_categories_level=not_categories_level, entities_title_text=entities_title_text, not_entities_title_text=not_entities_title_text, entities_title_type=entities_title_type, not_entities_title_type=not_entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, not_entities_title_links_dbpedia=not_entities_title_links_dbpedia, entities_body_text=entities_body_text, not_entities_body_text=not_entities_body_text, entities_body_type=entities_body_type, not_entities_body_type=not_entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, not_entities_body_links_dbpedia=not_entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, published_at_start=published_at_start, published_at_end=published_at_end, period=period)

List time series

This endpoint is used for getting time series by stories.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()


opts = { 
    'id': [56],
    'not_id': [56],
    'title': 'title_example',
    'body': 'body_example',
    'text': 'text_example',
    'language': ['language_example'],
    'not_language': ['not_language_example'],
    'categories_taxonomy': 'categories_taxonomy_example',
    'categories_confident': true,
    'categories_id': ['categories_id_example'],
    'not_categories_id': ['not_categories_id_example'],
    'categories_level': [56],
    'not_categories_level': [56],
    'entities_title_text': ['entities_title_text_example'],
    'not_entities_title_text': ['not_entities_title_text_example'],
    'entities_title_type': ['entities_title_type_example'],
    'not_entities_title_type': ['not_entities_title_type_example'],
    'entities_title_links_dbpedia': ['entities_title_links_dbpedia_example'],
    'not_entities_title_links_dbpedia': ['not_entities_title_links_dbpedia_example'],
    'entities_body_text': ['entities_body_text_example'],
    'not_entities_body_text': ['not_entities_body_text_example'],
    'entities_body_type': ['entities_body_type_example'],
    'not_entities_body_type': ['not_entities_body_type_example'],
    'entities_body_links_dbpedia': ['entities_body_links_dbpedia_example'],
    'not_entities_body_links_dbpedia': ['not_entities_body_links_dbpedia_example'],
    'sentiment_title_polarity': 'sentiment_title_polarity_example',
    'not_sentiment_title_polarity': 'not_sentiment_title_polarity_example',
    'sentiment_body_polarity': 'sentiment_body_polarity_example',
    'not_sentiment_body_polarity': 'not_sentiment_body_polarity_example',
    'media_images_count_min': 56,
    'media_images_count_max': 56,
    'media_images_width_min': 56,
    'media_images_width_max': 56,
    'media_images_height_min': 56,
    'media_images_height_max': 56,
    'media_images_content_length_min': 56,
    'media_images_content_length_max': 56,
    'media_images_format': ['media_images_format_example'],
    'not_media_images_format': ['not_media_images_format_example'],
    'media_videos_count_min': 56,
    'media_videos_count_max': 56,
    'author_id': [56],
    'not_author_id': [56],
    'author_name': 'author_name_example',
    'not_author_name': 'not_author_name_example',
    'source_id': [56],
    'not_source_id': [56],
    'source_name': ['source_name_example'],
    'not_source_name': ['not_source_name_example'],
    'source_domain': ['source_domain_example'],
    'not_source_domain': ['not_source_domain_example'],
    'source_locations_country': ['source_locations_country_example'],
    'not_source_locations_country': ['not_source_locations_country_example'],
    'source_locations_state': ['source_locations_state_example'],
    'not_source_locations_state': ['not_source_locations_state_example'],
    'source_locations_city': ['source_locations_city_example'],
    'not_source_locations_city': ['not_source_locations_city_example'],
    'source_scopes_country': ['source_scopes_country_example'],
    'not_source_scopes_country': ['not_source_scopes_country_example'],
    'source_scopes_state': ['source_scopes_state_example'],
    'not_source_scopes_state': ['not_source_scopes_state_example'],
    'source_scopes_city': ['source_scopes_city_example'],
    'not_source_scopes_city': ['not_source_scopes_city_example'],
    'source_scopes_level': ['source_scopes_level_example'],
    'not_source_scopes_level': ['not_source_scopes_level_example'],
    'source_links_in_count_min': 56,
    'source_links_in_count_max': 56,
    'source_rankings_alexa_rank_min': 56,
    'source_rankings_alexa_rank_max': 56,
    'source_rankings_alexa_country': ['source_rankings_alexa_country_example'],
    'social_shares_count_facebook_min': 56,
    'social_shares_count_facebook_max': 56,
    'social_shares_count_google_plus_min': 56,
    'social_shares_count_google_plus_max': 56,
    'social_shares_count_linkedin_min': 56,
    'social_shares_count_linkedin_max': 56,
    'social_shares_count_reddit_min': 56,
    'social_shares_count_reddit_max': 56,
    'published_at_start': 'NOW-7DAYS/DAY',
    'published_at_end': 'NOW/DAY',
    'period': '+1DAY'
}

try: 
    # List time series
    api_response = api_instance.list_time_series(**opts)
    pprint(api_response)
except ApiException as e:
    pprint("Exception when calling DefaultApi->list_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **list[int]**| This parameter is used for finding stories by story id. | [optional] 
 **not_id** | **list[int]**| This parameter is used for excluding stories by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | **list[str]**| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **not_language** | **list[str]**| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional]  [enum: iab-qag, iptc-subjectcode]
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] [default to true]
 **categories_id** | **list[str]**| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_id** | **list[str]**| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **categories_level** | **list[int]**| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_level** | **list[int]**| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **entities_title_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value. | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value. | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value. | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value. | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value. | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value. | [optional] 
 **media_images_format** | **list[str]**| This parameter is used for finding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **not_media_images_format** | **list[str]**| This parameter is used for excluding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | **list[int]**| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **not_author_id** | **list[int]**| This parameter is used for excluding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value. | [optional] 
 **source_id** | **list[int]**| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **not_source_id** | **list[int]**| This parameter is used for excluding stories whose source id is the specified value. | [optional] 
 **source_name** | **list[str]**| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **not_source_name** | **list[str]**| This parameter is used for excluding stories whose source name contains the specified value. | [optional] 
 **source_domain** | **list[str]**| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **not_source_domain** | **list[str]**| This parameter is used for excluding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | **list[str]**| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_country** | **list[str]**| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | **list[str]**| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_state** | **list[str]**| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | **list[str]**| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_city** | **list[str]**| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_country** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_state** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_city** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **not_source_scopes_level** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | **list[str]**| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value. | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] [default to NOW-7DAYS/DAY]
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] [default to NOW/DAY]
 **period** | **str**| The size of each date range is expressed as an interval to be added to the lower bound. It supports Date Math Syntax. Valid options are &#x60;+&#x60; following an integer number greater than 0 and one of the Date Math keywords. e.g. &#x60;+1DAY&#x60;, &#x60;+2MINUTES&#x60; and &#x60;+1MONTH&#x60;. Here are [Supported keywords](https://newsapi.aylien.com/docs/working-with-dates#date-math). | [optional] [default to +1DAY]

### Return type

[**TimeSeriesList**](TimeSeriesList.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_trends**
> Trends list_trends(field, id=id, not_id=not_id, title=title, body=body, text=text, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_level=categories_level, not_categories_level=not_categories_level, entities_title_text=entities_title_text, not_entities_title_text=not_entities_title_text, entities_title_type=entities_title_type, not_entities_title_type=not_entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, not_entities_title_links_dbpedia=not_entities_title_links_dbpedia, entities_body_text=entities_body_text, not_entities_body_text=not_entities_body_text, entities_body_type=entities_body_type, not_entities_body_type=not_entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, not_entities_body_links_dbpedia=not_entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max)

List trends

This endpoint is used for finding trends based on stories.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

field = 'field_example'

opts = { 
    'id': [56],
    'not_id': [56],
    'title': 'title_example',
    'body': 'body_example',
    'text': 'text_example',
    'language': ['language_example'],
    'not_language': ['not_language_example'],
    'published_at_start': 'published_at_start_example',
    'published_at_end': 'published_at_end_example',
    'categories_taxonomy': 'categories_taxonomy_example',
    'categories_confident': true,
    'categories_id': ['categories_id_example'],
    'not_categories_id': ['not_categories_id_example'],
    'categories_level': [56],
    'not_categories_level': [56],
    'entities_title_text': ['entities_title_text_example'],
    'not_entities_title_text': ['not_entities_title_text_example'],
    'entities_title_type': ['entities_title_type_example'],
    'not_entities_title_type': ['not_entities_title_type_example'],
    'entities_title_links_dbpedia': ['entities_title_links_dbpedia_example'],
    'not_entities_title_links_dbpedia': ['not_entities_title_links_dbpedia_example'],
    'entities_body_text': ['entities_body_text_example'],
    'not_entities_body_text': ['not_entities_body_text_example'],
    'entities_body_type': ['entities_body_type_example'],
    'not_entities_body_type': ['not_entities_body_type_example'],
    'entities_body_links_dbpedia': ['entities_body_links_dbpedia_example'],
    'not_entities_body_links_dbpedia': ['not_entities_body_links_dbpedia_example'],
    'sentiment_title_polarity': 'sentiment_title_polarity_example',
    'not_sentiment_title_polarity': 'not_sentiment_title_polarity_example',
    'sentiment_body_polarity': 'sentiment_body_polarity_example',
    'not_sentiment_body_polarity': 'not_sentiment_body_polarity_example',
    'media_images_count_min': 56,
    'media_images_count_max': 56,
    'media_images_width_min': 56,
    'media_images_width_max': 56,
    'media_images_height_min': 56,
    'media_images_height_max': 56,
    'media_images_content_length_min': 56,
    'media_images_content_length_max': 56,
    'media_images_format': ['media_images_format_example'],
    'not_media_images_format': ['not_media_images_format_example'],
    'media_videos_count_min': 56,
    'media_videos_count_max': 56,
    'author_id': [56],
    'not_author_id': [56],
    'author_name': 'author_name_example',
    'not_author_name': 'not_author_name_example',
    'source_id': [56],
    'not_source_id': [56],
    'source_name': ['source_name_example'],
    'not_source_name': ['not_source_name_example'],
    'source_domain': ['source_domain_example'],
    'not_source_domain': ['not_source_domain_example'],
    'source_locations_country': ['source_locations_country_example'],
    'not_source_locations_country': ['not_source_locations_country_example'],
    'source_locations_state': ['source_locations_state_example'],
    'not_source_locations_state': ['not_source_locations_state_example'],
    'source_locations_city': ['source_locations_city_example'],
    'not_source_locations_city': ['not_source_locations_city_example'],
    'source_scopes_country': ['source_scopes_country_example'],
    'not_source_scopes_country': ['not_source_scopes_country_example'],
    'source_scopes_state': ['source_scopes_state_example'],
    'not_source_scopes_state': ['not_source_scopes_state_example'],
    'source_scopes_city': ['source_scopes_city_example'],
    'not_source_scopes_city': ['not_source_scopes_city_example'],
    'source_scopes_level': ['source_scopes_level_example'],
    'not_source_scopes_level': ['not_source_scopes_level_example'],
    'source_links_in_count_min': 56,
    'source_links_in_count_max': 56,
    'source_rankings_alexa_rank_min': 56,
    'source_rankings_alexa_rank_max': 56,
    'source_rankings_alexa_country': ['source_rankings_alexa_country_example'],
    'social_shares_count_facebook_min': 56,
    'social_shares_count_facebook_max': 56,
    'social_shares_count_google_plus_min': 56,
    'social_shares_count_google_plus_max': 56,
    'social_shares_count_linkedin_min': 56,
    'social_shares_count_linkedin_max': 56,
    'social_shares_count_reddit_min': 56,
    'social_shares_count_reddit_max': 56
}

try: 
    # List trends
    api_response = api_instance.list_trends(field, **opts)
    pprint(api_response)
except ApiException as e:
    pprint("Exception when calling DefaultApi->list_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| This parameter is used to specify the trend field. |  [enum: author.name, source.name, source.domain, keywords, entities.title.text, entities.title.type, entities.title.links.dbpedia, entities.body.text, entities.body.type, entities.body.links.dbpedia, hashtags, categories.id, sentiment.title.polarity, sentiment.body.polarity]
 **id** | **list[int]**| This parameter is used for finding stories by story id. | [optional] 
 **not_id** | **list[int]**| This parameter is used for excluding stories by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | **list[str]**| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **not_language** | **list[str]**| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional]  [enum: en, de, fr, it, es, pt]
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional]  [enum: iab-qag, iptc-subjectcode]
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] [default to true]
 **categories_id** | **list[str]**| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_id** | **list[str]**| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **categories_level** | **list[int]**| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **not_categories_level** | **list[int]**| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories). | [optional] 
 **entities_title_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_title_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_title_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_text** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_text** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;text&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_type** | **list[str]**| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_type** | **list[str]**| This parameter is used to exclude stories based on the specified entities &#x60;type&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **entities_body_links_dbpedia** | **list[str]**| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **not_entities_body_links_dbpedia** | **list[str]**| This parameter is used to exclude stories based on the specified entities dbpedia URL in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities). | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value. | [optional]  [enum: positive, neutral, negative]
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value. | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value. | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value. | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value. | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value. | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value. | [optional] 
 **media_images_format** | **list[str]**| This parameter is used for finding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **not_media_images_format** | **list[str]**| This parameter is used for excluding stories whose images format are the specified value. | [optional]  [enum: BMP, GIF, JPEG, PNG, TIFF, PSD, ICO, CUR, WEBP, SVG]
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | **list[int]**| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **not_author_id** | **list[int]**| This parameter is used for excluding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value. | [optional] 
 **source_id** | **list[int]**| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **not_source_id** | **list[int]**| This parameter is used for excluding stories whose source id is the specified value. | [optional] 
 **source_name** | **list[str]**| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **not_source_name** | **list[str]**| This parameter is used for excluding stories whose source name contains the specified value. | [optional] 
 **source_domain** | **list[str]**| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **not_source_domain** | **list[str]**| This parameter is used for excluding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | **list[str]**| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_country** | **list[str]**| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | **list[str]**| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_state** | **list[str]**| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | **list[str]**| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_locations_city** | **list[str]**| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_country** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_state** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **not_source_scopes_city** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | **list[str]**| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **not_source_scopes_level** | **list[str]**| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional]  [enum: international, national, local]
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | **list[str]**| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value. | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value. | [optional] 

### Return type

[**Trends**](Trends.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

