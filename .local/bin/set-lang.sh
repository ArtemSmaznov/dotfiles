#!/usr/bin/env bash
#
# Usage: set-lang.sh [language]
# Examples:
# - set-lang.sh jp
# - set-lang.sh en

setxkbmap -layout $1

if [[ $(eww ping 2> /dev/null) == "pong" ]]
then eww update kbd=$1
fi
