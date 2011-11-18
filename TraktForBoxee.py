#!/usr/bin/env python

import logging
import ConfigParser
import boxeeboxclient as bbc
import sys

class TraktForBoxee(object):
    
    def __init__(self):
        logging.basicConfig(format="%(asctime)s::%(name)s::%(levelname)s::%(message)s",
                            level=logging.DEBUG,
                            stream=sys.stdout)
        
        self.log = logging.getLogger("TraktForBoxee")
        self.log.debug("Initialized Trakt for Boxee.")
        
        self.config = ConfigParser.RawConfigParser()
        self.config.read("settings.cfg")
        
        boxeeip = self.config.get("Boxee", "IP")
        boxeeport = self.config.getint("Boxee", "Port")
        
        self.client = bbc.BoxeeBoxClient("9001", boxeeip, boxeeport, "traktforboxee", "Trakt for Boxee")
        
        #t = self.client.callMethod("System.GetInfoLabels", {'labels': ['VideoPlayer.Title', 'VideoPlayer.TVShowTitle', 'VideoPlayer.Season', 'VideoPlayer.Time', 'VideoPlayer.Year']}, True);
        #t = self.client.callMethod("VideoPlayer.GetPercentage")
        #self.log.debug(t["result"])
        self.log.debug(self.client.getVideoPlayerPercentage())
        #print self.client.getActivePlayers()
        #self.client = bbc.BoxeeBoxClient("57", "192.168.1.148", 9090, "traktforboxee", "Trakt for Boxee")
        
if __name__ == '__main__':
    test = TraktForBoxee()