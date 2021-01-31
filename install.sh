#!/bin/bash
echo 'What do you want to set up?'
PS3='Selection: '
options=("Bash" "Vim" "Tmux" ".configs" "Quit")
select opt in "${options[@]}"; do
    case $opt in
    "Bash")
        rm -r ~/.bashrc
        ln -s $(pwd)/home/bashrc ~/.bashrc
        echo "symlink for .bashrc  recreated"
        ;;
    "Vim")
        rm -r ~/.vim_runtime ~/.vimrc
        ln -s $(pwd)/home/vim_runtime ~/.vim_runtime
        ln -s $(pwd)/home/vim_runtime/vimrc ~/.vimrc
        echo "symlinks for .vimrc and .vim_runtime/ recreated"
        ;;
    "Tmux")
        rm ~/.tmux.conf
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
