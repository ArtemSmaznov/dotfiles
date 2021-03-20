#!/bin/bash

# Set with the flags "-e", "-u","-o pipefail" cause the script to fail
# if certain things happen, which is a good thing.  Otherwise, we can
# get hidden bugs that are hard to discover.
set -euo pipefail

# Specifying a directory to save our screenshots.
SCREENSHOT_DIR="$HOME/Pictures/Screenshots"
# Makes sure the directory exists.
mkdir -p "${SCREENSHOT_DIR}"

# Filename Time Stamp Format
getTimeStamp() {
  date '+%Y-%m-%d_%T'
}

EXECUTE=true
MAIM_ARGS=""

# Get monitors and their settings for maim
DISPLAYS=$(xrandr --listactivemonitors | grep '+' | awk '{print $4, $3}' | awk -F'[x/+* ]' '{print $1,$2"x"$4"+"$6"+"$7}')

# Add monitor data
IFS=$'\n'
declare -A DISPLAY_MODE
for d in ${DISPLAYS}; do
  name=$(echo "${d}" | awk '{print $1}')
  area="$(echo "${d}" | awk '{print $2}')"
  DISPLAY_MODE[${name}]="${area}"
done
unset IFS



if [[ $1 == 'full' ]]; then
  MAIM_ARGS="-u -m 1"

elif [[ $1 == 'area' ]]; then
  MAIM_ARGS="-u -B -s -n -m 1"

elif [[ $1 == 'screen' ]]; then
  MAIM_ARGS="-u -g ${DISPLAY_MODE['DVI-D-0']} -m 1"

elif [[ $1 == 'window' ]]; then
  active_window=$(xdotool getactivewindow)
  MAIM_ARGS="-u -B -i ${active_window} -m 1"

else
  EXECUTE=false
  if [[ $1 == 'debug' ]]; then
    echo ${DISPLAY_MODE["DVI-D-0"]}

  else
    echo 'Only the following arguments are accepted: full, area, window'
  fi
fi


if $EXECUTE; then
  maim ${MAIM_ARGS} "${SCREENSHOT_DIR}/$(getTimeStamp).png"
fi

