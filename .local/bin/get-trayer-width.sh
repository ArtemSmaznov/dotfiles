#!/usr/bin/env bash
if [ $(pidof trayer) ]
then xprop -name panel | grep 'program specified minimum size' | awk '{print $5}'
else echo 0
fi
