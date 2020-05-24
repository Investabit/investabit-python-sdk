# coding: utf-8

# flake8: noqa
"""
    CryptoWeather

    The CryptoWeather API allows for access to all of the cryptocurrency data and market forecast services provided. There are two primary categories of routes, `public` and `private`, where `public` routes are accessible to the general public and do not require API authentication, and `private` routes, which require API authentication.  ## General Overview  1. All API methods adhere to RESTful best practices as closely as possible. As such, all API calls will be made via the standard HTTP protocol using the GET/POST/PUT/DELETE request types.  2. Every request returns the status as a JSON response with the following:     - success, true if it was successful     - code, the http status code (also in the response header)         - 200 if response is successful         - 400 if bad request         - 401 if authorization JWT is wrong or limit exceeded         - 404 wrong route         - 500 for any internal errors     - status, the status of the request, default **success**     - errors, an array of any relevant error details  3. For any requests that are not successful an error message is specified and returned as an array for the **errors** key in the JSON response.  4. All authentication uses JSON Web Tokens (JWT), which is set as the **Authorization** entry in the header, see the following for more details.     - http://jwt.io     - https://scotch.io/tutorials/the-anatomy-of-a-json-web-token  ## Code Example  The following is a code example in Python, which demonstrates using the [Python Requests library](https://requests.readthedocs.io/en/master/) for both the `public` and `private` API routes.  ``` import requests  HOST = \"https://api.cryptoweather.ai/v1\"  # Your API key (JWT) API_KEY = \"<YOUR API KEY>\"  # Example public request, no API key required. requests.get(\"{}/public/symbols\".format(HOST)).json()  # Get the current btc price using the public route requests.get(\"{}/public/price-current/{}\".format(HOST, \"btc\")).json()   # Example private request, API key required. Get the btc hourly forecasts headers = {\"Authorization\": \"Bearer {}\".format(API_KEY)} requests.get(\"{}/private/forecast/{}/{}\".format(HOST, \"btc\", \"1h\"),              headers=headers).json() ```  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.accuracy_route import AccuracyRoute
from swagger_client.models.default_response import DefaultResponse
from swagger_client.models.forecast_accuracy_route import ForecastAccuracyRoute
from swagger_client.models.forecast_route import ForecastRoute
from swagger_client.models.forecast_time_route import ForecastTimeRoute
from swagger_client.models.price_change_route import PriceChangeRoute
from swagger_client.models.price_current_route import PriceCurrentRoute
from swagger_client.models.price_history_route import PriceHistoryRoute
from swagger_client.models.private_accuracy_response import PrivateAccuracyResponse
from swagger_client.models.private_accuracy_response_data import PrivateAccuracyResponseData
from swagger_client.models.private_forecast_accuracy_response import PrivateForecastAccuracyResponse
from swagger_client.models.private_forecast_accuracy_response_data import PrivateForecastAccuracyResponseData
from swagger_client.models.private_forecast_response import PrivateForecastResponse
from swagger_client.models.private_forecast_response_data import PrivateForecastResponseData
from swagger_client.models.private_forecast_response_data_forecast import PrivateForecastResponseDataForecast
from swagger_client.models.private_forecast_time_response import PrivateForecastTimeResponse
from swagger_client.models.private_forecast_time_response_data import PrivateForecastTimeResponseData
from swagger_client.models.private_trend_tabular_response import PrivateTrendTabularResponse
from swagger_client.models.private_trend_tabular_response_data import PrivateTrendTabularResponseData
from swagger_client.models.private_trend_tabular_response_data_trend_tabular import PrivateTrendTabularResponseDataTrendTabular
from swagger_client.models.public_price_change_response import PublicPriceChangeResponse
from swagger_client.models.public_price_change_response_data import PublicPriceChangeResponseData
from swagger_client.models.public_price_change_response_data_price_change import PublicPriceChangeResponseDataPriceChange
from swagger_client.models.public_price_current_response import PublicPriceCurrentResponse
from swagger_client.models.public_price_current_response_data import PublicPriceCurrentResponseData
from swagger_client.models.public_price_current_response_data_current import PublicPriceCurrentResponseDataCurrent
from swagger_client.models.public_price_history_response import PublicPriceHistoryResponse
from swagger_client.models.public_price_history_response_data import PublicPriceHistoryResponseData
from swagger_client.models.public_price_history_response_data_history import PublicPriceHistoryResponseDataHistory
from swagger_client.models.public_price_history_response_data_price_history import PublicPriceHistoryResponseDataPriceHistory
from swagger_client.models.public_summary_response import PublicSummaryResponse
from swagger_client.models.public_summary_response_color import PublicSummaryResponseColor
from swagger_client.models.public_summary_response_data import PublicSummaryResponseData
from swagger_client.models.public_symbols_response import PublicSymbolsResponse
from swagger_client.models.public_symbols_response_data import PublicSymbolsResponseData
from swagger_client.models.public_symbols_response_data_symbols import PublicSymbolsResponseDataSymbols
from swagger_client.models.public_trend_response import PublicTrendResponse
from swagger_client.models.public_trend_response_data import PublicTrendResponseData
from swagger_client.models.public_trend_response_data_trend import PublicTrendResponseDataTrend
from swagger_client.models.summary_route import SummaryRoute
from swagger_client.models.symbols_route import SymbolsRoute
from swagger_client.models.trend_route import TrendRoute
from swagger_client.models.trend_tabluar_route import TrendTabluarRoute
