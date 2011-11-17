#!/usr/bin/env python

import simplejson as json
import urllib
import logging

from hashlib import sha1

class TraktClient(object):
    def __init__(self, apikey, username, password):
        self.username = username
        self.password = sha1(password).hexdigest()
        self.apikey = apikey
    
    def call_method(self, method, data = {}, post=True):
        method = method.replace("%API%", self.apikey)
        
        if (post):
            data["username"] = self.username
            data["password"] = self.password
            
            encoded_data = json.dumps(data);
            
            logging.debug(encoded_data)

            stream = urllib.urlopen("http://api.trakt.tv/" + method,
                                    encoded_data)
            print stream.read()
        else:
            pass #Build url with data embedded.
