" ==> Nerd Tree Git
let g:NERDTreeGitStatusWithFlags = 1
let g:NERDTreeGitStatusUseNerdFonts = 1 " you should install nerdfonts by yourself. default: 0

let NERDTreeShowHidden=1
let NERDTreeIgnore = ['^node_modules','\.pyc$', '__pycache__']

map <C-n> :NERDTreeToggle<cr> :wincmd p<cr>
map <leader>n :NERDTreeFind<cr> 

" autocmd VimEnter * NERDTreeFind | wincmd p

" Close NERDTree with tab
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") 
\ && b:NERDTree.isTabTree()) | q | endif

" Open the existing NERDTree on each new tab.
autocmd BufWinEnter * silent NERDTreeMirror


