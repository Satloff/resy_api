#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = "Theo Satloff"
__email__ = "theo@satloff.com"

import simplejson as json
import inspect
import time
import sys
import requests
from six.moves.urllib import parse
from Requester import Requester


class Resy(object):

    def __init__(self, api_key=None):
        self.base_requester = Requester(api_key)

    def location(self, params=None, lat=None, long=None, radius=None):
        """Returns venues wthin a given radius"""
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('location/config', 3, params)

    def venues(self, params=None, location_id=None):
        """Returns venues from within a location_id"""
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venues', 2, params)

    def venue(self, params=None, location_id=None, url_slug=None):
        """returns a specific venue given location_id and url_slug (venue name)"""
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venue', 2, params)

    def calendar(self, params=None, id=None):
        """ returns the dates open for a specific venue"""
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venue/calendar', 2, params)

    def top(self, params=None, day=None, location_id=None, num_seats=None):
        """returns the top venues from a given day, location, and seat number"""
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venues/top', 2, params)

    # def reservation(self, params=None,  x=None, y=None, day=None, num_seats=None,
    #                 auth_token=None, time_slot=None, venue_id=None, location_id=None):
    #     if params is None:
    #         params = self._process_params(locals())
    #     return self.base_requester.GET('reservation/find', 2, params)

    def get(self, path, version, params):
        """returns json for a specific path, version, and paramater list"""
        return self.base_requester.GET(path, version, params)

    def set_key(self, api_key):
        """set the api_key"""
        self.base_requester.set_key(api_key)

    def _process_params(self, params={}):
        """read in the locals from a function, and return the processed params dictionary"""
        for key, value in params.copy().iteritems():
            if 'self' == key or None == value:
                del params[key]
        return params

# if __name__ == "__main__":
#     key = 'VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5'
#     resy = Resy(key)
#     resy.location()
