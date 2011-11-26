#!/usr/bin/env python

import logging
import ConfigParser
import boxeeboxclient
import TraktClient
import sys
import time
import re
import os
import getopt

VERSION = "1.0"
BOXEE_VERSION = BOXEE_DATE = ""
TIMER_INTERVAL = 10

class TraktForBoxee(object):

    def __init__(self):
        logging.basicConfig(format="%(asctime)s::%(name)s::%(levelname)s::%(message)s",
                            level=logging.DEBUG,
                            stream=sys.stdout)

        self.log = logging.getLogger("TraktForBoxee")
        self.log.info("Initialized Trakt for Boxee.")

        self.config = ConfigParser.RawConfigParser()
        self.config.read(sys.path[0] + "/settings.cfg")

        boxee_ip = self.config.get("Boxee", "IP")
        boxee_port = self.config.getint("Boxee", "Port")

        self.boxee_client = boxeeboxclient.BoxeeBoxClient("9001",
                                                          boxee_ip,
                                                          boxee_port,
                                                          "traktforboxee",
                                                          "Trakt for Boxee")

        trakt_api = "f46fbebb833fbeb8196b69e0e8d5de8f852b7ea6"
        trakt_username = self.config.get("Trakt", "Username")
        trakt_password = self.config.get("Trakt", "Password")

        self.trakt_client = TraktClient.TraktClient(trakt_api,
                                                    trakt_username,
                                                    trakt_password)

        build_info = self.boxee_client.getInfoLabels(["System.BuildVersion",
                                                      "System.BuildDate"])
        BOXEE_VERSION = build_info["System.BuildVersion"]
        BOXEE_DATE = build_info["System.BuildDate"]

        self.SCROBBLE_TV = self.config.getboolean("TraktForBoxee", "ScrobbleTV")
        self.SCROBBLE_MOVIE = self.config.getboolean("TraktForBoxee", "ScrobbleMovie")
        self.NOTIFY_BOXEE = self.config.getboolean("TraktForBoxee", "NotifyBoxee")

        self.scrobbled = False
        self.watching_now = ""
<<<<<<< HEAD
=======
        self.timer = 0
>>>>>>> parent of 7ea9e6a... Revert 3b0770fc9f4ce865bb78c8ddc7b33046c11d6660^..HEAD

    def run(self):
        while (True):
<<<<<<< HEAD
            timer += TIMER_INTERVAL
            status = self.boxee_client.getCurrentlyPlaying()

            tv = status["type"] == "tv"

            if (status["type"] == "none"):
                self.log.debug("Boxee not playing anything, sleep.")
                if (self.watching_now != ""):
                    self.log.info("We were just watching something, canceling our watching status on Trakt.tv")
                    self.trakt_client.cancelWatching()
                    self.watching_now = ""
            else:
                boxee_idle = self.boxee_client.getIdle(300)

                if (boxee_idle):
                    if (self.watching_now != ""):
                        self.log.info("Boxee is idle, cancelling watching status.")
                        self.watching_now = ""
                        self.trakt_client.cancelWatching()
                else:
                    watching_now = (status["title"] + status["year"] +
                                    status["episode"] + status["season"] +
                                    status["episode_title"] + str(status["duration"]))
                    if (self.watching_now != watching_now):
                        self.watching_now = watching_now
                        self.scrobbled = False
                        self.log.debug("Now watching something else, canceling previous watching status.")
                        self.trakt_client.cancelWatching()
                        timer = 900 #Set watching first round through please

                    if ((tv and not self.SCROBBLE_TV) or
                        (not tv and not self.SCROBBLE_MOVIE)):
                        self.log.info("Set to ignore this media type, doing so.")
                    else:
                        if (status["percentage"] >= 90
                            and not self.scrobbled):
                                self.log.info("Scrobbling to Trakt")
                                if (self.NOTIFY_BOXEE):
                                    self.boxee_client.showNotification("Scrobbling to Trakt!")

                                try:
                                    self.trakt_client.update_media_status(status["title"],
                                                                          status["year"],
                                                                          status["duration"],
                                                                          status["percentage"],
                                                                          VERSION,
                                                                          BOXEE_VERSION,
                                                                          BOXEE_DATE,
                                                                          tv=tv,
                                                                          scrobble=True,
                                                                          season=status["season"],
                                                                          episode=status["episode"])
                                    self.scrobbled = True
                                except TraktClient.TraktError, (e):
                                    self.log.error("An error occurred while trying to scrobble: " + e.msg)

                        elif (status["percentage"] < 90
                              and not self.scrobbled
                              and timer >= 900):
                            self.log.info("Watching on Trakt")
                            timer = 0

                            try:
                                self.trakt_client.update_media_status(status["title"],
                                                                      status["year"],
                                                                      status["duration"],
                                                                      status["percentage"],
                                                                      VERSION,
                                                                      BOXEE_VERSION,
                                                                      BOXEE_DATE,
                                                                      tv=tv,
                                                                      season=status["season"],
                                                                      episode=status["episode"])

                                if (self.NOTIFY_BOXEE):
                                    self.boxee_client.showNotification("Watching on Trakt!")
                            except TraktClient.TraktError, (e):
                                timer = 870
                                self.log.error("An error occurred while trying to mark watching: " + e.msg)

            self.log.debug("NOT SCROBBLING... " + str(timer))
            time.sleep(TIMER_INTERVAL)
=======
            self.timer += TIMER_INTERVAL
            self.main()
            time.sleep(TIMER_INTERVAL)
    
    def main(self):
        status = self.boxee_client.getCurrentlyPlaying()
        boxee_idle = self.boxee_client.getIdle(300)
        tv = (status["type"] == "tv")
        
        if (status["type"] == "none"):
            self.log.debug("Boxee not playing anything, sleep.")
            self.clearWatching()
            return
        
        if (boxee_idle):
            self.clearWatching("Boxee is idle")
            return
        
        watching_now = (status["title"] + status["year"] +
                        status["episode"] + status["season"] +
                        status["episode_title"] + str(status["duration"]))
        
        if (self.watching_now != watching_now):
            self.clearWatching()
            self.watching_now = watching_now
            self.scrobbled = False
            self.log.info("Boxee watching something.")
            self.timer = 900 #Set watching first round through please
        
        if ((tv and not self.SCROBBLE_TV) or
            (not tv and not self.SCROBBLE_MOVIE)):
            self.log.info("Watching something but set to ignore media type, " +
                          "not scrobbling.")
            return
        
        if (status["percentage"] >= 90
            and not self.scrobbled):
                self.log.info("Scrobbling to Trakt")
                if (self.NOTIFY_BOXEE):
                    self.boxee_client.showNotification("Scrobbling to Trakt!")
                
                try:
                    self.trakt_client.update_media_status(status["title"],
                                                          status["year"],
                                                          status["duration"],
                                                          status["percentage"],
                                                          VERSION,
                                                          BOXEE_VERSION,
                                                          BOXEE_DATE,
                                                          tv=tv,
                                                          scrobble=True,
                                                          season=status["season"],
                                                          episode=status["episode"])
                    self.scrobbled = True
                except TraktClient.TraktError, (e):
                    self.log.error("An error occurred while trying to scrobble: " + e.msg)
                
        elif (status["percentage"] < 90
              and not self.scrobbled
              and self.timer >= 900):
            self.log.info("Watching on Trakt")
            self.timer = 0
        
            try:
                self.trakt_client.update_media_status(status["title"],
                                                      status["year"],
                                                      status["duration"],
                                                      status["percentage"],
                                                      VERSION,
                                                      BOXEE_VERSION,
                                                      BOXEE_DATE,
                                                      tv=tv,
                                                      season=status["season"],
                                                      episode=status["episode"])
                
                if (self.NOTIFY_BOXEE):
                    self.boxee_client.showNotification("Watching on Trakt!")
            except TraktClient.TraktError, (e):
                self.timer = 870
                self.log.error("An error occurred while trying to mark watching: " + e.msg)
            
        self.log.debug("Timer: " + str(self.timer))
        
    def clearWatching(self, msg=""):
        if (self.watching_now == ""):
            return
        if (msg != ""):
            self.log.info(msg)
        self.log.info("Clearing Trakt watching status.")
        self.trakt_client.cancelWatching()
        self.watching_now = ""

def daemonize():

    # Make a non-session-leader child process
        try:
            pid = os.fork() #@UndefinedVariable - only available in UNIX
            if pid != 0:
                sys.exit(0)
        except OSError, e:
            raise RuntimeError("1st fork failed: %s [%d]" %
                       (e.strerror, e.errno))

        os.setsid() #@UndefinedVariable - only available in UNIX

        # Make sure I can read my own files and shut out others
        prev = os.umask(0)
        os.umask(prev and int('077', 8))

        # Make the child a session-leader by detaching from the terminal
        try:
            pid = os.fork() #@UndefinedVariable - only available in UNIX
            if pid != 0:
                sys.exit(0)
        except OSError, e:
            raise RuntimeError("2st fork failed: %s [%d]" %
                       (e.strerror, e.errno))

        dev_null = file('/dev/null', 'r')
        os.dup2(dev_null.fileno(), sys.stdin.fileno())
>>>>>>> parent of 7ea9e6a... Revert 3b0770fc9f4ce865bb78c8ddc7b33046c11d6660^..HEAD

def daemonize():

    # Make a non-session-leader child process
        try:
            pid = os.fork() #@UndefinedVariable - only available in UNIX
            if pid != 0:
                sys.exit(0)
        except OSError, e:
            raise RuntimeError("1st fork failed: %s [%d]" %
                       (e.strerror, e.errno))

        os.setsid() #@UndefinedVariable - only available in UNIX

        # Make sure I can read my own files and shut out others
        prev = os.umask(0)
        os.umask(prev and int('077', 8))

        # Make the child a session-leader by detaching from the terminal
        try:
            pid = os.fork() #@UndefinedVariable - only available in UNIX
            if pid != 0:
                sys.exit(0)
        except OSError, e:
            raise RuntimeError("2st fork failed: %s [%d]" %
                       (e.strerror, e.errno))

        dev_null = file('/dev/null', 'r')
        os.dup2(dev_null.fileno(), sys.stdin.fileno())

def pair():
    config = ConfigParser.RawConfigParser()
    config.read(sys.path[0] + "/settings.cfg")

    ip = config.get("Boxee", "IP")
    port = config.get("Boxee", "Port")

    client = boxeeboxclient.BoxeeBoxClient("9001", ip, int(port), "traktforboxee",
                                           "Trakt for Boxee")
    client.callMethod("Device.PairChallenge", {'deviceid': "9001",
                                               'applicationid': client.application_id,
                                               'label': client.application_label,
                                               'icon': "http://dir.boxee.tv/apps/workbench/images/thumb.png",
                                               'type': 'other'})

    pattern = re.compile("^[0-9]{4}$")

    code = False
    while (not code or pattern.match(code) is None):
        code = raw_input("Enter the code displyed on the screen of your Boxee Box: ")

    client.callMethod("Device.PairResponse", {'deviceid': "9001", 'code': code})
    print "You are now ready to scrobble to Trakt.tv."

if __name__ == '__main__':
<<<<<<< HEAD
    Pair = False
    Daemon = False
=======
    should_pair = should_daemon = False
>>>>>>> parent of 7ea9e6a... Revert 3b0770fc9f4ce865bb78c8ddc7b33046c11d6660^..HEAD

    try:
        opts, args = getopt.getopt(sys.argv[1:], "dp", ['daemon', 'pair']) #@UnusedVariable
    except getopt.GetoptError:
        print "Available options: --daemon, --pair"
        sys.exit()

    for o, a in opts:
        # Pair to the Boxee box
        if o in ('-p', '--pair'):
<<<<<<< HEAD
            Pair = True
=======
            should_pair = True
>>>>>>> parent of 7ea9e6a... Revert 3b0770fc9f4ce865bb78c8ddc7b33046c11d6660^..HEAD

        # Run as a daemon
        if o in ('-d', '--daemon'):
            if sys.platform == 'win32':
                print "Daemonize not supported under Windows, starting normally"
            else:
<<<<<<< HEAD
                consoleLogging = False
                Daemon = True

    if Pair:
        pair()

    if Daemon:
=======
                should_daemon = True

    if should_pair:
        pair()

    if should_daemon:
>>>>>>> parent of 7ea9e6a... Revert 3b0770fc9f4ce865bb78c8ddc7b33046c11d6660^..HEAD
        daemonize()

    client = TraktForBoxee()
    client.run()
