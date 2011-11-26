#!/bin/sh

# CONFIG
HOMEPATH=/c/.traktforboxee

# # # #

SCRIPT=${HOMEPATH}/TraktForBoxee.py
PIDFILE=${HOMEPATH}/TraktForBoxee.pid

start() {
    if [[ -f $PIDFILE ]]; then
        echo "TraktForBoxee is already running."
    else
        echo "Starting TraktForBoxee..."
        python $SCRIPT --daemon
        echo "TraktForBoxee started."
    fi
}

stop() {
    if ! [[ -f $PIDFILE ]]; then
        echo "TraktForBoxee is not running."
    else
        echo "Stopping TraktForBoxee..."
        python $SCRIPT --daemon
        rm $PIDFILE
        echo "TraktForBoxee stopped."
    fi
}

pair() {
    echo "Starting pairing..."
    python $SCRIPT --pair
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
        sleep 2
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