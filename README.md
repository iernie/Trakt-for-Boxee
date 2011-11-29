Trakt For Boxee
===============

Trakt For Boxee is a simple script that will scrobble whatever you're watching
on your Boxee Box to Trakt.

Installation
------------
Getting setup with Trakt For Boxee is fairly straight foward, just follow the steps below and you'll be up and running in no time.

1. Install [Python 2.7.2](http://python.org/download/releases/2.7.2/) if you don't have it installed already.
2. Download the latest version of Trakt for Boxee [here](https://github.com/cold12/Trakt-for-Boxee/zipball/master)
3. Edit settings_example.cfg approriately, leave the Boxee port if you're unsure, and rename it to settings.cfg (or make a fresh copy if you want).
4. Pair Trakt For Boxee to your Boxee Box via the command 'python TraktForBoxee.py --pair' in the command line.

Startup script
--------------
1. Copy or move 'traktforboxee' file to your startup folder (usually '/etc/init.d/' depending on your system)
2. Make the file executable with 'chmod a+x /etc/init.d/traktforboxee'
3. Edit file and change the variables to match your system
4. Add script to startup by running 'update-rc.d traktforboxee defaults'

Updating
--------
To update Trakt For Boxee all you have to do is download the [newest version](https://github.com/cold12/Trakt-for-Boxee/zipball/master),
extract it and then copy over your old settings.cfg to the newly extracted folder.