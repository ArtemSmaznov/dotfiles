#!/usr/bin/env bash
setxkbmap -query | awk '$1=="layout:" {print $2}'
