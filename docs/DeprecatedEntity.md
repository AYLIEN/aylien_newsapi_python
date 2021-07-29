# DeprecatedEntity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the entity | [optional] 
**indices** | **list[list[int]]** | The indices of the entity text | [optional] 
**links** | [**EntityLinks**](EntityLinks.md) |  | [optional] 
**text** | **str** | The entity text | [optional] 
**stock_ticker** | **str** | The stock_ticker of the entity (might be null) | [optional] 
**types** | **list[str]** | An array of the entity types | [optional] 
**sentiment** | [**EntitySentiment**](EntitySentiment.md) |  | [optional] 
**surface_forms** | [**list[DeprecatedEntitySurfaceForm]**](DeprecatedEntitySurfaceForm.md) |  | [optional] 
**prominence_score** | **float** | Describes how relevant an entity is to the article | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


