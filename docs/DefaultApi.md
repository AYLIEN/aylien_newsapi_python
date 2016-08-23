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

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

type = 'type_example' # str | This parameter is used for defining the type of autocompletes.
term = 'term_example' # str | This parameter is used for finding autocomplete objects that contain the specified value.
language = 'en' # str | This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional) (default to en)
per_page = 3 # int | This parameter is used for specifying number of items in each page. (optional) (default to 3)

try: 
    # List autocompletes
    api_response = api_instance.list_autocompletes(type, term, language=language, per_page=per_page)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_autocompletes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| This parameter is used for defining the type of autocompletes. | 
 **term** | **str**| This parameter is used for finding autocomplete objects that contain the specified value. | 
 **language** | **str**| This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] [default to en]
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
> Coverages list_coverages(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, story_published_at=story_published_at, story_language=story_language, per_page=per_page)

List coverages

This endpoint is used for finding story coverages based on the parameters provided. The maximum number of related stories returned is 100.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

id = [56] # list[int] | This parameter is used for finding stroies by story id. (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. (optional)
categories_confident = true # bool | This parameter is used for finding stories whose categories are confident. (optional) (default to true)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. (optional)
entities_title_text = ['entities_title_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in story titles. (optional)
entities_title_type = ['entities_title_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in story titles. (optional)
entities_title_links_dbpedia = ['entities_title_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in story titles. (optional)
entities_body_text = ['entities_body_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in the body of stories. (optional)
entities_body_type = ['entities_body_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in the body of stories. (optional)
entities_body_links_dbpedia = ['entities_body_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value. (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value. (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value. (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value. (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value. (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value. (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value. (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value. (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value. (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value. (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
cluster = false # bool | This parameter enables clustering for the returned stories. (optional) (default to false)
cluster_algorithm = 'lingo' # str | This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. (optional) (default to lingo)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
story_id = 789 # int | A story id (optional)
story_url = 'story_url_example' # str | An article or webpage (optional)
story_title = 'story_title_example' # str | Title of the article (optional)
story_body = 'story_body_example' # str | Body of the article (optional)
story_published_at = '2013-10-20T19:20:30+01:00' # datetime | Publish date of the article. If you use a url or title and body of an article for getting coverages, this parameter is required. The format used is a restricted form of the canonical representation of dateTime in the [XML Schema specification (ISO 8601)](https://www.w3.org/TR/xmlschema-2/#dateTime). (optional)
story_language = 'auto' # str | This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional) (default to auto)
per_page = 3 # int | This parameter is used for specifying number of items in each page. (optional) (default to 3)

try: 
    # List coverages
    api_response = api_instance.list_coverages(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, story_published_at=story_published_at, story_language=story_language, per_page=per_page)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_coverages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stroies by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. | [optional] [default to true]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. | [optional] 
 **entities_title_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. | [optional] 
 **entities_title_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. | [optional] 
 **entities_title_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. | [optional] 
 **entities_body_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. | [optional] 
 **entities_body_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. | [optional] 
 **entities_body_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **cluster** | **bool**| This parameter enables clustering for the returned stories. | [optional] [default to false]
 **cluster_algorithm** | **str**| This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. | [optional] [default to lingo]
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **story_id** | **int**| A story id | [optional] 
 **story_url** | **str**| An article or webpage | [optional] 
 **story_title** | **str**| Title of the article | [optional] 
 **story_body** | **str**| Body of the article | [optional] 
 **story_published_at** | **datetime**| Publish date of the article. If you use a url or title and body of an article for getting coverages, this parameter is required. The format used is a restricted form of the canonical representation of dateTime in the [XML Schema specification (ISO 8601)](https://www.w3.org/TR/xmlschema-2/#dateTime). | [optional] 
 **story_language** | **str**| This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] [default to auto]
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
> Histograms list_histograms(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, interval_start=interval_start, interval_end=interval_end, interval_width=interval_width, field=field)

List histograms

This endpoint is used for getting histograms based on the `field` parameter passed to the API.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

id = [56] # list[int] | This parameter is used for finding stroies by story id. (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. (optional)
categories_confident = true # bool | This parameter is used for finding stories whose categories are confident. (optional) (default to true)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. (optional)
entities_title_text = ['entities_title_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in story titles. (optional)
entities_title_type = ['entities_title_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in story titles. (optional)
entities_title_links_dbpedia = ['entities_title_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in story titles. (optional)
entities_body_text = ['entities_body_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in the body of stories. (optional)
entities_body_type = ['entities_body_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in the body of stories. (optional)
entities_body_links_dbpedia = ['entities_body_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value. (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value. (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value. (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value. (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value. (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value. (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value. (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value. (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value. (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value. (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
interval_start = 56 # int | This parameter is used for setting the start data point of histogram intervals. (optional)
interval_end = 56 # int | This parameter is used for setting the end data point of histogram intervals. (optional)
interval_width = 56 # int | This parameter is used for setting the width of histogram intervals. (optional)
field = 'social_shares_count' # str | This parameter is used for specifying the y-axis variable for the histogram. (optional) (default to social_shares_count)

try: 
    # List histograms
    api_response = api_instance.list_histograms(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, interval_start=interval_start, interval_end=interval_end, interval_width=interval_width, field=field)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_histograms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stroies by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. | [optional] [default to true]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. | [optional] 
 **entities_title_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. | [optional] 
 **entities_title_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. | [optional] 
 **entities_title_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. | [optional] 
 **entities_body_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. | [optional] 
 **entities_body_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. | [optional] 
 **entities_body_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **interval_start** | **int**| This parameter is used for setting the start data point of histogram intervals. | [optional] 
 **interval_end** | **int**| This parameter is used for setting the end data point of histogram intervals. | [optional] 
 **interval_width** | **int**| This parameter is used for setting the width of histogram intervals. | [optional] 
 **field** | **str**| This parameter is used for specifying the y-axis variable for the histogram. | [optional] [default to social_shares_count]

### Return type

[**Histograms**](Histograms.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_related_stories**
> RelatedStories list_related_stories(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, boost_by=boost_by, story_language=story_language, per_page=per_page)

List related stories

This endpoint is used for finding related stories based on the parameters provided. The maximum number of related stories returned is 100.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

id = [56] # list[int] | This parameter is used for finding stroies by story id. (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. (optional)
categories_confident = true # bool | This parameter is used for finding stories whose categories are confident. (optional) (default to true)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. (optional)
entities_title_text = ['entities_title_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in story titles. (optional)
entities_title_type = ['entities_title_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in story titles. (optional)
entities_title_links_dbpedia = ['entities_title_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in story titles. (optional)
entities_body_text = ['entities_body_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in the body of stories. (optional)
entities_body_type = ['entities_body_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in the body of stories. (optional)
entities_body_links_dbpedia = ['entities_body_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value. (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value. (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value. (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value. (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value. (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value. (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value. (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value. (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value. (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value. (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
cluster = false # bool | This parameter enables clustering for the returned stories. (optional) (default to false)
cluster_algorithm = 'lingo' # str | This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. (optional) (default to lingo)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
story_id = 789 # int | A story id (optional)
story_url = 'story_url_example' # str | An article or webpage (optional)
story_title = 'story_title_example' # str | Title of the article (optional)
story_body = 'story_body_example' # str | Body of the article (optional)
boost_by = 'boost_by_example' # str | This parameter is used for boosting the result by the specified value. (optional)
story_language = 'auto' # str | This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional) (default to auto)
per_page = 3 # int | This parameter is used for specifying number of items in each page. (optional) (default to 3)

try: 
    # List related stories
    api_response = api_instance.list_related_stories(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, boost_by=boost_by, story_language=story_language, per_page=per_page)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_related_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stroies by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. | [optional] [default to true]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. | [optional] 
 **entities_title_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. | [optional] 
 **entities_title_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. | [optional] 
 **entities_title_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. | [optional] 
 **entities_body_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. | [optional] 
 **entities_body_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. | [optional] 
 **entities_body_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes  is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes  is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **cluster** | **bool**| This parameter enables clustering for the returned stories. | [optional] [default to false]
 **cluster_algorithm** | **str**| This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. | [optional] [default to lingo]
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **story_id** | **int**| A story id | [optional] 
 **story_url** | **str**| An article or webpage | [optional] 
 **story_title** | **str**| Title of the article | [optional] 
 **story_body** | **str**| Body of the article | [optional] 
 **boost_by** | **str**| This parameter is used for boosting the result by the specified value. | [optional] 
 **story_language** | **str**| This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] [default to auto]
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
> Stories list_stories(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)

List Stories

This endpoint is used for getting a list of stories.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

id = [56] # list[int] | This parameter is used for finding stroies by story id. (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. (optional)
categories_confident = true # bool | This parameter is used for finding stories whose categories are confident. (optional) (default to true)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. (optional)
entities_title_text = ['entities_title_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in story titles. (optional)
entities_title_type = ['entities_title_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in story titles. (optional)
entities_title_links_dbpedia = ['entities_title_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in story titles. (optional)
entities_body_text = ['entities_body_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in the body of stories. (optional)
entities_body_type = ['entities_body_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in the body of stories. (optional)
entities_body_links_dbpedia = ['entities_body_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value. (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value. (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value. (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value. (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value. (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value. (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value. (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value. (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value. (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value. (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
cluster = false # bool | This parameter enables clustering for the returned stories. (optional) (default to false)
cluster_algorithm = 'lingo' # str | This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. (optional) (default to lingo)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. (optional) (default to published_at)
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. (optional) (default to desc)
cursor = '*' # str | This parameter is used for finding a specific page. (optional) (default to *)
per_page = 10 # int | This parameter is used for specifying number of items in each page. (optional) (default to 10)

try: 
    # List Stories
    api_response = api_instance.list_stories(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, cluster=cluster, cluster_algorithm=cluster_algorithm, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stroies by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. | [optional] [default to true]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. | [optional] 
 **entities_title_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. | [optional] 
 **entities_title_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. | [optional] 
 **entities_title_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. | [optional] 
 **entities_body_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. | [optional] 
 **entities_body_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. | [optional] 
 **entities_body_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **cluster** | **bool**| This parameter enables clustering for the returned stories. | [optional] [default to false]
 **cluster_algorithm** | **str**| This parameter is used for specifying the clustering algorithm you wish to use. It supprts STC, Lingo and [k-means](https://en.wikipedia.org/wiki/K-means_clustering) algorithms. | [optional] [default to lingo]
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **sort_by** | **str**| This parameter is used for changing the order column of the results. | [optional] [default to published_at]
 **sort_direction** | **str**| This parameter is used for changing the order direction of the result. | [optional] [default to desc]
 **cursor** | **str**| This parameter is used for finding a specific page. | [optional] [default to *]
 **per_page** | **int**| This parameter is used for specifying number of items in each page. | [optional] [default to 10]

### Return type

[**Stories**](Stories.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

# **list_time_series**
> TimeSeriesList list_time_series(id=id, title=title, body=body, text=text, language=language, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, published_at_start=published_at_start, published_at_end=published_at_end, period=period)

List time series

This endpoint is used for getting time series by stories.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

id = [56] # list[int] | This parameter is used for finding stroies by story id. (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. (optional)
categories_confident = true # bool | This parameter is used for finding stories whose categories are confident. (optional) (default to true)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. (optional)
entities_title_text = ['entities_title_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in story titles. (optional)
entities_title_type = ['entities_title_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in story titles. (optional)
entities_title_links_dbpedia = ['entities_title_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in story titles. (optional)
entities_body_text = ['entities_body_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in the body of stories. (optional)
entities_body_type = ['entities_body_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in the body of stories. (optional)
entities_body_links_dbpedia = ['entities_body_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value. (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value. (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value. (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value. (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value. (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value. (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value. (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value. (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value. (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value. (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
published_at_start = 'NOW-7DAYS/DAY' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional) (default to NOW-7DAYS/DAY)
published_at_end = 'NOW/DAY' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional) (default to NOW/DAY)
period = '+1DAY' # str | The size of each date range is expressed as an interval to be added to the lower bound. It supports Date Math Syntax. Valid options are `+` following an integer number greater than 0 and one of the Date Math keywords. e.g. `+1DAY`, `+2MINUTES` and `+1MONTH`. Here are [Supported keywords](https://newsapi.aylien.com/docs/working-with-dates#date-math). (optional) (default to +1DAY)

try: 
    # List time series
    api_response = api_instance.list_time_series(id=id, title=title, body=body, text=text, language=language, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, published_at_start=published_at_start, published_at_end=published_at_end, period=period)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stroies by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. | [optional] [default to true]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. | [optional] 
 **entities_title_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. | [optional] 
 **entities_title_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. | [optional] 
 **entities_title_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. | [optional] 
 **entities_body_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. | [optional] 
 **entities_body_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. | [optional] 
 **entities_body_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
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
> Trends list_trends(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, field=field)

List trends

This endpoint is used for finding trends based on stories.

### Example 
```python
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

id = [56] # list[int] | This parameter is used for finding stroies by story id. (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. (optional)
categories_confident = true # bool | This parameter is used for finding stories whose categories are confident. (optional) (default to true)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. (optional)
entities_title_text = ['entities_title_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in story titles. (optional)
entities_title_type = ['entities_title_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in story titles. (optional)
entities_title_links_dbpedia = ['entities_title_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in story titles. (optional)
entities_body_text = ['entities_body_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `text` in the body of stories. (optional)
entities_body_type = ['entities_body_type_example'] # list[str] | This parameter is used to find stories based on the specified entities `type` in the body of stories. (optional)
entities_body_links_dbpedia = ['entities_body_links_dbpedia_example'] # list[str] | This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value. (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value. (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value. (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value. (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value. (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value. (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value. (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value. (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value. (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value. (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). (optional)
field = 'field_example' # str | This parameter is used to specify the trend field. (optional)

try: 
    # List trends
    api_response = api_instance.list_trends(id=id, title=title, body=body, text=text, language=language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, categories_level=categories_level, entities_title_text=entities_title_text, entities_title_type=entities_title_type, entities_title_links_dbpedia=entities_title_links_dbpedia, entities_body_text=entities_body_text, entities_body_type=entities_body_type, entities_body_links_dbpedia=entities_body_links_dbpedia, sentiment_title_polarity=sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, author_name=author_name, source_id=source_id, source_name=source_name, source_domain=source_domain, source_locations_country=source_locations_country, source_locations_state=source_locations_state, source_locations_city=source_locations_city, source_scopes_country=source_scopes_country, source_scopes_state=source_scopes_state, source_scopes_city=source_scopes_city, source_scopes_level=source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, field=field)
    print(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stroies by story id. | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specfic keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators). | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes. | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates). | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. | [optional] [default to true]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. | [optional] 
 **entities_title_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in story titles. | [optional] 
 **entities_title_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in story titles. | [optional] 
 **entities_title_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in story titles. | [optional] 
 **entities_body_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;text&#x60; in the body of stories. | [optional] 
 **entities_body_type** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;type&#x60; in the body of stories. | [optional] 
 **entities_body_links_dbpedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities dbpedia URL in the body of stories. | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value. | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value. | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value. | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value. | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value. | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value. | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value. | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value. | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value. | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value. | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value. | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations). | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count here [https://newsapi.aylien.com/docs/working-with-links-in-count](https://newsapi.aylien.com/docs/working-with-links-in-count). | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks here [https://newsapi.aylien.com/docs/working-with-alexa-ranks](https://newsapi.aylien.com/docs/working-with-alexa-ranks). | [optional] 
 **field** | **str**| This parameter is used to specify the trend field. | [optional] 

### Return type

[**Trends**](Trends.md)

### Authorization

[app_key](../README.rst#app_key), [app_id](../README.rst#app_id)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to Model list]](../README.rst#documentation-for-models) [[Back to README]](../README.rst)

