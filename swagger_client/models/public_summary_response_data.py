# coding: utf-8

"""
    CryptoWeather

    The CryptoWeather API allows for access to all of the cryptocurrency data and market forecast services provided. There are two primary categories of routes, `public` and `private`, where `public` routes are accessible to the general public and do not require API authentication, and `private` routes, which require API authentication.  ## General Overview  1. All API methods adhere to RESTful best practices as closely as possible. As such, all API calls will be made via the standard HTTP protocol using the GET/POST/PUT/DELETE request types.  2. Every request returns the status as a JSON response with the following:     - success, true if it was successful     - code, the http status code (also in the response header)         - 200 if response is successful         - 400 if bad request         - 401 if authorization JWT is wrong or limit exceeded         - 404 wrong route         - 500 for any internal errors     - status, the status of the request, default **success**     - errors, an array of any relevant error details  3. For any requests that are not successful an error message is specified and returned as an array for the **errors** key in the JSON response.  4. All authentication uses JSON Web Tokens (JWT), which is set as the **Authorization** entry in the header, see the following for more details.     - http://jwt.io     - https://scotch.io/tutorials/the-anatomy-of-a-json-web-token  ## Code Example  The following is a code example in Python, which demonstrates using the [Python Requests library](https://requests.readthedocs.io/en/master/) for both the `public` and `private` API routes.  ``` import requests  HOST = \"https://api.cryptoweather.ai/v1\"  # Your API key (JWT) API_KEY = \"<YOUR API KEY>\"  # Example public request, no API key required. requests.get(\"{}/public/symbols\".format(HOST)).json()  # Get the current btc price using the public route requests.get(\"{}/public/price-current/{}\".format(HOST, \"btc\")).json()   # Example private request, API key required. Get the btc hourly forecasts headers = {\"Authorization\": \"Bearer {}\".format(API_KEY)} requests.get(\"{}/private/forecast/{}/{}\".format(HOST, \"btc\", \"1h\"),              headers=headers).json() ```  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PublicSummaryResponseData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'icon': 'str',
        'name': 'str',
        'symbol_name': 'str',
        'slug': 'str',
        'added': 'float',
        'color': 'PublicSummaryResponseColor',
        'price_btc': 'float',
        'price_usd': 'float',
        'market_cap': 'float',
        'volume_usd': 'float',
        'change_pct': 'float',
        'market_data_time': 'float',
        'trend': 'list[PublicTrendResponseDataTrend]'
    }

    attribute_map = {
        'icon': 'icon',
        'name': 'name',
        'symbol_name': 'symbol_name',
        'slug': 'slug',
        'added': 'added',
        'color': 'color',
        'price_btc': 'price_btc',
        'price_usd': 'price_usd',
        'market_cap': 'market_cap',
        'volume_usd': 'volume_usd',
        'change_pct': 'change_pct',
        'market_data_time': 'market_data_time',
        'trend': 'trend'
    }

    def __init__(self, icon=None, name=None, symbol_name=None, slug=None, added=None, color=None, price_btc=None, price_usd=None, market_cap=None, volume_usd=None, change_pct=None, market_data_time=None, trend=None):  # noqa: E501
        """PublicSummaryResponseData - a model defined in Swagger"""  # noqa: E501

        self._icon = None
        self._name = None
        self._symbol_name = None
        self._slug = None
        self._added = None
        self._color = None
        self._price_btc = None
        self._price_usd = None
        self._market_cap = None
        self._volume_usd = None
        self._change_pct = None
        self._market_data_time = None
        self._trend = None
        self.discriminator = None

        self.icon = icon
        self.name = name
        self.symbol_name = symbol_name
        self.slug = slug
        self.added = added
        self.color = color
        self.price_btc = price_btc
        self.price_usd = price_usd
        self.market_cap = market_cap
        self.volume_usd = volume_usd
        self.change_pct = change_pct
        self.market_data_time = market_data_time
        self.trend = trend

    @property
    def icon(self):
        """Gets the icon of this PublicSummaryResponseData.  # noqa: E501


        :return: The icon of this PublicSummaryResponseData.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PublicSummaryResponseData.


        :param icon: The icon of this PublicSummaryResponseData.  # noqa: E501
        :type: str
        """
        if icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def name(self):
        """Gets the name of this PublicSummaryResponseData.  # noqa: E501


        :return: The name of this PublicSummaryResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicSummaryResponseData.


        :param name: The name of this PublicSummaryResponseData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def symbol_name(self):
        """Gets the symbol_name of this PublicSummaryResponseData.  # noqa: E501


        :return: The symbol_name of this PublicSummaryResponseData.  # noqa: E501
        :rtype: str
        """
        return self._symbol_name

    @symbol_name.setter
    def symbol_name(self, symbol_name):
        """Sets the symbol_name of this PublicSummaryResponseData.


        :param symbol_name: The symbol_name of this PublicSummaryResponseData.  # noqa: E501
        :type: str
        """
        if symbol_name is None:
            raise ValueError("Invalid value for `symbol_name`, must not be `None`")  # noqa: E501

        self._symbol_name = symbol_name

    @property
    def slug(self):
        """Gets the slug of this PublicSummaryResponseData.  # noqa: E501


        :return: The slug of this PublicSummaryResponseData.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this PublicSummaryResponseData.


        :param slug: The slug of this PublicSummaryResponseData.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    @property
    def added(self):
        """Gets the added of this PublicSummaryResponseData.  # noqa: E501


        :return: The added of this PublicSummaryResponseData.  # noqa: E501
        :rtype: float
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this PublicSummaryResponseData.


        :param added: The added of this PublicSummaryResponseData.  # noqa: E501
        :type: float
        """
        if added is None:
            raise ValueError("Invalid value for `added`, must not be `None`")  # noqa: E501

        self._added = added

    @property
    def color(self):
        """Gets the color of this PublicSummaryResponseData.  # noqa: E501


        :return: The color of this PublicSummaryResponseData.  # noqa: E501
        :rtype: PublicSummaryResponseColor
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this PublicSummaryResponseData.


        :param color: The color of this PublicSummaryResponseData.  # noqa: E501
        :type: PublicSummaryResponseColor
        """
        if color is None:
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def price_btc(self):
        """Gets the price_btc of this PublicSummaryResponseData.  # noqa: E501


        :return: The price_btc of this PublicSummaryResponseData.  # noqa: E501
        :rtype: float
        """
        return self._price_btc

    @price_btc.setter
    def price_btc(self, price_btc):
        """Sets the price_btc of this PublicSummaryResponseData.


        :param price_btc: The price_btc of this PublicSummaryResponseData.  # noqa: E501
        :type: float
        """
        if price_btc is None:
            raise ValueError("Invalid value for `price_btc`, must not be `None`")  # noqa: E501

        self._price_btc = price_btc

    @property
    def price_usd(self):
        """Gets the price_usd of this PublicSummaryResponseData.  # noqa: E501


        :return: The price_usd of this PublicSummaryResponseData.  # noqa: E501
        :rtype: float
        """
        return self._price_usd

    @price_usd.setter
    def price_usd(self, price_usd):
        """Sets the price_usd of this PublicSummaryResponseData.


        :param price_usd: The price_usd of this PublicSummaryResponseData.  # noqa: E501
        :type: float
        """
        if price_usd is None:
            raise ValueError("Invalid value for `price_usd`, must not be `None`")  # noqa: E501

        self._price_usd = price_usd

    @property
    def market_cap(self):
        """Gets the market_cap of this PublicSummaryResponseData.  # noqa: E501


        :return: The market_cap of this PublicSummaryResponseData.  # noqa: E501
        :rtype: float
        """
        return self._market_cap

    @market_cap.setter
    def market_cap(self, market_cap):
        """Sets the market_cap of this PublicSummaryResponseData.


        :param market_cap: The market_cap of this PublicSummaryResponseData.  # noqa: E501
        :type: float
        """
        if market_cap is None:
            raise ValueError("Invalid value for `market_cap`, must not be `None`")  # noqa: E501

        self._market_cap = market_cap

    @property
    def volume_usd(self):
        """Gets the volume_usd of this PublicSummaryResponseData.  # noqa: E501


        :return: The volume_usd of this PublicSummaryResponseData.  # noqa: E501
        :rtype: float
        """
        return self._volume_usd

    @volume_usd.setter
    def volume_usd(self, volume_usd):
        """Sets the volume_usd of this PublicSummaryResponseData.


        :param volume_usd: The volume_usd of this PublicSummaryResponseData.  # noqa: E501
        :type: float
        """
        if volume_usd is None:
            raise ValueError("Invalid value for `volume_usd`, must not be `None`")  # noqa: E501

        self._volume_usd = volume_usd

    @property
    def change_pct(self):
        """Gets the change_pct of this PublicSummaryResponseData.  # noqa: E501


        :return: The change_pct of this PublicSummaryResponseData.  # noqa: E501
        :rtype: float
        """
        return self._change_pct

    @change_pct.setter
    def change_pct(self, change_pct):
        """Sets the change_pct of this PublicSummaryResponseData.


        :param change_pct: The change_pct of this PublicSummaryResponseData.  # noqa: E501
        :type: float
        """
        if change_pct is None:
            raise ValueError("Invalid value for `change_pct`, must not be `None`")  # noqa: E501

        self._change_pct = change_pct

    @property
    def market_data_time(self):
        """Gets the market_data_time of this PublicSummaryResponseData.  # noqa: E501


        :return: The market_data_time of this PublicSummaryResponseData.  # noqa: E501
        :rtype: float
        """
        return self._market_data_time

    @market_data_time.setter
    def market_data_time(self, market_data_time):
        """Sets the market_data_time of this PublicSummaryResponseData.


        :param market_data_time: The market_data_time of this PublicSummaryResponseData.  # noqa: E501
        :type: float
        """
        if market_data_time is None:
            raise ValueError("Invalid value for `market_data_time`, must not be `None`")  # noqa: E501

        self._market_data_time = market_data_time

    @property
    def trend(self):
        """Gets the trend of this PublicSummaryResponseData.  # noqa: E501


        :return: The trend of this PublicSummaryResponseData.  # noqa: E501
        :rtype: list[PublicTrendResponseDataTrend]
        """
        return self._trend

    @trend.setter
    def trend(self, trend):
        """Sets the trend of this PublicSummaryResponseData.


        :param trend: The trend of this PublicSummaryResponseData.  # noqa: E501
        :type: list[PublicTrendResponseDataTrend]
        """
        if trend is None:
            raise ValueError("Invalid value for `trend`, must not be `None`")  # noqa: E501

        self._trend = trend

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PublicSummaryResponseData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicSummaryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
