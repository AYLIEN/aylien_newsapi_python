# aylien_news_api.DefaultApi

All URIs are relative to *https://api.aylien.com/news*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advanced_list_stories**](DefaultApi.md#advanced_list_stories) | **POST** /stories | List Stories
[**list_autocompletes**](DefaultApi.md#list_autocompletes) | **GET** /autocompletes | List autocompletes
[**list_clusters**](DefaultApi.md#list_clusters) | **GET** /clusters | List Clusters
[**list_histograms**](DefaultApi.md#list_histograms) | **GET** /histograms | List histograms
[**list_related_stories_get**](DefaultApi.md#list_related_stories_get) | **GET** /related_stories | 
[**list_related_stories_post**](DefaultApi.md#list_related_stories_post) | **POST** /related_stories | 
[**list_stories**](DefaultApi.md#list_stories) | **GET** /stories | List Stories
[**list_time_series**](DefaultApi.md#list_time_series) | **GET** /time_series | List time series
[**list_trends**](DefaultApi.md#list_trends) | **GET** /trends | List trends


# **advanced_list_stories**
> Stories advanced_list_stories(unknown_base_type, published_at_start=published_at_start, published_at_end=published_at_end, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)

List Stories

The stories endpoint is used to return stories based on the json query you set in your request body. The News API crawler gathers articles in near real-time and stores information about them, or metadata. Below you can see all of the query parameters, and JSON schema for the body, which you can use to narrow down your query. 

### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    unknown_base_type = {"$and":[{"$or":[{"body":{"$text":"Tim Cook"}},{"social.shares.count.reddit.max":{"$gte":5000,"$boost":5}}]},{"entity":{"$and":[{"name":{"$text":"Apple","$boost":2}},{"$not":[{"type":{"$eq":"Fruit"}}]}]}}]} # UNKNOWN_BASE_TYPE | /stories body schema to perform an advanced search with logical operators and nested objects. 
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

    try:
        # List Stories
        api_response = api_instance.advanced_list_stories(unknown_base_type, published_at_start=published_at_start, published_at_end=published_at_end, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->advanced_list_stories: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    unknown_base_type = {"$and":[{"$or":[{"body":{"$text":"Tim Cook"}},{"social.shares.count.reddit.max":{"$gte":5000,"$boost":5}}]},{"entity":{"$and":[{"name":{"$text":"Apple","$boost":2}},{"$not":[{"type":{"$eq":"Fruit"}}]}]}}]} # UNKNOWN_BASE_TYPE | /stories body schema to perform an advanced search with logical operators and nested objects. 
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

    try:
        # List Stories
        api_response = api_instance.advanced_list_stories(unknown_base_type, published_at_start=published_at_start, published_at_end=published_at_end, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->advanced_list_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| /stories body schema to perform an advanced search with logical operators and nested objects.  | 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **sort_by** | **str**| This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  | [optional] [default to &#39;published_at&#39;]
 **sort_direction** | **str**| This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  | [optional] [default to &#39;desc&#39;]
 **cursor** | **str**| This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  | [optional] [default to &#39;*&#39;]
 **per_page** | **int**| This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  | [optional] [default to 10]

### Return type

[**Stories**](Stories.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of stories |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_autocompletes**
> Autocompletes list_autocompletes(type, term, language=language, per_page=per_page)

List autocompletes

The autocompletes endpoint a string of characters provided to it, and then returns suggested terms that are the most likely full words or strings. The terms returned by the News API are based on parameters the type parameters you can see below. For example, if you provide the autocompletes endpoint with the term `New York C` and select the type `dbpedia_resources`, the API will return links to the DBpedia resources `New_York_City`, `New_York_City_Subway`, `New_York_City_Police_Department`, and so on. 

### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    type = 'source_names' # str | This parameter is used for defining the type of autocompletes. 
term = 'News' # str | This parameter is used for finding autocomplete objects that contain the specified value. 
language = 'en' # str | This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'en')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

    try:
        # List autocompletes
        api_response = api_instance.list_autocompletes(type, term, language=language, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_autocompletes: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    type = 'source_names' # str | This parameter is used for defining the type of autocompletes. 
term = 'News' # str | This parameter is used for finding autocomplete objects that contain the specified value. 
language = 'en' # str | This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'en')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

    try:
        # List autocompletes
        api_response = api_instance.list_autocompletes(type, term, language=language, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_autocompletes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| This parameter is used for defining the type of autocompletes.  | 
 **term** | **str**| This parameter is used for finding autocomplete objects that contain the specified value.  | 
 **language** | **str**| This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] [default to &#39;en&#39;]
 **per_page** | **int**| This parameter is used for specifying number of items in each page.  | [optional] [default to 3]

### Return type

[**Autocompletes**](Autocompletes.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of autocompletes |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clusters**
> Clusters list_clusters(id=id, not_id=not_id, story_count_min=story_count_min, story_count_max=story_count_max, time_start=time_start, time_end=time_end, earliest_story_start=earliest_story_start, earliest_story_end=earliest_story_end, latest_story_start=latest_story_start, latest_story_end=latest_story_end, location_country=location_country, not_location_country=not_location_country, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)

List Clusters

The clusters endpoint is used to return clusters based on parameters you set in your query. 

### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding clusters by cluster id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding clusters by cluster id.  (optional)
story_count_min = 56 # int | This parameter is used for finding clusters with more than or equal to a specific amount of stories associated with them.  (optional)
story_count_max = 56 # int | This parameter is used for finding clusters with less than or equal to a specific amount of stories associated with them.  (optional)
time_start = 'time_start_example' # str | This parameter is used for finding clusters whose creation time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
time_end = 'time_end_example' # str | This parameter is used for finding clusters whose creation time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_start = 'earliest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_end = 'earliest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_start = 'latest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its latest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_end = 'latest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its latest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
location_country = ['location_country_example'] # list[str] | This parameter is used for finding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_location_country = ['location_country_example'] # list[str] | This parameter is used for excluding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

    try:
        # List Clusters
        api_response = api_instance.list_clusters(id=id, not_id=not_id, story_count_min=story_count_min, story_count_max=story_count_max, time_start=time_start, time_end=time_end, earliest_story_start=earliest_story_start, earliest_story_end=earliest_story_end, latest_story_start=latest_story_start, latest_story_end=latest_story_end, location_country=location_country, not_location_country=not_location_country, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_clusters: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding clusters by cluster id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding clusters by cluster id.  (optional)
story_count_min = 56 # int | This parameter is used for finding clusters with more than or equal to a specific amount of stories associated with them.  (optional)
story_count_max = 56 # int | This parameter is used for finding clusters with less than or equal to a specific amount of stories associated with them.  (optional)
time_start = 'time_start_example' # str | This parameter is used for finding clusters whose creation time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
time_end = 'time_end_example' # str | This parameter is used for finding clusters whose creation time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_start = 'earliest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_end = 'earliest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_start = 'latest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its latest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_end = 'latest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its latest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
location_country = ['location_country_example'] # list[str] | This parameter is used for finding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_location_country = ['location_country_example'] # list[str] | This parameter is used for excluding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

    try:
        # List Clusters
        api_response = api_instance.list_clusters(id=id, not_id=not_id, story_count_min=story_count_min, story_count_max=story_count_max, time_start=time_start, time_end=time_end, earliest_story_start=earliest_story_start, earliest_story_end=earliest_story_end, latest_story_start=latest_story_start, latest_story_end=latest_story_end, location_country=location_country, not_location_country=not_location_country, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding clusters by cluster id.  | [optional] 
 **not_id** | [**list[int]**](int.md)| This parameter is used for excluding clusters by cluster id.  | [optional] 
 **story_count_min** | **int**| This parameter is used for finding clusters with more than or equal to a specific amount of stories associated with them.  | [optional] 
 **story_count_max** | **int**| This parameter is used for finding clusters with less than or equal to a specific amount of stories associated with them.  | [optional] 
 **time_start** | **str**| This parameter is used for finding clusters whose creation time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **time_end** | **str**| This parameter is used for finding clusters whose creation time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **earliest_story_start** | **str**| This parameter is used for finding clusters whose publication date of its earliest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **earliest_story_end** | **str**| This parameter is used for finding clusters whose publication date of its earliest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **latest_story_start** | **str**| This parameter is used for finding clusters whose publication date of its latest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **latest_story_end** | **str**| This parameter is used for finding clusters whose publication date of its latest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **location_country** | [**list[str]**](str.md)| This parameter is used for finding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_location_country** | [**list[str]**](str.md)| This parameter is used for excluding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **sort_by** | **str**| This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  | [optional] [default to &#39;published_at&#39;]
 **sort_direction** | **str**| This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  | [optional] [default to &#39;desc&#39;]
 **cursor** | **str**| This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  | [optional] [default to &#39;*&#39;]
 **per_page** | **int**| This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  | [optional] [default to 10]

### Return type

[**Clusters**](Clusters.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of clusters |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_histograms**
> Histograms list_histograms(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query, interval_start=interval_start, interval_end=interval_end, interval_width=interval_width, field=field)

List histograms

For the numerical metadata that the News API gathers (such as word counts or social shares for example), you can use the histograms endpoint to access and display this information. As this endpoint does not return actual stories, the results you are given will not count towards your story allowance provided by your subscription, so you can effectively query this endpoint free of charge. 

### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
interval_start = 56 # int | This parameter is used for setting the start data point of histogram intervals.  (optional)
interval_end = 56 # int | This parameter is used for setting the end data point of histogram intervals.  (optional)
interval_width = 56 # int | This parameter is used for setting the width of histogram intervals.  (optional)
field = 'social_shares_count' # str | This parameter is used for specifying the y-axis variable for the histogram.  (optional) (default to 'social_shares_count')

    try:
        # List histograms
        api_response = api_instance.list_histograms(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query, interval_start=interval_start, interval_end=interval_end, interval_width=interval_width, field=field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_histograms: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
interval_start = 56 # int | This parameter is used for setting the start data point of histogram intervals.  (optional)
interval_end = 56 # int | This parameter is used for setting the end data point of histogram intervals.  (optional)
interval_width = 56 # int | This parameter is used for setting the width of histogram intervals.  (optional)
field = 'social_shares_count' # str | This parameter is used for specifying the y-axis variable for the histogram.  (optional) (default to 'social_shares_count')

    try:
        # List histograms
        api_response = api_instance.list_histograms(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query, interval_start=interval_start, interval_end=interval_end, interval_width=interval_width, field=field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_histograms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stories by story id.  | [optional] 
 **not_id** | [**list[int]**](int.md)| This parameter is used for excluding stories by story id.  | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_title** | **str**| This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_body** | **str**| This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_text** | **str**| This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **links_permalink** | [**list[str]**](str.md)| This parameter is used to find stories based on their url.  | [optional] 
 **not_links_permalink** | [**list[str]**](str.md)| This parameter is used to exclude stories based on their url.  | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **not_language** | [**list[str]**](str.md)| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] [default to True]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_id** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_label** | [**list[str]**](str.md)| This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_label** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_level** | [**list[int]**](int.md)| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **entities_id** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_id** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_types** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_types** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_stock_tickers** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;stock_tickers&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_stock_tickers** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;stock_tickers&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_title_surface_forms_text** | **str**| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_title_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value.  | [optional] 
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value.  | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value.  | [optional] 
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value.  | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value.  | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value.  | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value.  | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value.  | [optional] 
 **media_images_format** | [**list[str]**](str.md)| This parameter is used for finding stories whose images format are the specified value.  | [optional] 
 **not_media_images_format** | [**list[str]**](str.md)| This parameter is used for excluding stories whose images format are the specified value.  | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value.  | [optional] 
 **not_author_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose author id is the specified value.  | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value.  | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value.  | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value.  | [optional] 
 **not_source_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose source id is the specified value.  | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value.  | [optional] 
 **not_source_name** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source name contains the specified value.  | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value.  | [optional] 
 **not_source_domain** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source domain is the specified value.  | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_level** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  | [optional] 
 **clusters** | [**list[str]**](str.md)| This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  | [optional] 
 **aql** | **str**| This parameter is used to supply a query in AYLIEN Query Language.  | [optional] 
 **aql_default_field** | **str**| This parameter is used to supply an optional default field name used in the AQL query.  | [optional] [default to &#39;text&#39;]
 **query** | **str**| This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  | [optional] 
 **interval_start** | **int**| This parameter is used for setting the start data point of histogram intervals.  | [optional] 
 **interval_end** | **int**| This parameter is used for setting the end data point of histogram intervals.  | [optional] 
 **interval_width** | **int**| This parameter is used for setting the width of histogram intervals.  | [optional] 
 **field** | **str**| This parameter is used for specifying the y-axis variable for the histogram.  | [optional] [default to &#39;social_shares_count&#39;]

### Return type

[**Histograms**](Histograms.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of the histogram intervals |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_related_stories_get**
> RelatedStories list_related_stories_get(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, aql=aql, aql_default_field=aql_default_field, query=query, boost_by=boost_by, story_language=story_language, per_page=per_page)



### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
story_id = 56 # int | A story id (optional)
story_url = 'story_url_example' # str | An article or webpage (optional)
story_title = 'story_title_example' # str | Title of the article (optional)
story_body = 'story_body_example' # str | Body of the article (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
boost_by = 'boost_by_example' # str | This parameter is used for boosting the result by the specified value.  (optional)
story_language = 'auto' # str | This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'auto')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

    try:
        api_response = api_instance.list_related_stories_get(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, aql=aql, aql_default_field=aql_default_field, query=query, boost_by=boost_by, story_language=story_language, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_related_stories_get: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
story_id = 56 # int | A story id (optional)
story_url = 'story_url_example' # str | An article or webpage (optional)
story_title = 'story_title_example' # str | Title of the article (optional)
story_body = 'story_body_example' # str | Body of the article (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
boost_by = 'boost_by_example' # str | This parameter is used for boosting the result by the specified value.  (optional)
story_language = 'auto' # str | This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'auto')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

    try:
        api_response = api_instance.list_related_stories_get(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, aql=aql, aql_default_field=aql_default_field, query=query, boost_by=boost_by, story_language=story_language, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_related_stories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stories by story id.  | [optional] 
 **not_id** | [**list[int]**](int.md)| This parameter is used for excluding stories by story id.  | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_title** | **str**| This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_body** | **str**| This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_text** | **str**| This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **links_permalink** | [**list[str]**](str.md)| This parameter is used to find stories based on their url.  | [optional] 
 **not_links_permalink** | [**list[str]**](str.md)| This parameter is used to exclude stories based on their url.  | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **not_language** | [**list[str]**](str.md)| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] [default to True]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_id** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_label** | [**list[str]**](str.md)| This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_label** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_level** | [**list[int]**](int.md)| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **entities_id** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_id** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_types** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_types** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_stock_tickers** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;stock_tickers&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_stock_tickers** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;stock_tickers&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_title_surface_forms_text** | **str**| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_title_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value.  | [optional] 
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value.  | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value.  | [optional] 
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value.  | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value.  | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value.  | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value.  | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value.  | [optional] 
 **media_images_format** | [**list[str]**](str.md)| This parameter is used for finding stories whose images format are the specified value.  | [optional] 
 **not_media_images_format** | [**list[str]**](str.md)| This parameter is used for excluding stories whose images format are the specified value.  | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value.  | [optional] 
 **not_author_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose author id is the specified value.  | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value.  | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value.  | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value.  | [optional] 
 **not_source_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose source id is the specified value.  | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value.  | [optional] 
 **not_source_name** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source name contains the specified value.  | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value.  | [optional] 
 **not_source_domain** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source domain is the specified value.  | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_level** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  | [optional] 
 **clusters** | [**list[str]**](str.md)| This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  | [optional] 
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **story_id** | **int**| A story id | [optional] 
 **story_url** | **str**| An article or webpage | [optional] 
 **story_title** | **str**| Title of the article | [optional] 
 **story_body** | **str**| Body of the article | [optional] 
 **aql** | **str**| This parameter is used to supply a query in AYLIEN Query Language.  | [optional] 
 **aql_default_field** | **str**| This parameter is used to supply an optional default field name used in the AQL query.  | [optional] [default to &#39;text&#39;]
 **query** | **str**| This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  | [optional] 
 **boost_by** | **str**| This parameter is used for boosting the result by the specified value.  | [optional] 
 **story_language** | **str**| This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] [default to &#39;auto&#39;]
 **per_page** | **int**| This parameter is used for specifying number of items in each page.  | [optional] [default to 3]

### Return type

[**RelatedStories**](RelatedStories.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of related stories |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_related_stories_post**
> RelatedStories list_related_stories_post(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, aql=aql, aql_default_field=aql_default_field, query=query, boost_by=boost_by, story_language=story_language, per_page=per_page)



### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
story_id = 56 # int | A story id (optional)
story_url = 'story_url_example' # str | An article or webpage (optional)
story_title = 'story_title_example' # str | Title of the article (optional)
story_body = 'story_body_example' # str | Body of the article (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
boost_by = 'boost_by_example' # str | This parameter is used for boosting the result by the specified value.  (optional)
story_language = 'auto' # str | This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'auto')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

    try:
        api_response = api_instance.list_related_stories_post(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, aql=aql, aql_default_field=aql_default_field, query=query, boost_by=boost_by, story_language=story_language, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_related_stories_post: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
story_id = 56 # int | A story id (optional)
story_url = 'story_url_example' # str | An article or webpage (optional)
story_title = 'story_title_example' # str | Title of the article (optional)
story_body = 'story_body_example' # str | Body of the article (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
boost_by = 'boost_by_example' # str | This parameter is used for boosting the result by the specified value.  (optional)
story_language = 'auto' # str | This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'auto')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

    try:
        api_response = api_instance.list_related_stories_post(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, story_id=story_id, story_url=story_url, story_title=story_title, story_body=story_body, aql=aql, aql_default_field=aql_default_field, query=query, boost_by=boost_by, story_language=story_language, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_related_stories_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stories by story id.  | [optional] 
 **not_id** | [**list[int]**](int.md)| This parameter is used for excluding stories by story id.  | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_title** | **str**| This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_body** | **str**| This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_text** | **str**| This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **links_permalink** | [**list[str]**](str.md)| This parameter is used to find stories based on their url.  | [optional] 
 **not_links_permalink** | [**list[str]**](str.md)| This parameter is used to exclude stories based on their url.  | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **not_language** | [**list[str]**](str.md)| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] [default to True]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_id** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_label** | [**list[str]**](str.md)| This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_label** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_level** | [**list[int]**](int.md)| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **entities_id** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_id** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_types** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_types** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_stock_tickers** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;stock_tickers&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_stock_tickers** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;stock_tickers&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_title_surface_forms_text** | **str**| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_title_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value.  | [optional] 
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value.  | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value.  | [optional] 
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value.  | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value.  | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value.  | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value.  | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value.  | [optional] 
 **media_images_format** | [**list[str]**](str.md)| This parameter is used for finding stories whose images format are the specified value.  | [optional] 
 **not_media_images_format** | [**list[str]**](str.md)| This parameter is used for excluding stories whose images format are the specified value.  | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value.  | [optional] 
 **not_author_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose author id is the specified value.  | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value.  | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value.  | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value.  | [optional] 
 **not_source_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose source id is the specified value.  | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value.  | [optional] 
 **not_source_name** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source name contains the specified value.  | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value.  | [optional] 
 **not_source_domain** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source domain is the specified value.  | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_level** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  | [optional] 
 **clusters** | [**list[str]**](str.md)| This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  | [optional] 
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **story_id** | **int**| A story id | [optional] 
 **story_url** | **str**| An article or webpage | [optional] 
 **story_title** | **str**| Title of the article | [optional] 
 **story_body** | **str**| Body of the article | [optional] 
 **aql** | **str**| This parameter is used to supply a query in AYLIEN Query Language.  | [optional] 
 **aql_default_field** | **str**| This parameter is used to supply an optional default field name used in the AQL query.  | [optional] [default to &#39;text&#39;]
 **query** | **str**| This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  | [optional] 
 **boost_by** | **str**| This parameter is used for boosting the result by the specified value.  | [optional] 
 **story_language** | **str**| This parameter is used for setting the language of the story. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] [default to &#39;auto&#39;]
 **per_page** | **int**| This parameter is used for specifying number of items in each page.  | [optional] [default to 3]

### Return type

[**RelatedStories**](RelatedStories.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of related stories |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stories**
> Stories list_stories(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, language=language, not_language=not_language, links_permalink=links_permalink, not_links_permalink=not_links_permalink, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, aql=aql, aql_default_field=aql_default_field, query=query, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)

List Stories

The stories endpoint is used to return stories based on parameters you set in your query. The News API crawler gathers articles in near real-time and stores information about them, or metadata. Below you can see all of the query parameters, which you can use to narrow down your query. 

### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

    try:
        # List Stories
        api_response = api_instance.list_stories(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, language=language, not_language=not_language, links_permalink=links_permalink, not_links_permalink=not_links_permalink, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, aql=aql, aql_default_field=aql_default_field, query=query, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

    try:
        # List Stories
        api_response = api_instance.list_stories(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, language=language, not_language=not_language, links_permalink=links_permalink, not_links_permalink=not_links_permalink, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, _return=_return, aql=aql, aql_default_field=aql_default_field, query=query, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stories by story id.  | [optional] 
 **not_id** | [**list[int]**](int.md)| This parameter is used for excluding stories by story id.  | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_title** | **str**| This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_body** | **str**| This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_text** | **str**| This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **not_language** | [**list[str]**](str.md)| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **links_permalink** | [**list[str]**](str.md)| This parameter is used to find stories based on their url.  | [optional] 
 **not_links_permalink** | [**list[str]**](str.md)| This parameter is used to exclude stories based on their url.  | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] [default to True]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_id** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_label** | [**list[str]**](str.md)| This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_label** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_level** | [**list[int]**](int.md)| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **entities_id** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_id** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_types** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_types** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_stock_tickers** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;stock_tickers&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_stock_tickers** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;stock_tickers&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_title_surface_forms_text** | **str**| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_title_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value.  | [optional] 
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value.  | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value.  | [optional] 
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value.  | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value.  | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value.  | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value.  | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value.  | [optional] 
 **media_images_format** | [**list[str]**](str.md)| This parameter is used for finding stories whose images format are the specified value.  | [optional] 
 **not_media_images_format** | [**list[str]**](str.md)| This parameter is used for excluding stories whose images format are the specified value.  | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value.  | [optional] 
 **not_author_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose author id is the specified value.  | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value.  | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value.  | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value.  | [optional] 
 **not_source_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose source id is the specified value.  | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value.  | [optional] 
 **not_source_name** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source name contains the specified value.  | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value.  | [optional] 
 **not_source_domain** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source domain is the specified value.  | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_level** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  | [optional] 
 **clusters** | [**list[str]**](str.md)| This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  | [optional] 
 **_return** | [**list[str]**](str.md)| This parameter is used for specifying return fields. | [optional] 
 **aql** | **str**| This parameter is used to supply a query in AYLIEN Query Language.  | [optional] 
 **aql_default_field** | **str**| This parameter is used to supply an optional default field name used in the AQL query.  | [optional] [default to &#39;text&#39;]
 **query** | **str**| This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  | [optional] 
 **sort_by** | **str**| This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  | [optional] [default to &#39;published_at&#39;]
 **sort_direction** | **str**| This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  | [optional] [default to &#39;desc&#39;]
 **cursor** | **str**| This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  | [optional] [default to &#39;*&#39;]
 **per_page** | **int**| This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  | [optional] [default to 10]

### Return type

[**Stories**](Stories.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of stories |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_series**
> TimeSeriesList list_time_series(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, language=language, not_language=not_language, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query, published_at_start=published_at_start, published_at_end=published_at_end, period=period)

List time series

The time series endpoint allows you to track information contained in stories over time. This information can be anything from mentions of a topic or entities, sentiment about a topic, or the volume of stories published by a source, to name but a few. The full list of parameters is given below. Using the [Date Math Syntax](https://newsapi.aylien.com/docs/working-with-dates), you can easily set your query to return information from any time period, from the current point in time to when the News API started collecting stories. The returned information can be rounded to a time also specified by you, for example by setting the results into hourly, daily, or weekly data points. 

### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
published_at_start = 'NOW-7DAYS/DAY' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional) (default to 'NOW-7DAYS/DAY')
published_at_end = 'NOW/DAY' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional) (default to 'NOW/DAY')
period = '+1DAY' # str | The size of each date range is expressed as an interval to be added to the lower bound. It supports Date Math Syntax. Valid options are `+` following an integer number greater than 0 and one of the Date Math keywords. e.g. `+1DAY`, `+2MINUTES` and `+1MONTH`. Here are [Supported keywords](https://newsapi.aylien.com/docs/working-with-dates#date-math).  (optional) (default to '+1DAY')

    try:
        # List time series
        api_response = api_instance.list_time_series(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, language=language, not_language=not_language, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query, published_at_start=published_at_start, published_at_end=published_at_end, period=period)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_time_series: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)
published_at_start = 'NOW-7DAYS/DAY' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional) (default to 'NOW-7DAYS/DAY')
published_at_end = 'NOW/DAY' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional) (default to 'NOW/DAY')
period = '+1DAY' # str | The size of each date range is expressed as an interval to be added to the lower bound. It supports Date Math Syntax. Valid options are `+` following an integer number greater than 0 and one of the Date Math keywords. e.g. `+1DAY`, `+2MINUTES` and `+1MONTH`. Here are [Supported keywords](https://newsapi.aylien.com/docs/working-with-dates#date-math).  (optional) (default to '+1DAY')

    try:
        # List time series
        api_response = api_instance.list_time_series(id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, language=language, not_language=not_language, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query, published_at_start=published_at_start, published_at_end=published_at_end, period=period)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding stories by story id.  | [optional] 
 **not_id** | [**list[int]**](int.md)| This parameter is used for excluding stories by story id.  | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_title** | **str**| This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_body** | **str**| This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_text** | **str**| This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **not_language** | [**list[str]**](str.md)| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] [default to True]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_id** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_label** | [**list[str]**](str.md)| This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_label** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_level** | [**list[int]**](int.md)| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **entities_id** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_id** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_types** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_types** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_stock_tickers** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;stock_tickers&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_stock_tickers** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;stock_tickers&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_title_surface_forms_text** | **str**| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_title_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value.  | [optional] 
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value.  | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value.  | [optional] 
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value.  | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value.  | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value.  | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value.  | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value.  | [optional] 
 **media_images_format** | [**list[str]**](str.md)| This parameter is used for finding stories whose images format are the specified value.  | [optional] 
 **not_media_images_format** | [**list[str]**](str.md)| This parameter is used for excluding stories whose images format are the specified value.  | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value.  | [optional] 
 **not_author_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose author id is the specified value.  | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value.  | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value.  | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value.  | [optional] 
 **not_source_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose source id is the specified value.  | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value.  | [optional] 
 **not_source_name** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source name contains the specified value.  | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value.  | [optional] 
 **not_source_domain** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source domain is the specified value.  | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_level** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  | [optional] 
 **clusters** | [**list[str]**](str.md)| This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  | [optional] 
 **aql** | **str**| This parameter is used to supply a query in AYLIEN Query Language.  | [optional] 
 **aql_default_field** | **str**| This parameter is used to supply an optional default field name used in the AQL query.  | [optional] [default to &#39;text&#39;]
 **query** | **str**| This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] [default to &#39;NOW-7DAYS/DAY&#39;]
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] [default to &#39;NOW/DAY&#39;]
 **period** | **str**| The size of each date range is expressed as an interval to be added to the lower bound. It supports Date Math Syntax. Valid options are &#x60;+&#x60; following an integer number greater than 0 and one of the Date Math keywords. e.g. &#x60;+1DAY&#x60;, &#x60;+2MINUTES&#x60; and &#x60;+1MONTH&#x60;. Here are [Supported keywords](https://newsapi.aylien.com/docs/working-with-dates#date-math).  | [optional] [default to &#39;+1DAY&#39;]

### Return type

[**TimeSeriesList**](TimeSeriesList.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of time series |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trends**
> Trends list_trends(field, id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query)

List trends

The trends endpoint allows you to identify the most-mentioned entities, concepts and keywords relevant to your query. For example, this endpoint allows you to set parameters like a time period, a subject category, or an entity, and your request will return the most mentioned entities or keywords that are mentioned in relation to your query. 

### Example

* Api Key Authentication (app_id):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    field = 'keywords' # str | This parameter is used to specify the trend field. 
id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)

    try:
        # List trends
        api_response = api_instance.list_trends(field, id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_trends: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.aylien.com/news
# See configuration.py for a list of all supported configuration parameters.
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_id': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Configure API key authorization: app_key
configuration = aylien_news_api.Configuration(
    host = "https://api.aylien.com/news",
    api_key = {
        'app_key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_key'] = 'Bearer'

# Enter a context with an instance of the API client
with aylien_news_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(api_client)
    field = 'keywords' # str | This parameter is used to specify the trend field. 
id = [56] # list[int] | This parameter is used for finding stories by story id.  (optional)
not_id = [56] # list[int] | This parameter is used for excluding stories by story id.  (optional)
title = 'title_example' # str | This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
body = 'body_example' # str | This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
text = 'text_example' # str | This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_title = 'translations_en_title_example' # str | This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_body = 'translations_en_body_example' # str | This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
translations_en_text = 'translations_en_text_example' # str | This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  (optional)
links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to find stories based on their url.  (optional)
not_links_permalink = ['links_permalink_example'] # list[str] | This parameter is used to exclude stories based on their url.  (optional)
language = ['language_example'] # list[str] | This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
not_language = ['language_example'] # list[str] | This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional)
published_at_start = 'published_at_start_example' # str | This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
published_at_end = 'published_at_end_example' # str | This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
categories_taxonomy = 'categories_taxonomy_example' # str | This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_confident = True # bool | This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional) (default to True)
categories_id = ['categories_id_example'] # list[str] | This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_id = ['categories_id_example'] # list[str] | This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_label = ['categories_label_example'] # list[str] | This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_label = ['categories_label_example'] # list[str] | This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
categories_level = [56] # list[int] | This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
not_categories_level = [56] # list[int] | This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  (optional)
entities_id = ['entities_id_example'] # list[str] | This parameter is used to find stories based on the specified entities `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_id = ['entities_id_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `id`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikipedia = ['entities_links_wikipedia_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_links_wikidata = ['entities_links_wikidata_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_types = ['entities_types_example'] # list[str] | This parameter is used to find stories based on the specified entities `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_types = ['entities_types_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `types`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_stock_tickers = ['entities_stock_tickers_example'] # list[str] | This parameter is used to find stories based on the specified entities `stock_tickers`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_stock_tickers = ['entities_body_stock_tickers_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `stock_tickers` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_surface_forms_text = ['entities_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form`. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_title_surface_forms_text = 'entities_title_surface_forms_text_example' # str | This parameter is used to find stories based on the specified entities `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_title_surface_forms_text = ['entities_title_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to find stories based on the specified entities `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
not_entities_body_surface_forms_text = ['entities_body_surface_forms_text_example'] # list[str] | This parameter is used to exclude stories based on the specified entity's `surface_form` in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  (optional)
sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for finding stories whose title sentiment is the specified value.  (optional)
not_sentiment_title_polarity = 'sentiment_title_polarity_example' # str | This parameter is used for excluding stories whose title sentiment is the specified value.  (optional)
sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for finding stories whose body sentiment is the specified value.  (optional)
not_sentiment_body_polarity = 'sentiment_body_polarity_example' # str | This parameter is used for excluding stories whose body sentiment is the specified value.  (optional)
media_images_count_min = 56 # int | This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  (optional)
media_images_count_max = 56 # int | This parameter is used for finding stories whose number of images is less than or equal to the specified value.  (optional)
media_images_width_min = 56 # int | This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  (optional)
media_images_width_max = 56 # int | This parameter is used for finding stories whose width of images are less than or equal to the specified value.  (optional)
media_images_height_min = 56 # int | This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  (optional)
media_images_height_max = 56 # int | This parameter is used for finding stories whose height of images are less than or equal to the specified value.  (optional)
media_images_content_length_min = 56 # int | This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  (optional)
media_images_content_length_max = 56 # int | This parameter is used for finding stories whose images content length are less than or equal to the specified value.  (optional)
media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for finding stories whose images format are the specified value.  (optional)
not_media_images_format = ['media_images_format_example'] # list[str] | This parameter is used for excluding stories whose images format are the specified value.  (optional)
media_videos_count_min = 56 # int | This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  (optional)
media_videos_count_max = 56 # int | This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  (optional)
author_id = [56] # list[int] | This parameter is used for finding stories whose author id is the specified value.  (optional)
not_author_id = [56] # list[int] | This parameter is used for excluding stories whose author id is the specified value.  (optional)
author_name = 'author_name_example' # str | This parameter is used for finding stories whose author full name contains the specified value.  (optional)
not_author_name = 'author_name_example' # str | This parameter is used for excluding stories whose author full name contains the specified value.  (optional)
source_id = [56] # list[int] | This parameter is used for finding stories whose source id is the specified value.  (optional)
not_source_id = [56] # list[int] | This parameter is used for excluding stories whose source id is the specified value.  (optional)
source_name = ['source_name_example'] # list[str] | This parameter is used for finding stories whose source name contains the specified value.  (optional)
not_source_name = ['source_name_example'] # list[str] | This parameter is used for excluding stories whose source name contains the specified value.  (optional)
source_domain = ['source_domain_example'] # list[str] | This parameter is used for finding stories whose source domain is the specified value.  (optional)
not_source_domain = ['source_domain_example'] # list[str] | This parameter is used for excluding stories whose source domain is the specified value.  (optional)
source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_country = ['source_locations_country_example'] # list[str] | This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_state = ['source_locations_state_example'] # list[str] | This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_locations_city = ['source_locations_city_example'] # list[str] | This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_country = ['source_scopes_country_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_state = ['source_scopes_state_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_city = ['source_scopes_city_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
not_source_scopes_level = ['source_scopes_level_example'] # list[str] | This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
source_links_in_count_min = 56 # int | This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_links_in_count_max = 56 # int | This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  (optional)
source_rankings_alexa_rank_min = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_rank_max = 56 # int | This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
source_rankings_alexa_country = ['source_rankings_alexa_country_example'] # list[str] | This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  (optional)
social_shares_count_facebook_min = 56 # int | This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_facebook_max = 56 # int | This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  (optional)
social_shares_count_google_plus_min = 56 # int | This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_google_plus_max = 56 # int | This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  (optional)
social_shares_count_linkedin_min = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_linkedin_max = 56 # int | This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  (optional)
social_shares_count_reddit_min = 56 # int | This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  (optional)
social_shares_count_reddit_max = 56 # int | This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  (optional)
clusters = ['clusters_example'] # list[str] | This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  (optional)
aql = 'aql_example' # str | This parameter is used to supply a query in AYLIEN Query Language.  (optional)
aql_default_field = 'text' # str | This parameter is used to supply an optional default field name used in the AQL query.  (optional) (default to 'text')
query = 'query_example' # str | This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  (optional)

    try:
        # List trends
        api_response = api_instance.list_trends(field, id=id, not_id=not_id, title=title, body=body, text=text, translations_en_title=translations_en_title, translations_en_body=translations_en_body, translations_en_text=translations_en_text, links_permalink=links_permalink, not_links_permalink=not_links_permalink, language=language, not_language=not_language, published_at_start=published_at_start, published_at_end=published_at_end, categories_taxonomy=categories_taxonomy, categories_confident=categories_confident, categories_id=categories_id, not_categories_id=not_categories_id, categories_label=categories_label, not_categories_label=not_categories_label, categories_level=categories_level, not_categories_level=not_categories_level, entities_id=entities_id, not_entities_id=not_entities_id, entities_links_wikipedia=entities_links_wikipedia, not_entities_links_wikipedia=not_entities_links_wikipedia, entities_links_wikidata=entities_links_wikidata, not_entities_links_wikidata=not_entities_links_wikidata, entities_types=entities_types, not_entities_types=not_entities_types, entities_stock_tickers=entities_stock_tickers, entities_body_stock_tickers=entities_body_stock_tickers, entities_surface_forms_text=entities_surface_forms_text, not_entities_surface_forms_text=not_entities_surface_forms_text, entities_title_surface_forms_text=entities_title_surface_forms_text, not_entities_title_surface_forms_text=not_entities_title_surface_forms_text, entities_body_surface_forms_text=entities_body_surface_forms_text, not_entities_body_surface_forms_text=not_entities_body_surface_forms_text, sentiment_title_polarity=sentiment_title_polarity, not_sentiment_title_polarity=not_sentiment_title_polarity, sentiment_body_polarity=sentiment_body_polarity, not_sentiment_body_polarity=not_sentiment_body_polarity, media_images_count_min=media_images_count_min, media_images_count_max=media_images_count_max, media_images_width_min=media_images_width_min, media_images_width_max=media_images_width_max, media_images_height_min=media_images_height_min, media_images_height_max=media_images_height_max, media_images_content_length_min=media_images_content_length_min, media_images_content_length_max=media_images_content_length_max, media_images_format=media_images_format, not_media_images_format=not_media_images_format, media_videos_count_min=media_videos_count_min, media_videos_count_max=media_videos_count_max, author_id=author_id, not_author_id=not_author_id, author_name=author_name, not_author_name=not_author_name, source_id=source_id, not_source_id=not_source_id, source_name=source_name, not_source_name=not_source_name, source_domain=source_domain, not_source_domain=not_source_domain, source_locations_country=source_locations_country, not_source_locations_country=not_source_locations_country, source_locations_state=source_locations_state, not_source_locations_state=not_source_locations_state, source_locations_city=source_locations_city, not_source_locations_city=not_source_locations_city, source_scopes_country=source_scopes_country, not_source_scopes_country=not_source_scopes_country, source_scopes_state=source_scopes_state, not_source_scopes_state=not_source_scopes_state, source_scopes_city=source_scopes_city, not_source_scopes_city=not_source_scopes_city, source_scopes_level=source_scopes_level, not_source_scopes_level=not_source_scopes_level, source_links_in_count_min=source_links_in_count_min, source_links_in_count_max=source_links_in_count_max, source_rankings_alexa_rank_min=source_rankings_alexa_rank_min, source_rankings_alexa_rank_max=source_rankings_alexa_rank_max, source_rankings_alexa_country=source_rankings_alexa_country, social_shares_count_facebook_min=social_shares_count_facebook_min, social_shares_count_facebook_max=social_shares_count_facebook_max, social_shares_count_google_plus_min=social_shares_count_google_plus_min, social_shares_count_google_plus_max=social_shares_count_google_plus_max, social_shares_count_linkedin_min=social_shares_count_linkedin_min, social_shares_count_linkedin_max=social_shares_count_linkedin_max, social_shares_count_reddit_min=social_shares_count_reddit_min, social_shares_count_reddit_max=social_shares_count_reddit_max, clusters=clusters, aql=aql, aql_default_field=aql_default_field, query=query)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_trends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| This parameter is used to specify the trend field.  | 
 **id** | [**list[int]**](int.md)| This parameter is used for finding stories by story id.  | [optional] 
 **not_id** | [**list[int]**](int.md)| This parameter is used for excluding stories by story id.  | [optional] 
 **title** | **str**| This parameter is used for finding stories whose title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **body** | **str**| This parameter is used for finding stories whose body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **text** | **str**| This parameter is used for finding stories whose title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_title** | **str**| This parameter is used for finding stories whose translation title contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_body** | **str**| This parameter is used for finding stories whose translation body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **translations_en_text** | **str**| This parameter is used for finding stories whose translation title or body contains a specific keyword. It supports [boolean operators](https://newsapi.aylien.com/docs/boolean-operators).  | [optional] 
 **links_permalink** | [**list[str]**](str.md)| This parameter is used to find stories based on their url.  | [optional] 
 **not_links_permalink** | [**list[str]**](str.md)| This parameter is used to exclude stories based on their url.  | [optional] 
 **language** | [**list[str]**](str.md)| This parameter is used for finding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **not_language** | [**list[str]**](str.md)| This parameter is used for excluding stories whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  | [optional] 
 **published_at_start** | **str**| This parameter is used for finding stories whose published at time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **published_at_end** | **str**| This parameter is used for finding stories whose published at time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **categories_taxonomy** | **str**| This parameter is used for defining the type of the taxonomy for the rest of the categories queries. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_confident** | **bool**| This parameter is used for finding stories whose categories are confident. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] [default to True]
 **categories_id** | [**list[str]**](str.md)| This parameter is used for finding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_id** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories id. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_label** | [**list[str]**](str.md)| This parameter is used for finding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_label** | [**list[str]**](str.md)| This parameter is used for excluding stories by categories label. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **categories_level** | [**list[int]**](int.md)| This parameter is used for finding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **not_categories_level** | [**list[int]**](int.md)| This parameter is used for excluding stories by categories level. You can read more about working with categories [here](https://newsapi.aylien.com/docs/working-with-categories).  | [optional] 
 **entities_id** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_id** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;id&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikipedia** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikipedia URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_links_wikidata** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s Wikidata URL. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_types** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_types** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;types&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_stock_tickers** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;stock_tickers&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_stock_tickers** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;stock_tickers&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60;. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_title_surface_forms_text** | **str**| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_title_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in story titles. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to find stories based on the specified entities &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **not_entities_body_surface_forms_text** | [**list[str]**](str.md)| This parameter is used to exclude stories based on the specified entity&#39;s &#x60;surface_form&#x60; in the body of stories. You can read more about working with entities [here](https://newsapi.aylien.com/docs/working-with-entities).  | [optional] 
 **sentiment_title_polarity** | **str**| This parameter is used for finding stories whose title sentiment is the specified value.  | [optional] 
 **not_sentiment_title_polarity** | **str**| This parameter is used for excluding stories whose title sentiment is the specified value.  | [optional] 
 **sentiment_body_polarity** | **str**| This parameter is used for finding stories whose body sentiment is the specified value.  | [optional] 
 **not_sentiment_body_polarity** | **str**| This parameter is used for excluding stories whose body sentiment is the specified value.  | [optional] 
 **media_images_count_min** | **int**| This parameter is used for finding stories whose number of images is greater than or equal to the specified value.  | [optional] 
 **media_images_count_max** | **int**| This parameter is used for finding stories whose number of images is less than or equal to the specified value.  | [optional] 
 **media_images_width_min** | **int**| This parameter is used for finding stories whose width of images are greater than or equal to the specified value.  | [optional] 
 **media_images_width_max** | **int**| This parameter is used for finding stories whose width of images are less than or equal to the specified value.  | [optional] 
 **media_images_height_min** | **int**| This parameter is used for finding stories whose height of images are greater than or equal to the specified value.  | [optional] 
 **media_images_height_max** | **int**| This parameter is used for finding stories whose height of images are less than or equal to the specified value.  | [optional] 
 **media_images_content_length_min** | **int**| This parameter is used for finding stories whose images content length are greater than or equal to the specified value.  | [optional] 
 **media_images_content_length_max** | **int**| This parameter is used for finding stories whose images content length are less than or equal to the specified value.  | [optional] 
 **media_images_format** | [**list[str]**](str.md)| This parameter is used for finding stories whose images format are the specified value.  | [optional] 
 **not_media_images_format** | [**list[str]**](str.md)| This parameter is used for excluding stories whose images format are the specified value.  | [optional] 
 **media_videos_count_min** | **int**| This parameter is used for finding stories whose number of videos is greater than or equal to the specified value.  | [optional] 
 **media_videos_count_max** | **int**| This parameter is used for finding stories whose number of videos is less than or equal to the specified value.  | [optional] 
 **author_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose author id is the specified value.  | [optional] 
 **not_author_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose author id is the specified value.  | [optional] 
 **author_name** | **str**| This parameter is used for finding stories whose author full name contains the specified value.  | [optional] 
 **not_author_name** | **str**| This parameter is used for excluding stories whose author full name contains the specified value.  | [optional] 
 **source_id** | [**list[int]**](int.md)| This parameter is used for finding stories whose source id is the specified value.  | [optional] 
 **not_source_id** | [**list[int]**](int.md)| This parameter is used for excluding stories whose source id is the specified value.  | [optional] 
 **source_name** | [**list[str]**](str.md)| This parameter is used for finding stories whose source name contains the specified value.  | [optional] 
 **not_source_name** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source name contains the specified value.  | [optional] 
 **source_domain** | [**list[str]**](str.md)| This parameter is used for finding stories whose source domain is the specified value.  | [optional] 
 **not_source_domain** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source domain is the specified value.  | [optional] 
 **source_locations_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source country is the specified value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source state/province is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_locations_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_locations_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source city is the specified value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_country** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_country** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_state** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_state** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified state/province value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_city** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_city** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified city value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_scopes_level** | [**list[str]**](str.md)| This parameter is used for finding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **not_source_scopes_level** | [**list[str]**](str.md)| This parameter is used for excluding stories whose source scopes is the specified level value. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **source_links_in_count_min** | **int**| This parameter is used for finding stories from sources whose Links in count is greater than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_links_in_count_max** | **int**| This parameter is used for finding stories from sources whose Links in count is less than or equal to the specified value. You can read more about working with Links in count [here](https://newsapi.aylien.com/docs/working-with-links-in-count).  | [optional] 
 **source_rankings_alexa_rank_min** | **int**| This parameter is used for finding stories from sources whose Alexa rank is greater than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_rank_max** | **int**| This parameter is used for finding stories from sources whose Alexa rank is less than or equal to the specified value. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **source_rankings_alexa_country** | [**list[str]**](str.md)| This parameter is used for finding stories from sources whose Alexa rank is in the specified country value. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. You can read more about working with Alexa ranks [here](https://newsapi.aylien.com/docs/working-with-alexa-ranks).  | [optional] 
 **social_shares_count_facebook_min** | **int**| This parameter is used for finding stories whose Facebook social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_facebook_max** | **int**| This parameter is used for finding stories whose Facebook social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_min** | **int**| This parameter is used for finding stories whose Google+ social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_google_plus_max** | **int**| This parameter is used for finding stories whose Google+ social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_min** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_linkedin_max** | **int**| This parameter is used for finding stories whose LinkedIn social shares count is less than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_min** | **int**| This parameter is used for finding stories whose Reddit social shares count is greater than or equal to the specified value.  | [optional] 
 **social_shares_count_reddit_max** | **int**| This parameter is used for finding stories whose Reddit social shares count is less than or equal to the specified value.  | [optional] 
 **clusters** | [**list[str]**](str.md)| This parameter is used for finding stories with belonging to one of clusters in a specific set of clusters You can read more about working with clustering [here](https://newsapi.aylien.com/docs/working-with-clustering).  | [optional] 
 **aql** | **str**| This parameter is used to supply a query in AYLIEN Query Language.  | [optional] 
 **aql_default_field** | **str**| This parameter is used to supply an optional default field name used in the AQL query.  | [optional] [default to &#39;text&#39;]
 **query** | **str**| This parameter is used to make an advanced query using $and, $or, $not logical operators and $eq for exact match, $text for a text search and $lt, $gt, $lte, $gte for range queries. value must be a json string.  | [optional] 

### Return type

[**Trends**](Trends.md)

### Authorization

[app_id](../README.md#app_id), [app_key](../README.md#app_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An object including an array of trends |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**492** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

