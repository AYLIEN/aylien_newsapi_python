# aylien_news_api.AutocompleteApi

All URIs are relative to *https://api.aylien.com/news*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_autocompletes**](AutocompleteApi.md#list_autocompletes) | **GET** /autocompletes | List autocompletes


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
api_instance = aylien_news_api.AutocompleteApi(aylien_news_api.ApiClient(configuration))
type = 'source_names' # str | This parameter is used for defining the type of autocompletes. 
term = 'News' # str | This parameter is used for finding autocomplete objects that contain the specified value. 
language = 'en' # str | This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'en')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

try:
    # List autocompletes
    api_response = api_instance.list_autocompletes(type, term, language=language, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->list_autocompletes: %s\n" % e)
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
api_instance = aylien_news_api.AutocompleteApi(aylien_news_api.ApiClient(configuration))
type = 'source_names' # str | This parameter is used for defining the type of autocompletes. 
term = 'News' # str | This parameter is used for finding autocomplete objects that contain the specified value. 
language = 'en' # str | This parameter is used for autocompletes whose language is the specified value. It supports [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language codes.  (optional) (default to 'en')
per_page = 3 # int | This parameter is used for specifying number of items in each page.  (optional) (default to 3)

try:
    # List autocompletes
    api_response = api_instance.list_autocompletes(type, term, language=language, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->list_autocompletes: %s\n" % e)
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
**429** | Too Many Requests |  * X-RateLimit-Limit - The number of allowed requests in the current period. <br>  * X-RateLimit-Remaining - The number of remaining requests in the current period. <br>  * X-RateLimit-Reset - The remaining window before the rate limit resets in UTC [epoch seconds](https://en.wikipedia.org/wiki/Unix_time).  <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

