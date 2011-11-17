#!/usr/bin/env python

import simplejson as json
import urllib
import sha

class TraktClient(object):
    def __init__(self, apikey, username, password):
        password_hash = sha.new(password).hexdigest()
        pass
    
    def callMethod(self, method)
        pass