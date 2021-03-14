"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Visual Elements
set foldcolumn=1     " Add a bit extra margin to the left
set signcolumn=yes   " Always show the signcolumn, otherwise it would shift the text each time
set ruler            " Always show current position
set number           " Show line numbers
set relativenumber   " Make line numbers relative
set cursorline       " Enable highlighting of the current line
set showtabline=2    " Always show tabs
set laststatus=2     " Always display the status line
set showcmd          " Show commands
set cmdheight=2      " Height of the command bar
set splitbelow       " Horizontal splits will automatically be below
set splitright       " Vertical splits will automatically be to the right
set termwinsize=10x0 " Set size for terminal
" Disable scrollbars 
" set guioptions-=r
" set guioptions-=R
" set guioptions-=l
" set guioptions-=L

" Remove separator pipes
set fillchars+=vert:\ 

" Enable Mouse Support
set mouse=a
set ttymouse=sgr

" Configure backspace so it acts as it should act
set backspace=eol,start,indent
set whichwrap+=<,>,h,l

set ignorecase " Ignore case when searching
set smartcase  " When searching try to be smart about cases
set hlsearch   " Highlight search results
set incsearch  " Makes search act like search in modern browsers
set lazyredraw " Don't redraw while executing macros (good performance config)
set magic      " For regular expressions turn magic on

set showmatch " Show matching brackets when text indicator is over them
set mat=2     " How many tenths of a second to blink when matching brackets
set wildmenu  " Turn on the Wild menu
set so=7      " Leave 7 lines on screen above/below the cursor

" Step size for navigating with CTRL+e/y
noremap <C-e> 4<C-e>
noremap <C-y> 4<C-y>

" No annoying sound on errors
set noerrorbells
set novisualbell
set t_vb=
set tm=500

" Colorscheme
set background=dark
colorscheme gruvbox8

" Ignore compiled files
set wildignore=*.o,*~,*.pyc
if has("win16") || has("win32")
  set wildignore+=.git\*,.hg\*,.svn\*
else
  set wildignore+=*/.git/*,*/.hg/*,*/.svn/*,*/.DS_Store
endif

" Properly disable sound on errors on MacVim
if has("gui_macvim")
    autocmd GUIEnter * set vb t_vb=
endif


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Fast editing and reloading of vimrc configs
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <leader>eu :e! ~/.vim/settings/ui.vim<cr>
autocmd! bufwritepost ~/.vim/settings/ui.vim source ~/.vim/settings/ui.vim
