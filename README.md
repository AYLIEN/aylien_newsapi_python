# aylien_news_api
The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.2.2
- Package version: 5.2.2
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://newsapi.aylien.com/](https://newsapi.aylien.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import aylien_news_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import aylien_news_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.aylien.com/news*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**advanced_list_stories**](docs/DefaultApi.md#advanced_list_stories) | **POST** /stories | List Stories
*DefaultApi* | [**list_autocompletes**](docs/DefaultApi.md#list_autocompletes) | **GET** /autocompletes | List autocompletes
*DefaultApi* | [**list_clusters**](docs/DefaultApi.md#list_clusters) | **GET** /clusters | List Clusters
*DefaultApi* | [**list_histograms**](docs/DefaultApi.md#list_histograms) | **GET** /histograms | List histograms
*DefaultApi* | [**list_related_stories_get**](docs/DefaultApi.md#list_related_stories_get) | **GET** /related_stories | 
*DefaultApi* | [**list_related_stories_post**](docs/DefaultApi.md#list_related_stories_post) | **POST** /related_stories | 
*DefaultApi* | [**list_stories**](docs/DefaultApi.md#list_stories) | **GET** /stories | List Stories
*DefaultApi* | [**list_time_series**](docs/DefaultApi.md#list_time_series) | **GET** /time_series | List time series
*DefaultApi* | [**list_trends**](docs/DefaultApi.md#list_trends) | **GET** /trends | List trends


## Documentation For Models

 - [AggregatedSentiment](docs/AggregatedSentiment.md)
 - [Author](docs/Author.md)
 - [Autocomplete](docs/Autocomplete.md)
 - [Autocompletes](docs/Autocompletes.md)
 - [Category](docs/Category.md)
 - [CategoryLinks](docs/CategoryLinks.md)
 - [CategoryTaxonomy](docs/CategoryTaxonomy.md)
 - [Cluster](docs/Cluster.md)
 - [Clusters](docs/Clusters.md)
 - [DunsNumber](docs/DunsNumber.md)
 - [Entity](docs/Entity.md)
 - [EntityInText](docs/EntityInText.md)
 - [EntityLinks](docs/EntityLinks.md)
 - [EntityMention](docs/EntityMention.md)
 - [EntityMentionIndex](docs/EntityMentionIndex.md)
 - [EntitySentiment](docs/EntitySentiment.md)
 - [EntitySurfaceForm](docs/EntitySurfaceForm.md)
 - [Error](docs/Error.md)
 - [ErrorLinks](docs/ErrorLinks.md)
 - [Errors](docs/Errors.md)
 - [ExternalIds](docs/ExternalIds.md)
 - [HistogramInterval](docs/HistogramInterval.md)
 - [Histograms](docs/Histograms.md)
 - [Location](docs/Location.md)
 - [Logicals](docs/Logicals.md)
 - [Media](docs/Media.md)
 - [MediaFormat](docs/MediaFormat.md)
 - [MediaType](docs/MediaType.md)
 - [NestedEntity](docs/NestedEntity.md)
 - [Parameter](docs/Parameter.md)
 - [Query](docs/Query.md)
 - [Rank](docs/Rank.md)
 - [Rankings](docs/Rankings.md)
 - [RelatedStories](docs/RelatedStories.md)
 - [RepresentativeStory](docs/RepresentativeStory.md)
 - [Scope](docs/Scope.md)
 - [ScopeLevel](docs/ScopeLevel.md)
 - [Sentiment](docs/Sentiment.md)
 - [SentimentPolarity](docs/SentimentPolarity.md)
 - [Sentiments](docs/Sentiments.md)
 - [ShareCount](docs/ShareCount.md)
 - [ShareCounts](docs/ShareCounts.md)
 - [Source](docs/Source.md)
 - [Stories](docs/Stories.md)
 - [Story](docs/Story.md)
 - [StoryCluster](docs/StoryCluster.md)
 - [StoryLinks](docs/StoryLinks.md)
 - [StoryTranslation](docs/StoryTranslation.md)
 - [StoryTranslations](docs/StoryTranslations.md)
 - [Summary](docs/Summary.md)
 - [TimeSeries](docs/TimeSeries.md)
 - [TimeSeriesList](docs/TimeSeriesList.md)
 - [Trend](docs/Trend.md)
 - [Trends](docs/Trends.md)
 - [Warning](docs/Warning.md)


## Documentation For Authorization


## app_id

- **Type**: API key
- **API key parameter name**: X-AYLIEN-NewsAPI-Application-ID
- **Location**: HTTP header


## app_key

- **Type**: API key
- **API key parameter name**: X-AYLIEN-NewsAPI-Application-Key
- **Location**: HTTP header


## Author

support@aylien.com


