# coding: utf-8

# flake8: noqa
"""
    Investabit

    The Investabit API allows for access to all of the public facing services provided, including market data and forecasts.  ## General Overview  1. All API methods will be built to adhere to RESTful best practices as closely as possible. As such, all API calls will be made via the standard HTTP protocol using the GET/POST/PUT/DELETE request types.  2. Every request returns the status as a JSON response with the following   - success, true if it was successful   - code, the http status code (also in the response header)          200 if response is successful          400 if bad request          401 if authorization JWT is wrong or limit exceeded          404 wrong route          500 for any internal errors  - status, the status of the request, default **success**  - errors, an array of any relevant error details  3. For any requests that are not successful an error message is specified and returned as an array for the **errors** key in the JSON response.  4. All authentication uses JSON Web Tokens (JWT), which is set as the **Authorization** entry in the header, see the following for more details.     * http://jwt.io     * https://scotch.io/tutorials/the-anatomy-of-a-json-web-token  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.current_route import CurrentRoute
from swagger_client.models.default_response import DefaultResponse
from swagger_client.models.price_change_route import PriceChangeRoute
from swagger_client.models.price_history_route import PriceHistoryRoute
from swagger_client.models.public_current_response import PublicCurrentResponse
from swagger_client.models.public_current_response_data import PublicCurrentResponseData
from swagger_client.models.public_current_response_data_current import PublicCurrentResponseDataCurrent
from swagger_client.models.public_price_change_response import PublicPriceChangeResponse
from swagger_client.models.public_price_change_response_data import PublicPriceChangeResponseData
from swagger_client.models.public_price_change_response_data_price_change import PublicPriceChangeResponseDataPriceChange
from swagger_client.models.public_price_history_response import PublicPriceHistoryResponse
from swagger_client.models.public_price_history_response_data import PublicPriceHistoryResponseData
from swagger_client.models.public_price_history_response_data_history import PublicPriceHistoryResponseDataHistory
from swagger_client.models.public_price_history_response_data_price_history import PublicPriceHistoryResponseDataPriceHistory
from swagger_client.models.public_symbols_response import PublicSymbolsResponse
from swagger_client.models.public_symbols_response_data import PublicSymbolsResponseData
from swagger_client.models.public_symbols_response_data_symbols import PublicSymbolsResponseDataSymbols
from swagger_client.models.public_trend_response import PublicTrendResponse
from swagger_client.models.public_trend_response_data import PublicTrendResponseData
from swagger_client.models.public_trend_response_data_trend import PublicTrendResponseDataTrend
from swagger_client.models.symbols_route import SymbolsRoute
from swagger_client.models.trend_route import TrendRoute
