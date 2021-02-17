let g:gitgutter_enabled=1

nnoremap <silent> <leader>gg :vertical Gstatus<cr>
nnoremap <silent> <leader>gd :vertical Gdiffsplit<cr>

nmap <leader>gp <Plug>(GitGutterPreviewHunk)
map <leader>gs <Plug>(GitGutterStageHunk)
nmap <leader>gu <Plug>(GitGutterUndoHunk)
