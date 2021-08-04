# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from aylien_news_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from aylien_news_api.model.aggregated_sentiment import AggregatedSentiment
from aylien_news_api.model.author import Author
from aylien_news_api.model.autocomplete import Autocomplete
from aylien_news_api.model.autocompletes import Autocompletes
from aylien_news_api.model.category import Category
from aylien_news_api.model.category_links import CategoryLinks
from aylien_news_api.model.category_taxonomy import CategoryTaxonomy
from aylien_news_api.model.cluster import Cluster
from aylien_news_api.model.clusters import Clusters
from aylien_news_api.model.deprecated_entities import DeprecatedEntities
from aylien_news_api.model.deprecated_entity import DeprecatedEntity
from aylien_news_api.model.deprecated_entity_surface_form import DeprecatedEntitySurfaceForm
from aylien_news_api.model.deprecated_related_stories import DeprecatedRelatedStories
from aylien_news_api.model.deprecated_stories import DeprecatedStories
from aylien_news_api.model.deprecated_story import DeprecatedStory
from aylien_news_api.model.entity import Entity
from aylien_news_api.model.entity_in_text import EntityInText
from aylien_news_api.model.entity_links import EntityLinks
from aylien_news_api.model.entity_mention import EntityMention
from aylien_news_api.model.entity_mention_index import EntityMentionIndex
from aylien_news_api.model.entity_sentiment import EntitySentiment
from aylien_news_api.model.entity_surface_form import EntitySurfaceForm
from aylien_news_api.model.error import Error
from aylien_news_api.model.error_links import ErrorLinks
from aylien_news_api.model.errors import Errors
from aylien_news_api.model.histogram_interval import HistogramInterval
from aylien_news_api.model.histograms import Histograms
from aylien_news_api.model.location import Location
from aylien_news_api.model.logical import Logical
from aylien_news_api.model.logicals import Logicals
from aylien_news_api.model.media import Media
from aylien_news_api.model.media_format import MediaFormat
from aylien_news_api.model.media_type import MediaType
from aylien_news_api.model.nested_entity import NestedEntity
from aylien_news_api.model.parameter import Parameter
from aylien_news_api.model.query import Query
from aylien_news_api.model.rank import Rank
from aylien_news_api.model.rankings import Rankings
from aylien_news_api.model.related_stories import RelatedStories
from aylien_news_api.model.representative_story import RepresentativeStory
from aylien_news_api.model.scope import Scope
from aylien_news_api.model.scope_level import ScopeLevel
from aylien_news_api.model.sentiment import Sentiment
from aylien_news_api.model.sentiment_polarity import SentimentPolarity
from aylien_news_api.model.sentiments import Sentiments
from aylien_news_api.model.share_count import ShareCount
from aylien_news_api.model.share_counts import ShareCounts
from aylien_news_api.model.source import Source
from aylien_news_api.model.stories import Stories
from aylien_news_api.model.story import Story
from aylien_news_api.model.story_cluster import StoryCluster
from aylien_news_api.model.story_links import StoryLinks
from aylien_news_api.model.story_translation import StoryTranslation
from aylien_news_api.model.story_translations import StoryTranslations
from aylien_news_api.model.summary import Summary
from aylien_news_api.model.time_series import TimeSeries
from aylien_news_api.model.time_series_list import TimeSeriesList
from aylien_news_api.model.trend import Trend
from aylien_news_api.model.trends import Trends
from aylien_news_api.model.warning import Warning
