let g:which_key_vertical = 1
let g:which_key_position = 'botright'
let g:which_key_use_floating_win = 1
let g:which_key_default_group_name = '+ unnamed'

" register dictionary for the <Space>-prefix
call which_key#register(' ', "g:which_key_map")

nnoremap <silent> <leader> :WhichKey ' '<CR>
vnoremap <silent> <leader> :WhichKeyVisual ' '<CR>
" default mappings like ]s stop working if which-key doesn't know about them
" nnoremap <silent> [ :WhichKey '['<CR>
" nnoremap <silent> ] :WhichKey ']'<CR>

" Define prefix dictionary
let g:which_key_map =  {}
let g:which_key_map.b = { 'name' : '+buffer' }
let g:which_key_map.c = { 'name' : '+NERDCommenter' }
let g:which_key_map.e = { 'name' : '+edit' }
let g:which_key_map.g = { 'name' : '+git' }
  let g:which_key_map.g.d = [ 'vertical Gdiffsplit', 'Diff Split' ]
  let g:which_key_map.g.g = [ 'vertical Gstatus', 'Status' ]
let g:which_key_map.i = { 'name' : '+coc' }
let g:which_key_map.s = { 'name' : '+search' }
let g:which_key_map.t = { 'name' : '+tabs' }
let g:which_key_map.u = { 'name' : '+ui' }

let g:which_key_map[']'] = {
      \ 'name' : '+[]',
      \ 's' : ['', 'Spell Checking'],
      \ 'g' : ['', 'Coc Linters'],
      \ 'c' : ['', 'Git Hunks']
      \}

