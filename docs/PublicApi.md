# swagger_client.PublicApi

All URIs are relative to *https://api.cryptoweather.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_public_price_change_symbol_get**](PublicApi.md#v1_public_price_change_symbol_get) | **GET** /v1/public/price-change/{symbol} | Price Change
[**v1_public_price_current_symbol_get**](PublicApi.md#v1_public_price_current_symbol_get) | **GET** /v1/public/price-current/{symbol} | Price Current
[**v1_public_price_history_symbol_period_interval_get**](PublicApi.md#v1_public_price_history_symbol_period_interval_get) | **GET** /v1/public/price-history/{symbol}/{period}/{interval} | Price History
[**v1_public_symbols_get**](PublicApi.md#v1_public_symbols_get) | **GET** /v1/public/symbols | Symbols
[**v1_public_trend_symbol_get**](PublicApi.md#v1_public_trend_symbol_get) | **GET** /v1/public/trend/{symbol} | Trend


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

The trend response contains a collection of forecasts for different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price

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

