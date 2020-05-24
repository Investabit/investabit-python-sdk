# swagger_client.PrivateApi

All URIs are relative to *https://api.cryptoweather.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_private_accuracy_symbol_interval_period_get**](PrivateApi.md#v1_private_accuracy_symbol_interval_period_get) | **GET** /v1/private/accuracy/{symbol}/{interval}/{period} | Accuracy
[**v1_private_forecast_accuracy_symbol_interval_period_get**](PrivateApi.md#v1_private_forecast_accuracy_symbol_interval_period_get) | **GET** /v1/private/forecast-accuracy/{symbol}/{interval}/{period} | Forecast Accuracy
[**v1_private_forecast_symbol_interval_get**](PrivateApi.md#v1_private_forecast_symbol_interval_get) | **GET** /v1/private/forecast/{symbol}/{interval} | Forecast
[**v1_private_forecast_time_symbol_interval_period_get**](PrivateApi.md#v1_private_forecast_time_symbol_interval_period_get) | **GET** /v1/private/forecast-time/{symbol}/{interval}/{period} | Forecast Time
[**v1_private_trend_symbol_get**](PrivateApi.md#v1_private_trend_symbol_get) | **GET** /v1/private/trend/{symbol} | Trend
[**v1_private_trend_tabular_get**](PrivateApi.md#v1_private_trend_tabular_get) | **GET** /v1/private/trend-tabular | Trend Tabular


# **v1_private_accuracy_symbol_interval_period_get**
> PrivateAccuracyResponse v1_private_accuracy_symbol_interval_period_get(symbol, interval, period, cookie=cookie, x_csrf=x_csrf)

Accuracy

The accuracy response contains the following attributes.  + `rmse` Root Mean Square Error  + `mae` Mean Absolute error  + `r2` R Squared  + `ci` Confidence Interval lower and upper error bounds

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PrivateApi(swagger_client.ApiClient(configuration))
symbol = 'btc' # str | The cryptocurrency symbol.
interval = '1h' # str | The forecast interval, 1h or 1d.
period = '7d' # str | The period for computing the accuracy, such as the past 7 days.
cookie = 'csrf=b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89 (optional)
x_csrf = 'b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. b1820141-1bad-4a9c-93c0-52022817ce89 (optional)

try:
    # Accuracy
    api_response = api_instance.v1_private_accuracy_symbol_interval_period_get(symbol, interval, period, cookie=cookie, x_csrf=x_csrf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->v1_private_accuracy_symbol_interval_period_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol. | 
 **interval** | **str**| The forecast interval, 1h or 1d. | 
 **period** | **str**| The period for computing the accuracy, such as the past 7 days. | 
 **cookie** | **str**| e.g. csrf&#x3D;b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 
 **x_csrf** | **str**| e.g. b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 

### Return type

[**PrivateAccuracyResponse**](PrivateAccuracyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_forecast_accuracy_symbol_interval_period_get**
> PrivateForecastAccuracyResponse v1_private_forecast_accuracy_symbol_interval_period_get(symbol, interval, period, cookie=cookie, x_csrf=x_csrf)

Forecast Accuracy



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PrivateApi(swagger_client.ApiClient(configuration))
symbol = 'btc' # str | The cryptocurrency symbol.
interval = '1h' # str | The forecast interval, 1h or 1d.
period = '7d' # str | The period for computing the error bounds, typically 7d or 30d.
cookie = 'csrf=b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89 (optional)
x_csrf = 'b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. b1820141-1bad-4a9c-93c0-52022817ce89 (optional)

try:
    # Forecast Accuracy
    api_response = api_instance.v1_private_forecast_accuracy_symbol_interval_period_get(symbol, interval, period, cookie=cookie, x_csrf=x_csrf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->v1_private_forecast_accuracy_symbol_interval_period_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol. | 
 **interval** | **str**| The forecast interval, 1h or 1d. | 
 **period** | **str**| The period for computing the error bounds, typically 7d or 30d. | 
 **cookie** | **str**| e.g. csrf&#x3D;b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 
 **x_csrf** | **str**| e.g. b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 

### Return type

[**PrivateForecastAccuracyResponse**](PrivateForecastAccuracyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_forecast_symbol_interval_get**
> PrivateForecastResponse v1_private_forecast_symbol_interval_get(symbol, interval, cookie=cookie, x_csrf=x_csrf)

Forecast

The forecast response contains a sequence of forecasts at the specified intervals, with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `low` forecasted high during the period  + `high` forecasted low during the period  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PrivateApi(swagger_client.ApiClient(configuration))
symbol = 'btc' # str | The cryptocurrency symbol.
interval = '1h' # str | The forecast interval, 1h or 1d.
cookie = 'csrf=b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89 (optional)
x_csrf = 'b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. b1820141-1bad-4a9c-93c0-52022817ce89 (optional)

try:
    # Forecast
    api_response = api_instance.v1_private_forecast_symbol_interval_get(symbol, interval, cookie=cookie, x_csrf=x_csrf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->v1_private_forecast_symbol_interval_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol. | 
 **interval** | **str**| The forecast interval, 1h or 1d. | 
 **cookie** | **str**| e.g. csrf&#x3D;b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 
 **x_csrf** | **str**| e.g. b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 

### Return type

[**PrivateForecastResponse**](PrivateForecastResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_forecast_time_symbol_interval_period_get**
> PrivateForecastTimeResponse v1_private_forecast_time_symbol_interval_period_get(symbol, interval, period, cookie=cookie, x_csrf=x_csrf)

Forecast Time



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PrivateApi(swagger_client.ApiClient(configuration))
symbol = 'btc' # str | The cryptocurrency symbol.
interval = '1h' # str | The forecast interval, 1h or 1d.
period = '7d' # str | The period for computing the error bounds, typically 7d or 30d.
cookie = 'csrf=b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89 (optional)
x_csrf = 'b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. b1820141-1bad-4a9c-93c0-52022817ce89 (optional)

try:
    # Forecast Time
    api_response = api_instance.v1_private_forecast_time_symbol_interval_period_get(symbol, interval, period, cookie=cookie, x_csrf=x_csrf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->v1_private_forecast_time_symbol_interval_period_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol. | 
 **interval** | **str**| The forecast interval, 1h or 1d. | 
 **period** | **str**| The period for computing the error bounds, typically 7d or 30d. | 
 **cookie** | **str**| e.g. csrf&#x3D;b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 
 **x_csrf** | **str**| e.g. b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 

### Return type

[**PrivateForecastTimeResponse**](PrivateForecastTimeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_trend_symbol_get**
> PublicTrendResponse v1_private_trend_symbol_get(symbol, cookie=cookie, x_csrf=x_csrf)

Trend

The trend response contains a collection of forecasts for different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PrivateApi(swagger_client.ApiClient(configuration))
symbol = 'btc' # str | The cryptocurrency symbol.
cookie = 'csrf=b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89 (optional)
x_csrf = 'b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. b1820141-1bad-4a9c-93c0-52022817ce89 (optional)

try:
    # Trend
    api_response = api_instance.v1_private_trend_symbol_get(symbol, cookie=cookie, x_csrf=x_csrf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->v1_private_trend_symbol_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| The cryptocurrency symbol. | 
 **cookie** | **str**| e.g. csrf&#x3D;b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 
 **x_csrf** | **str**| e.g. b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 

### Return type

[**PublicTrendResponse**](PublicTrendResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_private_trend_tabular_get**
> PrivateTrendTabularResponse v1_private_trend_tabular_get(cookie=cookie, x_csrf=x_csrf)

Trend Tabular

The trend tabular response contains a collection of forecasts for all supported cryptocurrencies at different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PrivateApi(swagger_client.ApiClient(configuration))
cookie = 'csrf=b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89 (optional)
x_csrf = 'b1820141-1bad-4a9c-93c0-52022817ce89' # str | e.g. b1820141-1bad-4a9c-93c0-52022817ce89 (optional)

try:
    # Trend Tabular
    api_response = api_instance.v1_private_trend_tabular_get(cookie=cookie, x_csrf=x_csrf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivateApi->v1_private_trend_tabular_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cookie** | **str**| e.g. csrf&#x3D;b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 
 **x_csrf** | **str**| e.g. b1820141-1bad-4a9c-93c0-52022817ce89 | [optional] 

### Return type

[**PrivateTrendTabularResponse**](PrivateTrendTabularResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

