#!/usr/bin/env bash
paplay "$HOME/public/audio/windows95-startup.wav" &

~/.local/bin/dm-scripts/dm-wallpaper -refresh &

# xscreensaver -no-splash &
# xautolock -time 60 -locker "$HOME/.local/bin/dm-scripts/dm-lock" &
xss-lock -- "$HOME/.local/bin/dm-scripts/dm-lock" &

picom -b &
nm-applet &
blueman-applet &
dunst &
unclutter -jitter 5 &

fcitx5 -d &

redshift-gtk &
# solaar -w hide &
# emacs --daemon &

# alacritty -t btop -e btop &
qutebrowser &
/usr/bin/steam-runtime %U &
nextcloud &
