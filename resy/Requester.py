__author__ = "Theo Satloff"
__email__ = "theo@satloff.com"

import simplejson as json
import inspect
import time
import sys
import requests
from six.moves.urllib import parse
from settings import *

class Requester(object):
    """Api requesting object"""
    def __init__(self, api_key=None):
        """Sets up the api object"""
        self.set_key(api_key)

    def set_key(self, api_key):
        """Set the api_key token for this requester"""
        self.api_key = api_key

    def GET(self, path, version, params={}):
        """GET request that returns processed data"""
        params = params.copy()

        # Continue processing normal requests
        headers = self._create_headers()
        url = '{API_ENDPOINT}/{version}/{path}'.format(
            API_ENDPOINT=API_ENDPOINT,
            version=version,
            path=path,
        )

        print url
        result = self._get(url, headers=headers, params=params)

        return result['data']

    def _create_headers(self):
        """Get the headers we need"""
        headers = {}
        if self.api_key:
            headers['Authorization'] = 'ResyAPI api_key="{api_key}"'.format(
                api_key=self.api_key
            )
        return headers

    def _get(self, url, headers={}, params=None):
        """Tries to GET data from an endpoint using retries"""
        param_string = parse.urlencode(params)
        for i in xrange(NUM_REQUEST_RETRIES):
            try:
                try:
                    print param_string
                    response = requests.get(url, headers=headers, params=param_string, verify=VERIFY_SSL)
                    return self._process_response(response)
                except requests.exceptions.RequestException as e:
                    self._log_and_raise_exception('Error connecting with Resy API', e)
            except ResyException as e:
                # Some errors don't bear repeating
                if e.__class__ in [Unauthorized, NotFound, InvalidFormat]: raise
                # If we've reached our last try, re-raise
                if ((i + 1) == NUM_REQUEST_RETRIES): raise
            time.sleep(1)

    def _process_response(self, response):
        """Make the request and handle exception processing"""
        # Read the response as JSON
        try:
            data = response.json()
        except ValueError:
            self._raise_error_from_response(response.text)

        # Default case, Got proper response
        if response.status_code == 200:
            return { 'headers': response.headers, 'data': data }
        return self._raise_error_from_response(data)

    def _raise_error_from_response(self, data):
        """Processes the response data"""
        # Check the meta-data for why this request failed
        if data and type(data) == dict:
            # Account for Resy conflicts
            # see: github.com/resy/developers for error responses
            if data.get('status') in (200, 400): return data
            exc = error_types.get(data.get('message'))
            if exc:
                raise exc(data.get('status'))
            else:
                self._log_and_raise_exception('Unknown error. status', data)
        else:
            exc = error_types.get('Invalid Format')
            raise exc(data)

    def _log_and_raise_exception(self, msg, data, cls=ResyException):
        """Calls log.error() then raises an exception of class cls"""
        data = u'{0}'.format(data)
        # We put data as a argument for log.error() so error tracking systems such
        # as Sentry will properly group errors together by msg only
        raise cls(u'{0}: {1}'.format(msg, data))
