"""Module for random data generator API."""

# pylint: disable=R0903
# pylint: disable=R0913
# pylint: disable=R0914

import base64

from urllib.error import HTTPError, URLError
import urllib.parse
import urllib.request

import json

class RequestError(ValueError):
    """Exception for wrong request."""

class ApiError(ValueError):
    """Exception for API error."""

class RandomDataGenerator:
    """Class for random data generator API."""

    main_url = 'https://www.fourmilab.ch/cgi-bin/Hotbits.api'
    custom_url = None

    def __init__(self, custom_url=None):
        """
        Initialize the class.

        Details about web service:
        -- https://www.fourmilab.ch/hotbits/
        -- https://www.fourmilab.ch/hotbits/how3.html
        -- https://www.fourmilab.ch/hotbits/secure_generate.html

        Input:
        -- custom_url -- Custom URL of the API.
        """

        self.custom_url = custom_url

    def generate(self, length='128', apikey='Pseudorandom'):
        """
        Generate random data using the API.

        Input:
        -- length -- Number of bytes to be generated.
        -- apikey -- API key for radioactively-generated random data.

        Output:
        -- Data from HotBits server.
        """

        request = {
            'nbytes': length,
            'apikey': apikey,

            'fmt': 'json',
        }

        parameters = urllib.parse.urlencode({k: v for k, v in request.items() if v is not None})

        for base_url in self.custom_url, self.main_url:
            if base_url:
                try:
                    url = base_url + '?' + parameters
                    request = urllib.request.Request(url)

                    response = urllib.request.urlopen(url).read()
                    result = json.loads(response.decode('utf-8'))

                    break

                except (URLError, ValueError) as err:
                    error = err

        try:
            return result['data']

        except (NameError, KeyError):
            # pylint: disable=E1101
            # pylint: disable=R1720

            if isinstance(error, HTTPError):
                if error.code == 400:
                    raise RequestError(error.read().decode('utf-8').strip('\n'))
                else:
                    raise ApiError(str(error))

            elif isinstance(error, URLError):
                raise ApiError(str(error))

            elif isinstance(error, ValueError):
                raise RequestError(str(error))

            raise ValueError('Can\'t get result because of wrong request or API error')

            # pylint: enable=R1720
            # pylint: enable=E1101
