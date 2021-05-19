HISTFILE=~/.config/zsh/histfile
HISTSIZE=1000
SAVEHIST=10000

setopt autocd
unsetopt beep
setopt COMPLETE_ALIASES # autocompletion of command line switches for aliases

bindkey -v


zstyle :compinstall filename '/home/artem/.zshrc'

# Load autocompletion
autoload -Uz compinit
compinit

zstyle ':completion:*' menu select
zstyle ':completion::complete:*' gain-privileges 1
zstyle ':completion:*' rehash true


# ░█▀▀░█▀█░█░█░█▀▄░█▀▀░█▀▀░█▀▀
# ░▀▀█░█░█░█░█░█▀▄░█░░░█▀▀░▀▀█
# ░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀

# Aliases
if [[ -f ~/.config/bash/aliases ]]; then
  . ~/.config/bash/aliases
fi

# Wake Commands
if [[ -f ~/.config/bash/wol ]]; then
  . ~/.config/bash/wol
fi

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh


# ░█▀▀░█▀█░█▀▄
# ░█▀▀░█░█░█░█
# ░▀▀▀░▀░▀░▀▀░

# Source the Starship Prompt
if hash starship 2>/dev/null; then
  eval "$(starship init zsh)"
fi

