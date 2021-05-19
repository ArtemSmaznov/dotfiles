#!/bin/bash
#
# Table of content:
#   1. Shopt
#   2. Exports
#   3. Bindings
#   4. Sources
#   5. End Section

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

iatest=$(expr index "$-" i)

# Allow ctrl-S for history navigation (with ctrl-R)
stty -ixon

# VIM mode - comment this out if you are not comfirtable with vim or kniw what vim is
# set -o vi


# ░█▀▀░█░█░█▀█░█▀█░▀█▀
# ░▀▀█░█▀█░█░█░█▀▀░░█░
# ░▀▀▀░▀░▀░▀▀▀░▀░░░░▀░

# ** to mean reclusive
shopt -s globstar

# auto cd when entering just the path
shopt -s autocd

# Causes bash to append to history instead of overwriting it so if you start a new terminal, you have old session history
shopt -s histappend
PROMPT_COMMAND='history -a'

# Check the window size after each command and, if necessary, update the values of LINES and COLUMNS
shopt -s checkwinsize


# ░█▀▀░█░█░█▀█░█▀█░█▀▄░▀█▀░█▀▀
# ░█▀▀░▄▀▄░█▀▀░█░█░█▀▄░░█░░▀▀█
# ░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀

# Make local bin files usable
export PATH=$PATH:~/.local/bin:~/.local/bin/dmscripts

# Set user folder paths
export GIT_DIR="$HOME/Documents/git/ArtemSmaznov"
export WALL_DIR="$HOME/Pictures/wallpapers"

# Git Indicators
export GIT_PS1_SHOWDIRTYSTATE=true
export GIT_PS1_SHOWSTASHSTATE=true
export GIT_PS1_SHOWUNTRACKEDFILES=true
export GIT_PS1_SHOWUPSTREAM=auto

# Expand the history size
export HISTFILESIZE=10000
export HISTSIZE=500

# Don't put duplicate lines in the history and do not add lines that start with a space
export HISTCONTROL=erasedups:ignoreboth

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


# ░█▀▄░▀█▀░█▀█░█▀▄░▀█▀░█▀█░█▀▀░█▀▀
# ░█▀▄░░█░░█░█░█░█░░█░░█░█░█░█░▀▀█
# ░▀▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀

# Disable the bell
if [[ $iatest > 0 ]]; then bind "set bell-style visible"; fi

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

# FZF configs
if [[ -f /usr/share/fzf/key-bindings.bash ]];
then
  source /usr/share/fzf/key-bindings.bash;
fi
if [[ -f /usr/share/fzf/completion.bash ]];
then
  source /usr/share/fzf/completion.bash;
fi

# Aliases
if [[ -f ~/.bash/aliases ]]; then
  . ~/.bash/aliases
fi

# Prompt
if [[ -f ~/.bash/prompt ]]; then
  . ~/.bash/prompt
fi

# Wake Commands
if [[ -f ~/.bash/wol ]]; then
  . ~/.bash/wol
fi

# Source custom overwrites - needs to be placed at the very end
if [[ -f ~/.bash/bashrc ]]; then
  . ~/.bash/bashrc
fi


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
