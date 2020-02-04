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


class PublicSummaryResponseColor(object):
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
        'b': 'float',
        'g': 'float',
        'r': 'float'
    }

    attribute_map = {
        'b': 'b',
        'g': 'g',
        'r': 'r'
    }

    def __init__(self, b=None, g=None, r=None):  # noqa: E501
        """PublicSummaryResponseColor - a model defined in Swagger"""  # noqa: E501

        self._b = None
        self._g = None
        self._r = None
        self.discriminator = None

        self.b = b
        self.g = g
        self.r = r

    @property
    def b(self):
        """Gets the b of this PublicSummaryResponseColor.  # noqa: E501


        :return: The b of this PublicSummaryResponseColor.  # noqa: E501
        :rtype: float
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this PublicSummaryResponseColor.


        :param b: The b of this PublicSummaryResponseColor.  # noqa: E501
        :type: float
        """
        if b is None:
            raise ValueError("Invalid value for `b`, must not be `None`")  # noqa: E501

        self._b = b

    @property
    def g(self):
        """Gets the g of this PublicSummaryResponseColor.  # noqa: E501


        :return: The g of this PublicSummaryResponseColor.  # noqa: E501
        :rtype: float
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this PublicSummaryResponseColor.


        :param g: The g of this PublicSummaryResponseColor.  # noqa: E501
        :type: float
        """
        if g is None:
            raise ValueError("Invalid value for `g`, must not be `None`")  # noqa: E501

        self._g = g

    @property
    def r(self):
        """Gets the r of this PublicSummaryResponseColor.  # noqa: E501


        :return: The r of this PublicSummaryResponseColor.  # noqa: E501
        :rtype: float
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this PublicSummaryResponseColor.


        :param r: The r of this PublicSummaryResponseColor.  # noqa: E501
        :type: float
        """
        if r is None:
            raise ValueError("Invalid value for `r`, must not be `None`")  # noqa: E501

        self._r = r

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
        if issubclass(PublicSummaryResponseColor, dict):
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
        if not isinstance(other, PublicSummaryResponseColor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
