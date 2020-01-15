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


class PublicPriceCurrentResponseDataCurrent(object):
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
        'symbol': 'str',
        'name': 'str',
        'price': 'float',
        'change_usd': 'float',
        'change_pct': 'float'
    }

    attribute_map = {
        'symbol': 'symbol',
        'name': 'name',
        'price': 'price',
        'change_usd': 'change_usd',
        'change_pct': 'change_pct'
    }

    def __init__(self, symbol=None, name=None, price=None, change_usd=None, change_pct=None):  # noqa: E501
        """PublicPriceCurrentResponseDataCurrent - a model defined in Swagger"""  # noqa: E501

        self._symbol = None
        self._name = None
        self._price = None
        self._change_usd = None
        self._change_pct = None
        self.discriminator = None

        self.symbol = symbol
        self.name = name
        self.price = price
        self.change_usd = change_usd
        self.change_pct = change_pct

    @property
    def symbol(self):
        """Gets the symbol of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501


        :return: The symbol of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this PublicPriceCurrentResponseDataCurrent.


        :param symbol: The symbol of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def name(self):
        """Gets the name of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501


        :return: The name of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicPriceCurrentResponseDataCurrent.


        :param name: The name of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501


        :return: The price of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PublicPriceCurrentResponseDataCurrent.


        :param price: The price of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def change_usd(self):
        """Gets the change_usd of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501


        :return: The change_usd of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :rtype: float
        """
        return self._change_usd

    @change_usd.setter
    def change_usd(self, change_usd):
        """Sets the change_usd of this PublicPriceCurrentResponseDataCurrent.


        :param change_usd: The change_usd of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :type: float
        """
        if change_usd is None:
            raise ValueError("Invalid value for `change_usd`, must not be `None`")  # noqa: E501

        self._change_usd = change_usd

    @property
    def change_pct(self):
        """Gets the change_pct of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501


        :return: The change_pct of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :rtype: float
        """
        return self._change_pct

    @change_pct.setter
    def change_pct(self, change_pct):
        """Sets the change_pct of this PublicPriceCurrentResponseDataCurrent.


        :param change_pct: The change_pct of this PublicPriceCurrentResponseDataCurrent.  # noqa: E501
        :type: float
        """
        if change_pct is None:
            raise ValueError("Invalid value for `change_pct`, must not be `None`")  # noqa: E501

        self._change_pct = change_pct

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
        if issubclass(PublicPriceCurrentResponseDataCurrent, dict):
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
        if not isinstance(other, PublicPriceCurrentResponseDataCurrent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
