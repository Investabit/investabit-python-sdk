# swagger_client.PublicApi

All URIs are relative to *https://api.investabit.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_public_current_symbol_get**](PublicApi.md#v1_public_current_symbol_get) | **GET** /v1/public/current/{symbol} | Current
[**v1_public_price_history_symbol_get**](PublicApi.md#v1_public_price_history_symbol_get) | **GET** /v1/public/price-history/{symbol} | Price History
[**v1_public_symbols_get**](PublicApi.md#v1_public_symbols_get) | **GET** /v1/public/symbols | Symbols
[**v1_public_trend_symbol_get**](PublicApi.md#v1_public_trend_symbol_get) | **GET** /v1/public/trend/{symbol} | Trend


# **v1_public_current_symbol_get**
> PublicCurrentResponse v1_public_current_symbol_get(symbol)

Current



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PublicApi()
symbol = '\"btc\"' # str | The cryptocurrency symbol, default is btc.

try:
    # Current
    api_response = api_instance.v1_public_current_symbol_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_current_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol, default is btc. | 

### Return type

[**PublicCurrentResponse**](PublicCurrentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_public_price_history_symbol_get**
> PublicPriceResponse v1_public_price_history_symbol_get(symbol)

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
symbol = '\"btc\"' # str | The cryptocurrency symbol, default is btc.

try:
    # Price History
    api_response = api_instance.v1_public_price_history_symbol_get(symbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PublicApi->v1_public_price_history_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol, default is btc. | 

### Return type

[**PublicPriceResponse**](PublicPriceResponse.md)

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
symbol = '\"btc\"' # str | The cryptocurrency symbol, default is btc.

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
 **symbol** | **str**| The cryptocurrency symbol, default is btc. | 

### Return type

[**PublicTrendResponse**](PublicTrendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

