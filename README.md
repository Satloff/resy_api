# Python Wrapper for Resy API

Python wrapper for the Resy API ([resy.com](https://resy.com/)).

Features:
* Automatic retries
* partial endpoint coverage (only endpoints that I could find)
* Useful exception classes

Dependencies:

* requests
* simplejson
* urllib


### Install
from within the local clone of git directory:
    #install the local package
    pip install .

## Usage



### Import

    # Creating Resy object with key
    r = Resy('API KEY')

### Authentication

Load the key as part of the object creation
    # Creating Resy object with key
    r = Resy('API KEY')

Or, create object and add the key separately
    # Object creating with separate key add
    r = Resy()
    r.set_key('API KEY')


### Examples

#### endpoints

###### location
    r = Resy('API KEY')
    # use native pythonic calls
    r.location(lat=40.7643304, long=-73.9772046, radius=1)

    # or pass parameters as a dictionary
    r.location({'lat':40.7643304, 'long': -73.9772046, 'radius': 1})

###### venues
    r = Resy('API KEY')
    # use native pythonic calls
    r.venues(location_id=1)

    # or pass parameters as a dictionary
    r.location({'location_id': 1})

###### venue
    r = Resy('API KEY')
    # use native pythonic calls
    r.venue(location_id=1, url_slug='estela')

    # or pass parameters as a dictionary
    r.location({'location_id': 1, 'url_slug': 'estela'})

###### calendar
    r = Resy('API KEY')
    # use native pythonic calls
    r.calendar(id=6)

    # or pass parameters as a dictionary
    r.location({'id': 6})

###### top
    r = Resy('API KEY')
    # use native pythonic calls
    r.top(day='2017-06-21', location_id='li', num_seats=2)

    # or pass parameters as a dictionary
    r.top({'day': '2017-06-21', 'location_id': 'li', 'num_seats': 2})

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

### Credits
* thanks to mLewisLogic for the basic api structure [foursquare](https://github.com/mLewisLogic/foursquare)
