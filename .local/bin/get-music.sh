#!/usr/bin/env bash
usage="""Usage:
    get-music.sh song
    get-music.sh state
    get-music.sh flags """

convert_flag() {
    if [[ $(mpc status "%$1%") == "on" ]]
    then echo $2
    else echo -
    fi
}

get_flags() {
    echo "[$(convert_flag repeat r)$(convert_flag random z)$(convert_flag single s)$(convert_flag consume c)]"
}

case $1 in
    song) mpc current -f "%artist% - %title%";;
    state) mpc status "%state%";;
    flags) get_flags;;
    *) echo "$usage"
esac
