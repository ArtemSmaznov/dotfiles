#!/usr/bin/env bash
color="0x282828"

bar_size=24

if [[ $(pidof trayer) ]]
then
    killall trayer
fi

sleep 2
trayer \
    --edge top \
    --align right \
    --widthtype request \
    --height $bar_size \
    --SetDockType true \
    --SetPartialStrut true \
    --transparent true \
    --tint $color \
    --alpha 0 \
    --expand true \
    --padding 4 \
    --monitor 1
    # --distancefrom right \
    # --distance 400 \
