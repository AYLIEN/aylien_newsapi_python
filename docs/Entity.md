# Entity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the entity | [optional] 
**links** | [**EntityLinks**](EntityLinks.md) |  | [optional] 
**stock_tickers** | **[str]** | The stock tickers of the entity (might be empty) | [optional] 
**types** | **[str]** | An array of the entity types | [optional] 
**overall_sentiment** | [**EntitySentiment**](EntitySentiment.md) |  | [optional] 
**overall_prominence** | **float** | Describes how relevant an entity is to the article | [optional] 
**overall_frequency** | **int** | Amount of entity surface form mentions in the article | [optional] 
**body** | [**EntityInText**](EntityInText.md) |  | [optional] 
**title** | [**EntityInText**](EntityInText.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


