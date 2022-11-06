#!/bin/bash

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

iatest=$(expr index "$-" i)

# VIM mode - comment this out if you are not comfirtable with vim or kniw what vim is
set -o vi

# Disable the bell
if [[ $iatest > 0 ]]; then bind "set bell-style visible"; fi

shopt -s globstar     # ** to mean reclusive
shopt -s autocd       # auto cd when entering just the path
shopt -s checkwinsize # Check the window size after each command and, if necessary, update the values of LINES and COLUMNS

# Allow ctrl-S for history navigation (with ctrl-R)
stty -ixon

# Causes bash to append to history instead of overwriting it so if you start a new terminal, you have old session history
shopt -s histappend
PROMPT_COMMAND='history -a'

# Expand the history size
export HISTFILESIZE=10000
export HISTSIZE=10000

# Don't put duplicate lines in the history and do not add lines that start with a space
export HISTCONTROL=erasedups:ignoreboth

# Make local bin files usable
export PATH=$PATH:$HOME/.local/bin
export PATH=$PATH:$HOME/.local/bin/dm-scripts
export PATH=$PATH:$XDG_CONFIG_HOME/emacs/bin

### SET MANPAGER
export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'

# Enable history completion with up and down arrow keys
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

# Ignore case on auto-completion
# Note: bind used instead of sticking these in .inputrc
if [[ $iatest > 0 ]]; then bind "set completion-ignore-case on"; fi

# Show auto-completion list automatically, without double tab
# if [[ $iatest > 0 ]]; then bind "set show-all-if-ambiguous On"; fi

function source_config() {
  [ -f $1 ] && source $1
}

# Primary imports
source_config $XDG_CONFIG_HOME/shell/exportrc
source_config $XDG_CONFIG_HOME/shell/aliasrc
source_config $XDG_CONFIG_HOME/shell/wol
source_config $XDG_CONFIG_HOME/bash/prompt
source_config $XDG_CONFIG_HOME/bash/bashrc

# FZF configs
source_config /usr/share/fzf/key-bindings.bash
source_config /usr/share/fzf/completion.bash

# MPC configs
source_config $XDG_CONFIG_HOME/mpc/mpcvars

function has_command() {
    hash "$1" 2>/dev/null
    return $?
}

# Source the Starship Prompt
if has_command starship; then eval "$(starship init bash)"; fi

# Script to run on terminal launch
if has_command neofetch; then neofetch; fi
