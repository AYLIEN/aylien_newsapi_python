AYLIEN News API
===============

AYLIEN News API is the most powerful way of sourcing, searching and
syndicating analyzed and enriched news content. If you haven't already
done so, you will need to `sign
up <https://newsapi.aylien.com/signup>`__.

Visit our `interactive documentation <https://newsapi.aylien.com/docs/#swagger-ui-container>`__ to familiarize yourself with the API.

Requirements.
-------------

Python 2.7 and 3.4+

Installation & Usage
--------------------

PyPI
~~~~

Install it directly from PyPI repository:

.. code:: sh

    pip install aylien_news_api

(or ``sudo pip install aylien_news_api`` to install the package for all
users)

Git
~~~

Install it via:

.. code:: sh

    pip install git+https://github.com/AYLIEN/aylien_newsapi_python.git

(you may need to run ``pip`` with root permission:
``sudo pip install git+https://github.com/AYLIEN/aylien_newsapi_python.git``)

Then import the package:

.. code:: python

    import aylien_news_api 

Getting Started
---------------

Please follow the `installation procedure <#installation--usage>`__ and
then run the following:

.. code:: python

    import aylien_news_api
    from aylien_news_api.rest import ApiException

    # Configure API key authorization: app_id
    aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'YOUR_APP_ID'
    # Configure API key authorization: app_key
    aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = 'YOUR_APP_KEY'

    # create an instance of the API class
    api_instance = aylien_news_api.DefaultApi()

    title = 'trump'
    sort_by = 'social_shares_count.facebook'
    language = ['en']
    since = 'NOW-7DAYS'
    until = 'NOW'
    entities = [
      'http://dbpedia.org/resource/Donald_Trump',
      'http://dbpedia.org/resource/Hillary_Rodham_Clinton'
    ]

    try:
        # List stories
        api_response = api_instance.list_stories(title=title, language=language, published_at_start=since, published_at_end=until, entities_body_links_dbpedia=entities, sort_by=sort_by)
        print(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)

Documentation for API Endpoints
-------------------------------

All URIs are relative to \*\ https://api.newsapi.aylien.com/api/v1*

+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+
| Class          | Method                                                                     | HTTP request                 | Description            |
+================+============================================================================+==============================+========================+
| *DefaultApi*   | `**list\_autocompletes** <docs/DefaultApi.md#list_autocompletes>`__        | **GET** /autocompletes       | List autocompletes     |
+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+
| *DefaultApi*   | `**list\_coverages** <docs/DefaultApi.md#list_coverages>`__                | **POST** /coverages          | List coverages         |
+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+
| *DefaultApi*   | `**list\_histograms** <docs/DefaultApi.md#list_histograms>`__              | **GET** /histograms          | List histograms        |
+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+
| *DefaultApi*   | `**list\_related\_stories** <docs/DefaultApi.md#list_related_stories>`__   | **POST** /related\_stories   | List related stories   |
+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+
| *DefaultApi*   | `**list\_stories** <docs/DefaultApi.md#list_stories>`__                    | **GET** /stories             | List Stories           |
+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+
| *DefaultApi*   | `**list\_time\_series** <docs/DefaultApi.md#list_time_series>`__           | **GET** /time\_series        | List time series       |
+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+
| *DefaultApi*   | `**list\_trends** <docs/DefaultApi.md#list_trends>`__                      | **GET** /trends              | List trends            |
+----------------+----------------------------------------------------------------------------+------------------------------+------------------------+

Documentation For Models
------------------------

-  `Author <docs/Author.md>`__
-  `Autocomplete <docs/Autocomplete.md>`__
-  `Autocompletes <docs/Autocompletes.md>`__
-  `Category <docs/Category.md>`__
-  `CategoryLinks <docs/CategoryLinks.md>`__
-  `Coverages <docs/Coverages.md>`__
-  `Entities <docs/Entities.md>`__
-  `Entity <docs/Entity.md>`__
-  `EntityLinks <docs/EntityLinks.md>`__
-  `Error <docs/Error.md>`__
-  `ErrorLinks <docs/ErrorLinks.md>`__
-  `Errors <docs/Errors.md>`__
-  `HistogramInterval <docs/HistogramInterval.md>`__
-  `Histograms <docs/Histograms.md>`__
-  `Location <docs/Location.md>`__
-  `Media <docs/Media.md>`__
-  `RelatedStories <docs/RelatedStories.md>`__
-  `Scope <docs/Scope.md>`__
-  `Sentiment <docs/Sentiment.md>`__
-  `Sentiments <docs/Sentiments.md>`__
-  `ShareCount <docs/ShareCount.md>`__
-  `ShareCounts <docs/ShareCounts.md>`__
-  `Source <docs/Source.md>`__
-  `Stories <docs/Stories.md>`__
-  `Story <docs/Story.md>`__
-  `StoryCluster <docs/StoryCluster.md>`__
-  `StoryLinks <docs/StoryLinks.md>`__
-  `Summary <docs/Summary.md>`__
-  `TimeSeries <docs/TimeSeries.md>`__
-  `TimeSeriesList <docs/TimeSeriesList.md>`__
-  `Trend <docs/Trend.md>`__
-  `Trends <docs/Trends.md>`__

Documentation For Authorization
-------------------------------

app\_id
-------

-  **Type**: API key
-  **API key parameter name**: X-AYLIEN-NewsAPI-Application-ID
-  **Location**: HTTP header

app\_key
--------

-  **Type**: API key
-  **API key parameter name**: X-AYLIEN-NewsAPI-Application-Key
-  **Location**: HTTP header
