"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Key Mappings that are specific to plugins are defined per plugin under 'plug-configs' directory
"
" Sections:
"    -> General
"    -> File navigation
"    -> Spell checking
"    -> Tabs, windows and buffer
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" :W sudo saves the file 
" (useful for handling the permission-denied error)
command! W execute 'w !sudo tee % > /dev/null' <bar> edit!

" Remove the Windows ^M - when the encodings gets messed up
noremap <Leader>m mmHmt:%s/<C-V><cr>//ge<cr>'tzt'm

" Toggle paste mode on and off
map <leader>pp :setlocal paste!<cr>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => File navigation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Visual mode pressing * or # searches for the current selection
" Super useful! From an idea by Michael Naumann
vnoremap <silent> * :<C-u>call VisualSelection('', '')<CR>/<C-R>=@/<CR><CR>
vnoremap <silent> # :<C-u>call VisualSelection('', '')<CR>?<C-R>=@/<CR><CR>

" Move a line of text using Shift+j/k in all modes 
nnoremap K :m-2<cr>==
nnoremap J :m+<cr>==
vnoremap K :m '<-2<cr>gv=gv
vnoremap J :m '>+1<cr>gv=gv

" Encase in parenthesis/brackets
vnoremap $> <esc>`>a)<esc>`<i(<esc>
vnoremap $] <esc>`>a]<esc>`<i[<esc>
vnoremap $} <esc>`>a}<esc>`<i{<esc>
vnoremap $" <esc>`>a"<esc>`<i"<esc>
vnoremap $' <esc>`>a'<esc>`<i'<esc>
vnoremap $` <esc>`>a`<esc>`<i`<esc>


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Spell checking
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Pressing ,ss will toggle and untoggle spell checking
map <leader>ss :setlocal spell!<cr>


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Tabs, windows and buffers
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Smart way to move between windows
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

" Resize windows
noremap <silent> <C-Left> :vertical resize +4<CR>
noremap <silent> <C-Right> :vertical resize -4<CR>
noremap <silent> <C-Up> :resize +4<CR>
noremap <silent> <C-Down> :resize -4<CR>

" Useful mappings for managing tabs
map <leader>tn :tabnew<cr>
map <leader>to :tabonly<cr>
map <leader>tc :tabclose<cr>
map <leader>tm :tabmove 
map <leader>t<leader> :tabnext<cr>

" Let 'tl' toggle between this and the last accessed tab
let g:lasttab = 1
nmap <Leader>tl :exe "tabn ".g:lasttab<CR>
au TabLeave * let g:lasttab = tabpagenr()

" Working with buffers
map <silent> <leader><space> :noh<cr>     " Disable search highlight
map <leader>bd :Bclose<cr>:tabclose<cr>gT " Close the current buffer
map <leader>ba :bufdo bd<cr>              " Close all the buffers
map <leader>h :bprevious<cr>              " Prev buffer
map <leader>l :bnext<cr>                  " Next buffer

" Switch CWD to the directory of the open buffer
map <leader>cd :cd %:p:h<cr>:pwd<cr>



