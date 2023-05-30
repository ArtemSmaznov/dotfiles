#!/usr/bin/env bash
#
# Start flavours
# Base16 Gruvbox dark, medium theme
# by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)
# template by Artem Smaznov

background="0x282828"
# End flavours

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
    --tint $background \
    --alpha 0 \
    --expand true \
    --padding 4 \
    --monitor 0
    # --distancefrom right \
    # --distance 400 \
