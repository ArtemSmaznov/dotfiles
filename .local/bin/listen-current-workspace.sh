#!/usr/bin/env bash
xprop -spy -root _NET_CURRENT_DESKTOP |
    while read workspace_index; do
        echo $workspace_index |
            awk '{print $3}'
    done
