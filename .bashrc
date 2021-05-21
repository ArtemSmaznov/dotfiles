#!/bin/bash
#
# Table of contents:
#   1. Options
#   2. History
#   3. Exports
#   4. Autocomplete
#   5. Sources
#   6. End Section

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

iatest=$(expr index "$-" i)


# ░█▀█░█▀█░▀█▀░▀█▀░█▀█░█▀█░█▀▀
# ░█░█░█▀▀░░█░░░█░░█░█░█░█░▀▀█
# ░▀▀▀░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀

# VIM mode - comment this out if you are not comfirtable with vim or kniw what vim is
# set -o vi

# Disable the bell
if [[ $iatest > 0 ]]; then bind "set bell-style visible"; fi

shopt -s globstar     # ** to mean reclusive
shopt -s autocd       # auto cd when entering just the path
shopt -s checkwinsize # Check the window size after each command and, if necessary, update the values of LINES and COLUMNS


# ░█░█░▀█▀░█▀▀░▀█▀░█▀█░█▀▄░█░█
# ░█▀█░░█░░▀▀█░░█░░█░█░█▀▄░░█░
# ░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░░▀░

# Allow ctrl-S for history navigation (with ctrl-R)
stty -ixon

# Causes bash to append to history instead of overwriting it so if you start a new terminal, you have old session history
shopt -s histappend
PROMPT_COMMAND='history -a'

# Expand the history size
export HISTFILESIZE=10000
export HISTSIZE=10000
export HISTFILE=$HOME/.cache/shell_history

# Don't put duplicate lines in the history and do not add lines that start with a space
export HISTCONTROL=erasedups:ignoreboth


# ░█▀▀░█░█░█▀█░█▀█░█▀▄░▀█▀░█▀▀
# ░█▀▀░▄▀▄░█▀▀░█░█░█▀▄░░█░░▀▀█
# ░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀

# Make local bin files usable
export PATH=$PATH:$HOME/.local/bin:$HOME/.local/bin/dmscripts

# Set user folder paths
export GIT_DIRECTORY="$HOME/Documents/git/ArtemSmaznov"
export WALL_DIRECTORY="$HOME/Pictures/wallpapers"

# Set the default editor
export EDITOR=vim
export VISUAL=vim

### SET MANPAGER
export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

# Color for manpages in less makes manpages a little easier to read
export LESS_TERMCAP_mb=$'\E[01;31m'
export LESS_TERMCAP_md=$'\E[01;31m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;44;33m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[01;32m'


# ░█▀█░█░█░▀█▀░█▀█░█▀▀░█▀█░█▄█░█▀█░█░░░█▀▀░▀█▀░█▀▀
# ░█▀█░█░█░░█░░█░█░█░░░█░█░█░█░█▀▀░█░░░█▀▀░░█░░█▀▀
# ░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀

# Enable history completion with up and down arrow keys
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

# Ignore case on auto-completion
# Note: bind used instead of sticking these in .inputrc
if [[ $iatest > 0 ]]; then bind "set completion-ignore-case on"; fi

# Show auto-completion list automatically, without double tab
# if [[ $iatest > 0 ]]; then bind "set show-all-if-ambiguous On"; fi


# ░█▀▀░█▀█░█░█░█▀▄░█▀▀░█▀▀░█▀▀
# ░▀▀█░█░█░█░█░█▀▄░█░░░█▀▀░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀

source_config() {
  [ -f $1 ] && source $1
}

# Primary imports
source_config $HOME/.config/bash/aliases
source_config $HOME/.config/bash/wol
source_config $HOME/.config/bash/prompt
source_config $HOME/.config/bash/bashrc

# FZF configs
source_config /usr/share/fzf/key-bindings.bash
source_config /usr/share/fzf/completion.bash


# ░█▀▀░█▀█░█▀▄
# ░█▀▀░█░█░█░█
# ░▀▀▀░▀░▀░▀▀░

# Source the Starship Prompt
if hash starship 2>/dev/null; then
  eval "$(starship init bash)"
fi

# Script to run on terminal launch
if hash neofetch 2>/dev/null; then
  neofetch
fi
