#!/bin/sh
# by iernie@github

####### START EDIT ME ########

PYTHON_PATH=/usr/bin/python
APP_PATH=/c/.traktforboxee
RUN_AS=admin

####### END EDIT ME ##########

SCRIPT=${APP_PATH}/TraktForBoxee.py
PIDFILE=${APP_PATH}/TraktForBoxee.pid

chown -R ${RUN_AS}:${RUN_AS} ${APP_PATH}
chmod -R 755 ${APP_PATH}


start() {
    if [[ -f $PIDFILE ]]; then
        echo "TraktForBoxee is already running."
    else
        echo "Starting TraktForBoxee..."
        $PYTHON_PATH $SCRIPT --daemon
        echo "TraktForBoxee started."
    fi
}

stop() {
    if ! [[ -f $PIDFILE ]]; then
        echo "TraktForBoxee is not running."
    else
        echo "Stopping TraktForBoxee..."
        kill `cat $PIDFILE`
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