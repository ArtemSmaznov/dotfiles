#!/usr/bin/env bash
eww update music-flags="$(~/.local/bin/get-music.sh flags)"
eww update music-volume="$(~/.local/bin/get-music.sh volume)"
eww update music-state="$(~/.local/bin/get-music.sh state)"
