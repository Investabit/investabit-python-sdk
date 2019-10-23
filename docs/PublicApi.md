# swagger_client.PublicApi

All URIs are relative to *https://api.investabit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_public_price_change_symbol_get**](PublicApi.md#v1_public_price_change_symbol_get) | **GET** /v1/public/price-change/{symbol} | Price Change
[**v1_public_price_current_symbol_get**](PublicApi.md#v1_public_price_current_symbol_get) | **GET** /v1/public/price-current/{symbol} | Price Current
[**v1_public_price_history_symbol_period_interval_get**](PublicApi.md#v1_public_price_history_symbol_period_interval_get) | **GET** /v1/public/price-history/{symbol}/{period}/{interval} | Price History
[**v1_public_symbols_get**](PublicApi.md#v1_public_symbols_get) | **GET** /v1/public/symbols | Symbols
[**v1_public_trend_symbol_get**](PublicApi.md#v1_public_trend_symbol_get) | **GET** /v1/public/trend/{symbol} | Trend
[**v1_public_waiting_list_post**](PublicApi.md#v1_public_waiting_list_post) | **POST** /v1/public/waiting-list | Waiting List


# **v1_public_price_change_symbol_get**
> PublicPriceChangeResponse v1_public_price_change_symbol_get(symbol)

Price Change



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicApi()
symbol = 'btc' # str | The cryptocurrency symbol.

try:
    # Price Change
    api_response = api_instance.v1_public_price_change_symbol_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_price_change_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol. | 

### Return type

[**PublicPriceChangeResponse**](PublicPriceChangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_price_current_symbol_get**
> PublicPriceCurrentResponse v1_public_price_current_symbol_get(symbol)

Price Current



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicApi()
symbol = 'btc' # str | The cryptocurrency symbol, provide `all` to get every symbol.

try:
    # Price Current
    api_response = api_instance.v1_public_price_current_symbol_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_price_current_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol, provide &#x60;all&#x60; to get every symbol. | 

### Return type

[**PublicPriceCurrentResponse**](PublicPriceCurrentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_price_history_symbol_period_interval_get**
> PublicPriceHistoryResponse v1_public_price_history_symbol_period_interval_get(symbol, period, interval)

Price History



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicApi()
symbol = 'btc' # str | The cryptocurrency symbol, provide `all` to get every symbol.
period = '30d' # str | The period to get data for, such as past 30 days.
interval = '1d' # str | The bar interval, such as 1 day.

try:
    # Price History
    api_response = api_instance.v1_public_price_history_symbol_period_interval_get(symbol, period, interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_price_history_symbol_period_interval_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol, provide &#x60;all&#x60; to get every symbol. | 
 **period** | **str**| The period to get data for, such as past 30 days. | 
 **interval** | **str**| The bar interval, such as 1 day. | 

### Return type

[**PublicPriceHistoryResponse**](PublicPriceHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_symbols_get**
> PublicSymbolsResponse v1_public_symbols_get()

Symbols



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicApi()

try:
    # Symbols
    api_response = api_instance.v1_public_symbols_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_symbols_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicSymbolsResponse**](PublicSymbolsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_trend_symbol_get**
> PublicTrendResponse v1_public_trend_symbol_get(symbol)

Trend



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicApi()
symbol = 'btc' # str | The cryptocurrency symbol.

try:
    # Trend
    api_response = api_instance.v1_public_trend_symbol_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_trend_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol. | 

### Return type

[**PublicTrendResponse**](PublicTrendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_waiting_list_post**
> DefaultResponse v1_public_waiting_list_post(body=body)

Waiting List

Subscribe a user to the waiting list, `name` is not required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicApi()
body = swagger_client.PublicWaitingListRequest() # PublicWaitingListRequest |  (optional)

try:
    # Waiting List
    api_response = api_instance.v1_public_waiting_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_waiting_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PublicWaitingListRequest**](PublicWaitingListRequest.md)|  | [optional] 

### Return type

[**DefaultResponse**](DefaultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

