#!/usr/bin/env bash
if [[ $DESKTOP_SESSION == "xmonad" ]]
then
    xprop -spy -root _XMONAD_LOG |
        stdbuf -oL sed 's/^.*= //' |
        stdbuf -oL sed 's/^"\(.*\)"$/\1/' |
        stdbuf -oL awk -F'::::' '{ print $3 }'
fi

exit 0
