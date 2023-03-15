#!/usr/bin/env bash
#
# Usage: set-volume.sh [+-] [%step]
# Examples:
# - set-volume.sh + 2
# - set-volume.sh - 1

direction=$1
step=$2

amixer -q sset Master ${step}%${direction} unmute
