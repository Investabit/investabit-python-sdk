# coding: utf-8

"""
    CryptoWeather

    The CryptoWeather API allows for access to all of the cryptocurrency data and market forecast services provided. There are two primary categories of routes, `public` and `private`, where `public` routes are accessible to the general public and do not require API authentication, and `private` routes, which require API authentication.  ## General Overview  1. All API methods adhere to RESTful best practices as closely as possible. As such, all API calls will be made via the standard HTTP protocol using the GET/POST/PUT/DELETE request types.  2. Every request returns the status as a JSON response with the following:     - success, true if it was successful     - code, the http status code (also in the response header)         - 200 if response is successful         - 400 if bad request         - 401 if authorization JWT is wrong or limit exceeded         - 404 wrong route         - 500 for any internal errors     - status, the status of the request, default **success**     - errors, an array of any relevant error details  3. For any requests that are not successful an error message is specified and returned as an array for the **errors** key in the JSON response.  4. All authentication uses JSON Web Tokens (JWT), which is set as the **Authorization** entry in the header, see the following for more details.     - http://jwt.io     - https://scotch.io/tutorials/the-anatomy-of-a-json-web-token  ## Code Example  The following is a code example in Python, which demonstrates using the [Python Requests library](https://requests.readthedocs.io/en/master/) for both the `public` and `private` API routes.  ``` import requests  HOST = \"https://api.cryptoweather.ai/v1\"  # Your API key (JWT) API_KEY = \"<YOUR API KEY>\"  # Example public request, no API key required. requests.get(\"{}/public/symbols\".format(HOST)).json()  # Get the current btc price using the public route requests.get(\"{}/public/price-current/{}\".format(HOST, \"btc\")).json()   # Example private request, API key required. Get the btc hourly forecasts headers = {\"Authorization\": \"Bearer {}\".format(API_KEY)} requests.get(\"{}/private/forecast/{}/{}\".format(HOST, \"btc\", \"1h\"),              headers=headers).json() ```  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PrivateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_private_accuracy_symbol_interval_period_get(self, symbol, interval, period, **kwargs):  # noqa: E501
        """Accuracy  # noqa: E501

        The accuracy response contains the following attributes.  + `rmse` Root Mean Square Error  + `mae` Mean Absolute error  + `r2` R Squared  + `ci` Confidence Interval lower and upper error bounds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_accuracy_symbol_interval_period_get(symbol, interval, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str period: The period for computing the accuracy, such as the past 7 days. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateAccuracyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_private_accuracy_symbol_interval_period_get_with_http_info(symbol, interval, period, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_private_accuracy_symbol_interval_period_get_with_http_info(symbol, interval, period, **kwargs)  # noqa: E501
            return data

    def v1_private_accuracy_symbol_interval_period_get_with_http_info(self, symbol, interval, period, **kwargs):  # noqa: E501
        """Accuracy  # noqa: E501

        The accuracy response contains the following attributes.  + `rmse` Root Mean Square Error  + `mae` Mean Absolute error  + `r2` R Squared  + `ci` Confidence Interval lower and upper error bounds  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_accuracy_symbol_interval_period_get_with_http_info(symbol, interval, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str period: The period for computing the accuracy, such as the past 7 days. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateAccuracyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'interval', 'period', 'cookie', 'x_csrf']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_private_accuracy_symbol_interval_period_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_private_accuracy_symbol_interval_period_get`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `v1_private_accuracy_symbol_interval_period_get`")  # noqa: E501
        # verify the required parameter 'period' is set
        if ('period' not in params or
                params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `v1_private_accuracy_symbol_interval_period_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501
        if 'interval' in params:
            path_params['interval'] = params['interval']  # noqa: E501
        if 'period' in params:
            path_params['period'] = params['period']  # noqa: E501

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']  # noqa: E501
        if 'x_csrf' in params:
            header_params['X-csrf'] = params['x_csrf']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/private/accuracy/{symbol}/{interval}/{period}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrivateAccuracyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_private_forecast_accuracy_symbol_interval_period_get(self, symbol, interval, period, **kwargs):  # noqa: E501
        """Forecast Accuracy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_forecast_accuracy_symbol_interval_period_get(symbol, interval, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str period: The period for computing the error bounds, typically 7d or 30d. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateForecastAccuracyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_private_forecast_accuracy_symbol_interval_period_get_with_http_info(symbol, interval, period, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_private_forecast_accuracy_symbol_interval_period_get_with_http_info(symbol, interval, period, **kwargs)  # noqa: E501
            return data

    def v1_private_forecast_accuracy_symbol_interval_period_get_with_http_info(self, symbol, interval, period, **kwargs):  # noqa: E501
        """Forecast Accuracy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_forecast_accuracy_symbol_interval_period_get_with_http_info(symbol, interval, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str period: The period for computing the error bounds, typically 7d or 30d. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateForecastAccuracyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'interval', 'period', 'cookie', 'x_csrf']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_private_forecast_accuracy_symbol_interval_period_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_private_forecast_accuracy_symbol_interval_period_get`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `v1_private_forecast_accuracy_symbol_interval_period_get`")  # noqa: E501
        # verify the required parameter 'period' is set
        if ('period' not in params or
                params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `v1_private_forecast_accuracy_symbol_interval_period_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501
        if 'interval' in params:
            path_params['interval'] = params['interval']  # noqa: E501
        if 'period' in params:
            path_params['period'] = params['period']  # noqa: E501

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']  # noqa: E501
        if 'x_csrf' in params:
            header_params['X-csrf'] = params['x_csrf']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/private/forecast-accuracy/{symbol}/{interval}/{period}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrivateForecastAccuracyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_private_forecast_symbol_interval_get(self, symbol, interval, **kwargs):  # noqa: E501
        """Forecast  # noqa: E501

        The forecast response contains a sequence of forecasts at the specified intervals, with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `low` forecasted high during the period  + `high` forecasted low during the period  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_forecast_symbol_interval_get(symbol, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateForecastResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_private_forecast_symbol_interval_get_with_http_info(symbol, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_private_forecast_symbol_interval_get_with_http_info(symbol, interval, **kwargs)  # noqa: E501
            return data

    def v1_private_forecast_symbol_interval_get_with_http_info(self, symbol, interval, **kwargs):  # noqa: E501
        """Forecast  # noqa: E501

        The forecast response contains a sequence of forecasts at the specified intervals, with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `low` forecasted high during the period  + `high` forecasted low during the period  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_forecast_symbol_interval_get_with_http_info(symbol, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateForecastResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'interval', 'cookie', 'x_csrf']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_private_forecast_symbol_interval_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_private_forecast_symbol_interval_get`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `v1_private_forecast_symbol_interval_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501
        if 'interval' in params:
            path_params['interval'] = params['interval']  # noqa: E501

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']  # noqa: E501
        if 'x_csrf' in params:
            header_params['X-csrf'] = params['x_csrf']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/private/forecast/{symbol}/{interval}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrivateForecastResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_private_forecast_time_symbol_interval_period_get(self, symbol, interval, period, **kwargs):  # noqa: E501
        """Forecast Time  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_forecast_time_symbol_interval_period_get(symbol, interval, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str period: The period for computing the error bounds, typically 7d or 30d. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateForecastTimeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_private_forecast_time_symbol_interval_period_get_with_http_info(symbol, interval, period, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_private_forecast_time_symbol_interval_period_get_with_http_info(symbol, interval, period, **kwargs)  # noqa: E501
            return data

    def v1_private_forecast_time_symbol_interval_period_get_with_http_info(self, symbol, interval, period, **kwargs):  # noqa: E501
        """Forecast Time  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_forecast_time_symbol_interval_period_get_with_http_info(symbol, interval, period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str interval: The forecast interval, 1h or 1d. (required)
        :param str period: The period for computing the error bounds, typically 7d or 30d. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateForecastTimeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'interval', 'period', 'cookie', 'x_csrf']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_private_forecast_time_symbol_interval_period_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_private_forecast_time_symbol_interval_period_get`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `v1_private_forecast_time_symbol_interval_period_get`")  # noqa: E501
        # verify the required parameter 'period' is set
        if ('period' not in params or
                params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `v1_private_forecast_time_symbol_interval_period_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501
        if 'interval' in params:
            path_params['interval'] = params['interval']  # noqa: E501
        if 'period' in params:
            path_params['period'] = params['period']  # noqa: E501

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']  # noqa: E501
        if 'x_csrf' in params:
            header_params['X-csrf'] = params['x_csrf']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/private/forecast-time/{symbol}/{interval}/{period}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrivateForecastTimeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_private_trend_symbol_get(self, symbol, **kwargs):  # noqa: E501
        """Trend  # noqa: E501

        The trend response contains a collection of forecasts for different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_trend_symbol_get(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PublicTrendResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_private_trend_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_private_trend_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def v1_private_trend_symbol_get_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """Trend  # noqa: E501

        The trend response contains a collection of forecasts for different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_trend_symbol_get_with_http_info(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PublicTrendResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'cookie', 'x_csrf']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_private_trend_symbol_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_private_trend_symbol_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']  # noqa: E501
        if 'x_csrf' in params:
            header_params['X-csrf'] = params['x_csrf']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/private/trend/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicTrendResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_private_trend_tabular_get(self, **kwargs):  # noqa: E501
        """Trend Tabular  # noqa: E501

        The trend tabular response contains a collection of forecasts for all supported cryptocurrencies at different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_trend_tabular_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateTrendTabularResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_private_trend_tabular_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_private_trend_tabular_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_private_trend_tabular_get_with_http_info(self, **kwargs):  # noqa: E501
        """Trend Tabular  # noqa: E501

        The trend tabular response contains a collection of forecasts for all supported cryptocurrencies at different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_private_trend_tabular_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cookie: e.g. csrf=b1820141-1bad-4a9c-93c0-52022817ce89
        :param str x_csrf: e.g. b1820141-1bad-4a9c-93c0-52022817ce89
        :return: PrivateTrendTabularResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cookie', 'x_csrf']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_private_trend_tabular_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'cookie' in params:
            header_params['Cookie'] = params['cookie']  # noqa: E501
        if 'x_csrf' in params:
            header_params['X-csrf'] = params['x_csrf']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/private/trend-tabular', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrivateTrendTabularResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
