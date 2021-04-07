let g:ctrlp_working_path_mode = 0

" Quickly find and open a file in the current working directory
map <leader>sp :CtrlP<cr>

" Quickly find and open a buffer
map <leader>sb :CtrlPBuffer<cr>

" Quickly find and open a recently opened file
map <leader>sr :CtrlPMRU<CR>

let g:ctrlp_max_height = 20
let g:ctrlp_custom_ignore = 'node_modules\|^\.DS_Store\|^\.git\|^\.coffee'

