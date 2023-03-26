#!/usr/bin/env bash
if [[ ! $(pidof eww) ]]; then
    eww daemon
fi

eww open-many \
    bar0 \
    bar1
