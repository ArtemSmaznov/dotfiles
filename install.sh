#!/bin/bash
echo 'What do you want to set up?'
PS3='Selection: '
options=("Bash" "Vim" "Tmux" ".configs" "Quit")
select opt in "${options[@]}"; do
    case $opt in
    "Bash")
        if [[ -f ~/.bashrc ]]; then
          rm -r ~/.bashrc
        fi
        ln -s $(pwd)/home/bashrc ~/.bashrc
        echo "symlink for .bashrc  recreated"
        ;;

    "Vim")
        if [[ -f ~/.vimrc ]]; then
          rm ~/.vimrc
          echo "vimrc replaced"
        fi
        ln -s $(pwd)/home/vim/rc.vim ~/.vimrc

        if [[ -f ~/.vim ]]; then
          rm ~/.vim
          echo "vim runtime replaced"
        fi
        ln -s $(pwd)/home/vim ~/.vim

        echo "symlinks for .vimrc and .vim/ recreated"
        ;;

    "Tmux")
        if [[ -f ~/.tmux.conf ]]; then
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
