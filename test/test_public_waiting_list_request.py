# coding: utf-8

"""
    Investabit

    The Investabit API allows for access to all of the public facing services provided, including market data and forecasts.  ## General Overview  1. All API methods will be built to adhere to RESTful best practices as closely as possible. As such, all API calls will be made via the standard HTTP protocol using the GET/POST/PUT/DELETE request types.  2. Every request returns the status as a JSON response with the following   - success, true if it was successful   - code, the http status code (also in the response header)          200 if response is successful          400 if bad request          401 if authorization JWT is wrong or limit exceeded          404 wrong route          500 for any internal errors  - status, the status of the request, default **success**  - errors, an array of any relevant error details  3. For any requests that are not successful an error message is specified and returned as an array for the **errors** key in the JSON response.  4. All authentication uses JSON Web Tokens (JWT), which is set as the **Authorization** entry in the header, see the following for more details.     * http://jwt.io     * https://scotch.io/tutorials/the-anatomy-of-a-json-web-token  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.public_waiting_list_request import PublicWaitingListRequest  # noqa: E501
from swagger_client.rest import ApiException


class TestPublicWaitingListRequest(unittest.TestCase):
    """PublicWaitingListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPublicWaitingListRequest(self):
        """Test PublicWaitingListRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.public_waiting_list_request.PublicWaitingListRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
