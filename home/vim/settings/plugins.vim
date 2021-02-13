""""""""""""""""""""""""""""""
" => Load Plugins
""""""""""""""""""""""""""""""
call plug#begin('~/.vim/plugged')
Plug 'jiangmiao/auto-pairs'                     " Insert or delete brackets, parens, quotes in pair
Plug 'neoclide/coc.nvim', {'branch': 'release'} " LSP support for Vim & Neovim
Plug 'itchyny/lightline.vim'                    " A light and configurable statusline/tabline for Vim
" Plug 'powerline/powerline'                      " A more powerfull statusline
Plug 'ctrlpvim/ctrlp.vim'                       " Fuzzy file, buffer, mru, tag, ... finder
Plug 'godlygeek/tabular'                        " Configurable, flexible, intuitive text aligning
Plug 'terryma/vim-expand-region'                " Incremental visual selection
Plug 'airblade/vim-gitgutter'                   " A Vim plugin which shows a git diff in the gutter
Plug 'michaeljsmith/vim-indent-object'          " Text objects based on indent levels
Plug 'farmergreg/vim-lastplace'                 " Intelligently reopen files where you left off
Plug 'maxbrunsfeld/vim-yankstack'               " Plugin for storing and cycling through yanked text strings
Plug 'tpope/vim-fugitive'                       " A Git wrapper so awesome, it should be illegal
Plug 'tpope/vim-surround'                       " Plugin for deleting, changing, and adding surroundings
Plug 'ryanoasis/vim-devicons' |
" Plug 'preservim/nerdtree' |                     
      " \ Plug 'tiagofumo/vim-nerdtree-syntax-highlight' |
      " \ Plug 'Xuyuanp/nerdtree-git-plugin' 
      " \ Plug 'tsony-tsonev/nerdtree-git-plugin' 

" To learn
Plug 'mileszs/ack.vim'                          " Plugin that integrates ack with Vim
Plug 'jlanzarotta/bufexplorer'                  " Buffer Explorer

" Language Support
Plug 'tpope/vim-cucumber'                       " Filetype plugin for Cucumber
Plug 'pangloss/vim-javascript'                  " Filetype plugin for JavaScript
Plug 'leafgarland/typescript-vim'               " Filetype plugin for TypeScript
Plug 'plasticboy/vim-markdown'                  " Vim Markdown
Plug 'rust-lang/rust.vim'                       " Filetype plugin for Rust
Plug 'scrooloose/nerdcommenter'                 " Plugin for commenting code

" Color Schemes
Plug 'lifepillar/vim-gruvbox8'

call plug#end()


""""""""""""""""""""""""""""""
" => Load Configs
""""""""""""""""""""""""""""""
source ~/.vim/settings/plugins/coc.vim
source ~/.vim/settings/plugins/tabularize.vim
source ~/.vim/settings/plugins/buffExplorer.vim
source ~/.vim/settings/plugins/yankstack.vim
source ~/.vim/settings/plugins/ctrlp.vim 
source ~/.vim/settings/plugins/nerdcommenter.vim
" source ~/.vim/settings/plugins/nerdtree.vim
source ~/.vim/settings/plugins/surround.vim
source ~/.vim/settings/plugins/lightline.vim
source ~/.vim/settings/plugins/gitGutter.vim


" Automatically install missing plugins on startup
autocmd VimEnter *
  \  if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \|   PlugInstall --sync | q
  \| endif
