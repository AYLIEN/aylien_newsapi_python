# Story

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the story which is a unique identification | [optional] 
**title** | **str** | Title of the story | [optional] 
**body** | **str** | Body of the story | [optional] 
**summary** | [**Summary**](Summary.md) | The suggested story summary | [optional] 
**source** | [**Source**](Source.md) | The story source | [optional] 
**author** | [**Author**](Author.md) | The story author | [optional] 
**entities** | [**Entities**](Entities.md) | Extracted entities from the story title or body | [optional] 
**keywords** | **list[str]** | Extracted keywords mentioned in the story title or body | [optional] 
**hashtags** | **list[str]** | An array of suggested Story hashtags | [optional] 
**characters_count** | **int** | Character count of the story body | [optional] 
**words_count** | **int** | Word count of the story body | [optional] 
**sentences_count** | **int** | Sentence count of the story body | [optional] 
**paragraphs_count** | **int** | Paragraph count of the story body | [optional] 
**categories** | [**list[Category]**](Category.md) | Suggested categories for the story | [optional] 
**social_shares_count** | [**ShareCounts**](ShareCounts.md) | Social shares count for the story | [optional] 
**media** | [**list[Media]**](Media.md) | An array of extracted media such as images and videos | [optional] 
**sentiment** | [**Sentiments**](Sentiments.md) | Suggested sentiments for the story title or body | [optional] 
**language** | **str** | Language of the story | [optional] 
**published_at** | **datetime** | Published date of the story | [optional] 
**links** | [**StoryLinks**](StoryLinks.md) | Links which is related to the story | [optional] 

[[Back to Model list]](../README.rst#documentation-for-models) [[Back to API list]](../README.rst#documentation-for-api-endpoints) [[Back to README]](../README.rst)


