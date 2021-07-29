# aylien_news_api.ClusterApi

All URIs are relative to *https://api.aylien.com/news*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_clusters**](ClusterApi.md#list_clusters) | **GET** /clusters | List Clusters


# **list_clusters**
> Clusters list_clusters(id=id, id2=id2, story_count_min=story_count_min, story_count_max=story_count_max, time_start=time_start, time_end=time_end, earliest_story_start=earliest_story_start, earliest_story_end=earliest_story_end, latest_story_start=latest_story_start, latest_story_end=latest_story_end, location_country=location_country, location_country2=location_country2, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)

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
configuration = aylien_news_api.Configuration()
# Configure API key authorization: app_id
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AYLIEN-NewsAPI-Application-ID'] = 'Bearer'
configuration = aylien_news_api.Configuration()
# Configure API key authorization: app_key
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AYLIEN-NewsAPI-Application-Key'] = 'Bearer'

# Defining host is optional and default to https://api.aylien.com/news
configuration.host = "https://api.aylien.com/news"
# Create an instance of the API class
api_instance = aylien_news_api.ClusterApi(aylien_news_api.ApiClient(configuration))
id = [56] # list[int] | This parameter is used for finding clusters by cluster id.  (optional)
id2 = [56] # list[int] | This parameter is used for excluding clusters by cluster id.  (optional)
story_count_min = 56 # int | This parameter is used for finding clusters with more than or equal to a specific amount of stories associated with them.  (optional)
story_count_max = 56 # int | This parameter is used for finding clusters with less than or equal to a specific amount of stories associated with them.  (optional)
time_start = 'time_start_example' # str | This parameter is used for finding clusters whose creation time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
time_end = 'time_end_example' # str | This parameter is used for finding clusters whose creation time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_start = 'earliest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_end = 'earliest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_start = 'latest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its latest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_end = 'latest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its latest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
location_country = ['location_country_example'] # list[str] | This parameter is used for finding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
location_country2 = ['location_country_example'] # list[str] | This parameter is used for excluding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

try:
    # List Clusters
    api_response = api_instance.list_clusters(id=id, id2=id2, story_count_min=story_count_min, story_count_max=story_count_max, time_start=time_start, time_end=time_end, earliest_story_start=earliest_story_start, earliest_story_end=earliest_story_end, latest_story_start=latest_story_start, latest_story_end=latest_story_end, location_country=location_country, location_country2=location_country2, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_clusters: %s\n" % e)
```

* Api Key Authentication (app_key):
```python
from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
configuration = aylien_news_api.Configuration()
# Configure API key authorization: app_id
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AYLIEN-NewsAPI-Application-ID'] = 'Bearer'
configuration = aylien_news_api.Configuration()
# Configure API key authorization: app_key
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AYLIEN-NewsAPI-Application-Key'] = 'Bearer'

# Defining host is optional and default to https://api.aylien.com/news
configuration.host = "https://api.aylien.com/news"
# Create an instance of the API class
api_instance = aylien_news_api.ClusterApi(aylien_news_api.ApiClient(configuration))
id = [56] # list[int] | This parameter is used for finding clusters by cluster id.  (optional)
id2 = [56] # list[int] | This parameter is used for excluding clusters by cluster id.  (optional)
story_count_min = 56 # int | This parameter is used for finding clusters with more than or equal to a specific amount of stories associated with them.  (optional)
story_count_max = 56 # int | This parameter is used for finding clusters with less than or equal to a specific amount of stories associated with them.  (optional)
time_start = 'time_start_example' # str | This parameter is used for finding clusters whose creation time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
time_end = 'time_end_example' # str | This parameter is used for finding clusters whose creation time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_start = 'earliest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
earliest_story_end = 'earliest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its earliest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_start = 'latest_story_start_example' # str | This parameter is used for finding clusters whose publication date of its latest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
latest_story_end = 'latest_story_end_example' # str | This parameter is used for finding clusters whose publication date of its latest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  (optional)
location_country = ['location_country_example'] # list[str] | This parameter is used for finding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
location_country2 = ['location_country_example'] # list[str] | This parameter is used for excluding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  (optional)
_return = ['_return_example'] # list[str] | This parameter is used for specifying return fields. (optional)
sort_by = 'published_at' # str | This parameter is used for changing the order column of the results. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'published_at')
sort_direction = 'desc' # str | This parameter is used for changing the order direction of the result. You can read about sorting results [here](https://newsapi.aylien.com/docs/sorting-results).  (optional) (default to 'desc')
cursor = '*' # str | This parameter is used for finding a specific page. You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results).  (optional) (default to '*')
per_page = 10 # int | This parameter is used for specifying number of items in each page You can read more about pagination of results [here](https://newsapi.aylien.com/docs/pagination-of-results)  (optional) (default to 10)

try:
    # List Clusters
    api_response = api_instance.list_clusters(id=id, id2=id2, story_count_min=story_count_min, story_count_max=story_count_max, time_start=time_start, time_end=time_end, earliest_story_start=earliest_story_start, earliest_story_end=earliest_story_end, latest_story_start=latest_story_start, latest_story_end=latest_story_end, location_country=location_country, location_country2=location_country2, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->list_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| This parameter is used for finding clusters by cluster id.  | [optional] 
 **id2** | [**list[int]**](int.md)| This parameter is used for excluding clusters by cluster id.  | [optional] 
 **story_count_min** | **int**| This parameter is used for finding clusters with more than or equal to a specific amount of stories associated with them.  | [optional] 
 **story_count_max** | **int**| This parameter is used for finding clusters with less than or equal to a specific amount of stories associated with them.  | [optional] 
 **time_start** | **str**| This parameter is used for finding clusters whose creation time is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **time_end** | **str**| This parameter is used for finding clusters whose creation time is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **earliest_story_start** | **str**| This parameter is used for finding clusters whose publication date of its earliest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **earliest_story_end** | **str**| This parameter is used for finding clusters whose publication date of its earliest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **latest_story_start** | **str**| This parameter is used for finding clusters whose publication date of its latest story is greater than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **latest_story_end** | **str**| This parameter is used for finding clusters whose publication date of its latest story is less than the specified value. [Here](https://newsapi.aylien.com/docs/working-with-dates) you can find more information about how [to work with dates](https://newsapi.aylien.com/docs/working-with-dates).  | [optional] 
 **location_country** | [**list[str]**](str.md)| This parameter is used for finding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
 **location_country2** | [**list[str]**](str.md)| This parameter is used for excluding clusters belonging to a specific country. It supports [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country codes. [Here](https://newsapi.aylien.com/docs/working-with-locations) you can find more information about how [to work with locations](https://newsapi.aylien.com/docs/working-with-locations).  | [optional] 
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
**429** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

