#!/usr/bin/env bash
uptime --pretty \
    | sed -e 's/up //' \
          -e 's/ \([a-z]\)\w*,*/\1/g' \
    | awk '{print $1 " " $2}'
