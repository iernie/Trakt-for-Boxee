#!/bin/sh
# by iernie@github

####### START EDIT ME ########

# Path to app
APP_PATH=/c/.traktforboxee

# Path to python bin
DAEMON=/usr/bin/python

# path to pid file
# Make sure this path has write permissions
PID_FILE=/var/run/traktforboxee.pid

# Name of app file
APP_NAME="TraktForBoxee.py"

# Default startup args
DEFAULT_OPTS="--daemon"

# user
RUN_AS=admin

####### END EDIT ME ##########

test -x $DAEMON || exit 0


start() {
    echo "Starting TraktForBoxee..."
    start-stop-daemon -d $APP_PATH -c $RUN_AS --start --background --pidfile $PID_FILE --make-pidfile --exec $DAEMON $APP_NAME -- $DEFAULT_OPTS
}

stop() {
    echo "Stopping TraktForBoxee..."
    start-stop-daemon --stop --pidfile $PID_FILE
}

pair() {
    echo "Starting pairing..."
    cd $APP_PATH
    $DAEMON $APP_NAME --pair
}

case "$1" in
    start)
        start
    ;;
    stop)
        stop
    ;;
    restart)
        stop
        start
    ;;
    pair)
        pair
    ;;
    *)
        echo "Usage: $0 {start|stop|restart|pair}"
        exit 1
    ;;
esac