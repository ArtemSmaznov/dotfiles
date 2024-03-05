#!/usr/bin/env bash
[ -z "$1" ] && action="toggle" || action="$1"
[ -z "$2" ] && monitor=0 || monitor="$2"

case "$monitor" in
    0) status_bar="main-bar"   ;;
    1) status_bar="second-bar" ;;
    *) status_bar="main-bar"   ;;
esac

case $action in
    open)  eww open "$status_bar"          ;;
    close) eww close "$status_bar"         ;;
    *)     eww open --toggle "$status_bar" ;;
esac
