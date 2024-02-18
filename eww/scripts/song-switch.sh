#!/usr/bin/env bash
eww update music-song="$(~/.local/bin/get-music.sh song)"
eww update music-title="$(~/.local/bin/get-music.sh title)"
eww update music-artist="$(~/.local/bin/get-music.sh artist)"
eww update music-album="$(~/.local/bin/get-music.sh album)"
eww update music-album-cover-file="$(~/.local/bin/get-music.sh albumcover)"
