# coding: utf-8

"""
    Investabit API

    The Investabit API allows for access to all of the public facing services provided, including market data and forecasts.  ## General Overview  1. All API methods will be built to adhere to RESTful best practices as closely as possible. As such, all API calls will be made via the standard HTTP protocol using the GET/POST/PUT/DELETE request types.  2. Every request returns the status as a JSON response with the following   - success, true if it was successful   - code, the http status code (also in the response header)          200 if response is successful          400 if bad request          401 if authorization JWT is wrong or limit exceeded          404 wrong route          500 for any internal errors  - status, the status of the request, default **success**  - errors, an array of any relevant error details  3. For any requests that are not successful an error message is specified and returned as an array for the **errors** key in the JSON response.  4. All authentication uses JSON Web Tokens (JWT), which is set as the **Authorization** entry in the header, see the following for more details.     * http://jwt.io     * https://scotch.io/tutorials/the-anatomy-of-a-json-web-token  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.public_price_response_data import PublicPriceResponseData  # noqa: F401,E501


class PublicPriceResponse(object):
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
        'success': 'bool',
        'code': 'int',
        'status': 'str',
        'data': 'PublicPriceResponseData',
        'errors': 'list[object]'
    }

    attribute_map = {
        'success': 'success',
        'code': 'code',
        'status': 'status',
        'data': 'data',
        'errors': 'errors'
    }

    def __init__(self, success=None, code=None, status=None, data=None, errors=None):  # noqa: E501
        """PublicPriceResponse - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._code = None
        self._status = None
        self._data = None
        self._errors = None
        self.discriminator = None

        self.success = success
        self.code = code
        self.status = status
        self.data = data
        if errors is not None:
            self.errors = errors

    @property
    def success(self):
        """Gets the success of this PublicPriceResponse.  # noqa: E501


        :return: The success of this PublicPriceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PublicPriceResponse.


        :param success: The success of this PublicPriceResponse.  # noqa: E501
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def code(self):
        """Gets the code of this PublicPriceResponse.  # noqa: E501


        :return: The code of this PublicPriceResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PublicPriceResponse.


        :param code: The code of this PublicPriceResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def status(self):
        """Gets the status of this PublicPriceResponse.  # noqa: E501


        :return: The status of this PublicPriceResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicPriceResponse.


        :param status: The status of this PublicPriceResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def data(self):
        """Gets the data of this PublicPriceResponse.  # noqa: E501


        :return: The data of this PublicPriceResponse.  # noqa: E501
        :rtype: PublicPriceResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PublicPriceResponse.


        :param data: The data of this PublicPriceResponse.  # noqa: E501
        :type: PublicPriceResponseData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def errors(self):
        """Gets the errors of this PublicPriceResponse.  # noqa: E501


        :return: The errors of this PublicPriceResponse.  # noqa: E501
        :rtype: list[object]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this PublicPriceResponse.


        :param errors: The errors of this PublicPriceResponse.  # noqa: E501
        :type: list[object]
        """

        self._errors = errors

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
        if issubclass(PublicPriceResponse, dict):
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
        if not isinstance(other, PublicPriceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
