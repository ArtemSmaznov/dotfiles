#!/usr/bin/env bash
xprop -spy -root _NET_ACTIVE_WINDOW |
    while read window_id
    do
        echo $window_id |
            awk '{print "getwindowname " $5}' |
            xdotool -
    done
