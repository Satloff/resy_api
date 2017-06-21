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

    def location(self, params=None, lat=None, long=None):
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('location/config', 3, params)

    def venues(self, params=None, location_id=None):
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venues', 2, params)

    def venue(self, params=None, location_id=None, url_slug=None):
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venue', 2, params)

    def calendar(self, params=None, id=None):
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venue/calendar', 2, params)

    def top(self, params=None, day=None, location_id=None, num_seats=None):
        if params is None:
            params = self._process_params(locals())
        return self.base_requester.GET('venues/top', 2, params)

    # def reservation(self, params=None,  x=None, y=None, day=None, num_seats=None,
    #                 auth_token=None, time_slot=None, venue_id=None, location_id=None):
    #     if params is None:
    #         params = self._process_params(locals())
    #     return self.base_requester.GET('reservation/find', 2, params)

    def get(self, path, version, params):
        return self.base_requester.GET(path, version, params)

    def set_key(self, api_key):
        self.base_requester.set_key(api_key)

    def _process_params(self, params={}):
        for key, value in params.copy().iteritems():
            if 'self' == key or None == value:
                del params[key]
        return params

if __name__ == "__main__":
    key = 'VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5'
    resy = Resy(key)
    #resy.
    #print resy.reservation(x=40.7643304, y=-73.9772046, day='2017-06-21', num_seats=2)
    #print resy.reservation({'x':'40.7643304', 'y': '-73.9772046', 'day': '2017-06-21', 'num_seats':2})
    #print resy.location({'lat':40.7643304, 'long': -73.9772046, 'radius': 1})
    #print resy.venue(location_id=1, url_slug='estela')
    #print resy.calendar(id=6)

    #https://api.resy.com/2/venue?location_id=1&url_slug=estela
    #print resy.top({'day': '2017-06-21', 'location_id': 'li', 'num_seats': 2})

    # https://api.resy.com/3/google/static_maps/url/sign?url=https:%2F%2Fmaps.googleapis.com%2Fmaps%2Fapi%2Fstaticmap%3Fsize%3D385x385%26zoom%3D17%26markers%3Dcolor:0xE5382E%257C40.724664,-73.994748%26key%3DAIzaSyBC2hN321Moz9bhWU0CvdPg6rvKSN_SVgM


#calendar?id=6
#url_slug=estela


#location/config?lat=40.7643304&long=-73.9772046

#/venues
#/top?day=2017-06-21&location_id=li&num_seats=2
