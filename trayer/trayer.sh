#!/usr/bin/env bash
# environment variables ________________________________________________________
[ ! "$XDG_CONFIG_HOME" ] && export XDG_CONFIG_HOME="$HOME/.config"

# variables ====================================================================
. "$XDG_CONFIG_HOME"/trayer/themes/base16.sh

bar_size=24

# setup ________________________________________________________________________
if [[ $(pidof trayer) ]]; then
    killall trayer
fi

sleep 2

# execution ********************************************************************
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
