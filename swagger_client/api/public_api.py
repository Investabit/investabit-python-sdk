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


class PublicApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_public_price_change_symbol_get(self, symbol, **kwargs):  # noqa: E501
        """Price Change  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_price_change_symbol_get(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :return: PublicPriceChangeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_public_price_change_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_public_price_change_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def v1_public_price_change_symbol_get_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """Price Change  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_price_change_symbol_get_with_http_info(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :return: PublicPriceChangeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_price_change_symbol_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_public_price_change_symbol_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/public/price-change/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicPriceChangeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_public_price_current_symbol_get(self, symbol, **kwargs):  # noqa: E501
        """Price Current  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_price_current_symbol_get(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol, provide `all` to get every symbol. (required)
        :return: PublicPriceCurrentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_public_price_current_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_public_price_current_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def v1_public_price_current_symbol_get_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """Price Current  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_price_current_symbol_get_with_http_info(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol, provide `all` to get every symbol. (required)
        :return: PublicPriceCurrentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_price_current_symbol_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_public_price_current_symbol_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/public/price-current/{symbol}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicPriceCurrentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_public_price_history_symbol_period_interval_get(self, symbol, period, interval, **kwargs):  # noqa: E501
        """Price History  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_price_history_symbol_period_interval_get(symbol, period, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol, provide `all` to get every symbol. (required)
        :param str period: The period to get data for, such as past 30 days. (required)
        :param str interval: The bar interval, such as 1 day. (required)
        :return: PublicPriceHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_public_price_history_symbol_period_interval_get_with_http_info(symbol, period, interval, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_public_price_history_symbol_period_interval_get_with_http_info(symbol, period, interval, **kwargs)  # noqa: E501
            return data

    def v1_public_price_history_symbol_period_interval_get_with_http_info(self, symbol, period, interval, **kwargs):  # noqa: E501
        """Price History  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_price_history_symbol_period_interval_get_with_http_info(symbol, period, interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol, provide `all` to get every symbol. (required)
        :param str period: The period to get data for, such as past 30 days. (required)
        :param str interval: The bar interval, such as 1 day. (required)
        :return: PublicPriceHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'period', 'interval']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_price_history_symbol_period_interval_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_public_price_history_symbol_period_interval_get`")  # noqa: E501
        # verify the required parameter 'period' is set
        if ('period' not in params or
                params['period'] is None):
            raise ValueError("Missing the required parameter `period` when calling `v1_public_price_history_symbol_period_interval_get`")  # noqa: E501
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `v1_public_price_history_symbol_period_interval_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501
        if 'period' in params:
            path_params['period'] = params['period']  # noqa: E501
        if 'interval' in params:
            path_params['interval'] = params['interval']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/public/price-history/{symbol}/{period}/{interval}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicPriceHistoryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_public_summary_get(self, **kwargs):  # noqa: E501
        """Summary  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_summary_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PublicSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_public_summary_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_public_summary_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_public_summary_get_with_http_info(self, **kwargs):  # noqa: E501
        """Summary  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_summary_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PublicSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_summary_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/public/summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicSummaryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_public_symbols_get(self, **kwargs):  # noqa: E501
        """Symbols  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_symbols_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PublicSymbolsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_public_symbols_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_public_symbols_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_public_symbols_get_with_http_info(self, **kwargs):  # noqa: E501
        """Symbols  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_symbols_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PublicSymbolsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_symbols_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/public/symbols', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicSymbolsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_public_trend_symbol_get(self, symbol, **kwargs):  # noqa: E501
        """Trend  # noqa: E501

        The trend response contains a collection of forecasts for different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_trend_symbol_get(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :return: PublicTrendResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_public_trend_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_public_trend_symbol_get_with_http_info(symbol, **kwargs)  # noqa: E501
            return data

    def v1_public_trend_symbol_get_with_http_info(self, symbol, **kwargs):  # noqa: E501
        """Trend  # noqa: E501

        The trend response contains a collection of forecasts for different intervals with the following attributes.  + `time_start` start time of the period the forecast is applicable for  + `time_end` end time of the period the forecast is applicable for  + `interval` interval in hours that the forecast is applicable for  + `weighted_price` forecasted weighted price during the period  + `change_pct` percent change in price for forecasted weighted_price relative to current price  + `change_usd` dollar change in price for forecasted weighted_price relative to current price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_public_trend_symbol_get_with_http_info(symbol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str symbol: The cryptocurrency symbol. (required)
        :return: PublicTrendResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_public_trend_symbol_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'symbol' is set
        if ('symbol' not in params or
                params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `v1_public_trend_symbol_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'symbol' in params:
            path_params['symbol'] = params['symbol']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/public/trend/{symbol}', 'GET',
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
