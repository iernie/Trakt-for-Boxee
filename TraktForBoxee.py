#!/usr/bin/env python

import logging
import ConfigParser
import boxeeboxclient
import TraktClient
import sys
import time

VERSION = "1.0"
BOXEE_VERSION = BOXEE_DATE = ""

class TraktForBoxee(object):
    
    def __init__(self):
        logging.basicConfig(format="%(asctime)s::%(name)s::%(levelname)s::%(message)s",
                            level=logging.DEBUG,
                            stream=sys.stdout)
        
        self.log = logging.getLogger("TraktForBoxee")
        self.log.debug("Initialized Trakt for Boxee.")
        
        self.config = ConfigParser.RawConfigParser()
        self.config.read("settings.cfg")
        
        boxee_ip = self.config.get("Boxee", "IP")
        boxee_port = self.config.getint("Boxee", "Port")
        
        self.boxee_client = boxeeboxclient.BoxeeBoxClient("9001",
                                                          boxee_ip,
                                                          boxee_port,
                                                          "traktforboxee",
                                                          "Trakt for Boxee")
        
        trakt_api = self.config.get("Trakt", "APIKey")
        trakt_username = self.config.get("Trakt", "Username")
        trakt_password = self.config.get("Trakt", "Password")
        
        self.trakt_client = TraktClient.TraktClient(trakt_api,
                                                    trakt_username,
                                                    trakt_password)
        
        build_info = self.boxee_client.getInfoLabels(["System.BuildVersion",
                                                      "System.BuildDate"])
        BOXEE_VERSION = build_info["System.BuildVersion"]
        BOXEE_DATE = build_info["System.BuildDate"]
        
        self.log.debug(self.boxee_client.getCurrentlyPlaying())
        
        #t = self.client.callMethod("System.GetInfoLabels", {'labels': ['VideoPlayer.Title', 'VideoPlayer.TVShowTitle', 'VideoPlayer.Season', 'VideoPlayer.Time', 'VideoPlayer.Year']}, True);
        #t = self.client.callMethod("VideoPlayer.GetPercentage")
        #self.log.debug(t["result"])
        #self.log.debug(int(self.boxee_client.getVideoPlayerPercentage()))
        #print self.client.getActivePlayers()
        #self.client = bbc.BoxeeBoxClient("57", "192.168.1.148", 9090, "traktforboxee", "Trakt for Boxee")
    
    def run(self):
        while (true):
            pass
        
if __name__ == '__main__':
    test = TraktForBoxee()