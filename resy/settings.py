
# --------- Global Config ---------
# Number of times to retry http requests
NUM_REQUEST_RETRIES = 3

API_ENDPOINT = 'https://api.resy.com'

# Change this if your Python distribution has issues with Resy's SSL cert
VERIFY_SSL = True



#--------- Error Logging ---------
# Generic Resy exception
class ResyException(Exception): pass

# Specific exceptions
class Unauthorized(ResyException): pass
class NotFound(ResyException): pass
class InvalidFormat(ResyException): pass
class PaymentRequired(ResyException): pass
class Conflict(ResyException): pass

error_types = {
    'Unauthorized': Unauthorized,
    'Not Found': NotFound,
    'Invalid Format': InvalidFormat,
    'Payment Required': PaymentRequired,
    'Conflict': Conflict,
}
