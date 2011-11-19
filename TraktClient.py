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
            return json.loads(stream.read())
        else:
            pass #Decisions...

    def scrobbleShow(self, title, year, season, episode, duration, progress,
                     plugin_ver, media_center_ver, media_center_date):
        data = {'title': title,
                'year': year,
                'season': season,
                'episode': episode,
                'duration': duration,
                'progress': progress,
                'plugin_version': plugin_ver,
                'media_center_version': media_center_ver,
                'media_center_date': media_center_date}
        
        self.call_method("show/scrobble/%API%", data)
        
    def watchingShow(self, title, year, season, episode, duration, progress,
                     plugin_ver, media_center_ver, media_center_date):
        data = {'title': title,
                'year': year,
                'season': season,
                'episode': episode,
                'duration': duration,
                'progress': progress,
                'plugin_version': plugin_ver,
                'media_center_version': media_center_ver,
                'media_center_date': media_center_date}
        
        self.call_method("show/watching/%API%", data)
        
    def scrobbleMovie(self, title, year, duration, progress, plugin_ver,
                      media_center_ver, media_center_date):
        data = {'title': title,
                'year': year,
                'duration': duration,
                'progress': progress,
                'plugin_version': plugin_ver,
                'media_center_version': media_center_ver,
                'media_center_date': media_center_date}
        
        self.call_method("movie/scrobble/%API%", data)
        
    def watchingMovie(self, title, year, duration, progress, plugin_ver,
                      media_center_ver, media_center_date):
        data = {'title': title,
                'year': year,
                'duration': duration,
                'progress': progress,
                'plugin_version': plugin_ver,
                'media_center_version': media_center_ver,
                'media_center_date': media_center_date}
        
        self.call_method("movie/watching/%API%", data)
    
    def cancelWatching(self):
        self.call_method("show/cancelwatching/%API%")
        self.call_method("movie/cancelwatching/%API%")