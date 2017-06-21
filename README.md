# foursquare

Python wrapper for the Resy API ([resy.com](resy.com)).

Features:
* Automatic retries
* partial endpoint coverage (only endpoints that I could find)
* Useful exception classes

Dependencies:

* requests
* simplejson
* urllib


## Usage

### Authentication

Load the key as part of the object creation
    # Creating Resy object with key
    resy = Resy('API KEY')

Or, create object and add the key separately
    # Object creating with separate key add
    resy = Resy()
    resy.set_key('API KEY')


### Examples

#### endpoints

###### location
    resy = Resy('API KEY')
    # use native pythonic calls
    resy.location(lat=40.7643304, long=-73.9772046, radius=1)

    # or pass parameters as a dictionary
    resy.location({'lat':40.7643304, 'long': -73.9772046, 'radius': 1})

###### venues
    resy = Resy('API KEY')
    # use native pythonic calls
    resy.venues(location_id=1)

    # or pass parameters as a dictionary
    resy.location({'location_id': 1})

###### venue
    resy = Resy('API KEY')
    # use native pythonic calls
    resy.venue(location_id=1, url_slug='estela')

    # or pass parameters as a dictionary
    resy.location({'location_id': 1, 'url_slug': 'estela'})

###### calendar
    resy = Resy('API KEY')
    # use native pythonic calls
    resy.calendar(id=6)

    # or pass parameters as a dictionary
    resy.location({'id': 6})

###### top
    resy = Resy('API KEY')
    # use native pythonic calls
    resy.top(day='2017-06-21', location_id='li', num_seats=2)

    # or pass parameters as a dictionary
    resy.top({'day': '2017-06-21', 'location_id': 'li', 'num_seats': 2})

### Partial endpoint list
Note: (if you know more, please let me know.)

    location()
    venues()
    venue()
    calendar()
    top()

### TODO
* restructure endpoints to be one-to-one with Resy
* write tests
* find more endpoints
