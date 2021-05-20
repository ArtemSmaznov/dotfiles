# Table of contents:
#   1. Options
#   2. History
#   3. Exports
#   4. Autocomplete
#   5. Keys
#   6. Sources
#   7. End Section


# ░█▀█░█▀█░▀█▀░▀█▀░█▀█░█▀█░█▀▀
# ░█░█░█▀▀░░█░░░█░░█░█░█░█░▀▀█
# ░▀▀▀░▀░░░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀

# VIM mode - comment this out if you are not comfirtable with vim or kniw what vim is
bindkey -v

# Disable the bell
unsetopt beep

setopt autocd           # auto cd when entering just the path


# ░█░█░▀█▀░█▀▀░▀█▀░█▀█░█▀▄░█░█
# ░█▀█░░█░░▀▀█░░█░░█░█░█▀▄░░█░
# ░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░░▀░

# History
SAVEHIST=10000
HISTSIZE=10000
HISTFILE=$HOME/.cache/shell_history

# Causes zsh to append to history instead of overwriting it so if you start a new terminal, you have old session history
setopt INC_APPEND_HISTORY

# Don't put duplicate lines in the history and do not add lines that start with a space
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_IGNORE_SPACE


# ░█▀▀░█░█░█▀█░█▀█░█▀▄░▀█▀░█▀▀
# ░█▀▀░▄▀▄░█▀▀░█░█░█▀▄░░█░░▀▀█
# ░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀

# Make local bin files usable
path+=($HOME/.local/bin)
path+=($HOME/.local/bin/dmscripts)

# Set user folder paths
export GIT_DIRECTORY="$HOME/Documents/git/ArtemSmaznov"
export WALL_DIRECTORY="$HOME/Pictures/wallpapers"

# Set the default editor
export EDITOR=vim
export VISUAL=vim

### SET MANPAGER
export MANPAGER='/bin/bash -c "vim -MRn -c \"set buftype=nofile showtabline=0 ft=man ts=8 nomod nolist noma\" -c \"normal L\" -c \"nmap q :qa<CR>\"</dev/tty <(col -b)"'


# ░█▀█░█░█░▀█▀░█▀█░█▀▀░█▀█░█▄█░█▀█░█░░░█▀▀░▀█▀░█▀▀
# ░█▀█░█░█░░█░░█░█░█░░░█░█░█░█░█▀▀░█░░░█▀▀░░█░░█▀▀
# ░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀

fpath=(~/.config/zsh/completion $fpath)
zstyle :compinstall filename '/home/artem/.zshrc'

# Autocompletion
autoload -Uz compinit && compinit # Load autocompletion
zstyle ':completion::complete:*' gain-privileges 1 # Enable aliases for Sudo commands
zstyle ':completion:*' menu select
zstyle ':completion:*' rehash true                 # automatically rehash bin files
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'

zstyle -e ':completion:*:default' list-colors 'reply=("${PREFIX:+=(#bi)($PREFIX:t)(?)*==02=01}:${(s.:.)LS_COLORS}")' # Color the common prefix

# enable history search
autoload -Uz up-line-or-beginning-search down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search


# ░█░█░█▀▀░█░█░█▀▀
# ░█▀▄░█▀▀░░█░░▀▀█
# ░▀░▀░▀▀▀░░▀░░▀▀▀

# create a zkbd compatible hash;
# to add other keys to this hash, see: man 5 terminfo
typeset -g -A key

key[Home]="${terminfo[khome]}"
key[End]="${terminfo[kend]}"
key[Insert]="${terminfo[kich1]}"
key[Backspace]="${terminfo[kbs]}"
key[Delete]="${terminfo[kdch1]}"
key[Up]="${terminfo[kcuu1]}"
key[Down]="${terminfo[kcud1]}"
key[Left]="${terminfo[kcub1]}"
key[Right]="${terminfo[kcuf1]}"
key[PageUp]="${terminfo[kpp]}"
key[PageDown]="${terminfo[knp]}"
key[Shift-Tab]="${terminfo[kcbt]}"
key[Control-Left]="${terminfo[kLFT5]}"
key[Control-Right]="${terminfo[kRIT5]}"

# setup key accordingly
[[ -n "${key[Home]}"          ]] && bindkey -- "${key[Home]}"          beginning-of-line
[[ -n "${key[End]}"           ]] && bindkey -- "${key[End]}"           end-of-line
[[ -n "${key[Backspace]}"     ]] && bindkey -- "${key[Backspace]}"     backward-delete-char
[[ -n "${key[Delete]}"        ]] && bindkey -- "${key[Delete]}"        delete-char
[[ -n "${key[Up]}"            ]] && bindkey -- "${key[Up]}"            up-line-or-beginning-search
[[ -n "${key[Down]}"          ]] && bindkey -- "${key[Down]}"          down-line-or-beginning-search
[[ -n "${key[Left]}"          ]] && bindkey -- "${key[Left]}"          backward-char
[[ -n "${key[Right]}"         ]] && bindkey -- "${key[Right]}"         forward-char
[[ -n "${key[PageUp]}"        ]] && bindkey -- "${key[PageUp]}"        beginning-of-buffer-or-history
[[ -n "${key[PageDown]}"      ]] && bindkey -- "${key[PageDown]}"      end-of-buffer-or-history
[[ -n "${key[Shift-Tab]}"     ]] && bindkey -- "${key[Shift-Tab]}"     reverse-menu-complete
[[ -n "${key[Control-Left]}"  ]] && bindkey -- "${key[Control-Left]}"  backward-word
[[ -n "${key[Control-Right]}" ]] && bindkey -- "${key[Control-Right]}" forward-word

# Bind ctrl + space to accept the current suggestion.
bindkey '^ ' end-of-line

# Finally, make sure the terminal is in application mode, when zle is
# active. Only then are the values from $terminfo valid.
if (( ${+terminfo[smkx]} && ${+terminfo[rmkx]} )); then
	autoload -Uz add-zle-hook-widget
	function zle_application_mode_start { echoti smkx }
	function zle_application_mode_stop { echoti rmkx }
	add-zle-hook-widget -Uz zle-line-init zle_application_mode_start
	add-zle-hook-widget -Uz zle-line-finish zle_application_mode_stop
fi


# ░█▀▀░█▀█░█░█░█▀▄░█▀▀░█▀▀░█▀▀
# ░▀▀█░█░█░█░█░█▀▄░█░░░█▀▀░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀

[ -f $HOME/.config/bash/aliases ] && source $HOME/.config/bash/aliases
[ -f $HOME/.config/bash/wol ] && source $HOME/.config/bash/wol

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh


# ░█▀▀░█▀█░█▀▄
# ░█▀▀░█░█░█░█
# ░▀▀▀░▀░▀░▀▀░

# Source the Starship Prompt
if hash starship 2>/dev/null; then
  eval "$(starship init zsh)"
fi

# Script to run on terminal launch
if hash neofetch 2>/dev/null; then
  neofetch
fi
