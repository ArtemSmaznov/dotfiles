#!/bin/bash
echo 'What do you want to set up?'
PS3='Selection: '
options=("Bash" "Vim" "Tmux" ".configs" "Quit")
select opt in "${options[@]}"; do
    case $opt in
    "Bash")
        if [[ -f ~/.bashrc ]]
        rm -r ~/.bashrc
        fi
        ln -s $(pwd)/home/bashrc ~/.bashrc
        echo "symlink for .bashrc  recreated"
        ;;

    "Vim")
        if [[ -f ~/.vim_runtime ]]
          rm -r ~/.vim_rubntime
        fi
        if [[ -f ~/.vimrc ]]
          rm .vimrc
        fi
        ln -s $(pwd)/home/vim_runtime ~/.vim_runtime
        ln -s $(pwd)/home/vim_runtime/vimrc ~/.vimrc
        echo "symlinks for .vimrc and .vim_runtime/ recreated"
        ;;

    "Tmux")
        if [[ -f ~/.tmux.conf ]]
        rm ~/.tmux.conf
        fi
        ln -s $(pwd)/home/tmux.conf ~/.tmux.conf
        echo "symlink for .tmux.conf recreated"
        ;;

    ".configs")
        cp -r $(pwd)/config/* ~/.config/
        echo ".configs overwritten"
        ;;

    "Quit")
        echo Done!
        break
        ;;

   *) echo "invalid option $REPLY" ;;
    esac
done
