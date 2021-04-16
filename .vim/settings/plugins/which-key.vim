let g:which_key_position = 'botright'
let g:which_key_vertical = 1
let g:which_key_centered = 0
let g:which_key_flatten = 1
let g:which_key_use_floating_win = 1
let g:which_key_fallback_to_native_key=1

" register dictionary for the <Space>-prefix
call which_key#register(' ', "g:leader_map")
nnoremap <silent> <leader> :WhichKey ' '<CR>
vnoremap <silent> <leader> :WhichKeyVisual ' '<CR>

" default mappings like ]s stop working if which-key doesn't know about them
call which_key#register('[', "g:left_square_bracket_map")
call which_key#register(']', "g:right_square_bracket_map")
nnoremap <silent> [ :WhichKey '['<CR>
nnoremap <silent> ] :WhichKey ']'<CR>


let g:which_key_default_group_name = '+Group'

" Define prefix dictionary
let g:leader_map =  {}
let g:leader_map['`'] = [ 'term', 'Terminal' ]
let g:leader_map['k'] = [ 'call <SID>show_documentation()', 'Search Documentation' ]
let g:leader_map.b = { 'name' : '+ Buffers' }
  let g:leader_map.b.a = [ 'bufdo bd', 'Close all buffers' ]
  let g:leader_map.b.d = [ 'Bclose<cr>:tabclose<cr>gT', 'Close current buffer' ]
  let g:leader_map.b.c = [ 'cd %:p:h<cr>:pwd<cr>', 'CD to current directory' ]
  let g:leader_map.b.h = [ 'bprevious', 'Prev Buffer' ]
  let g:leader_map.b.l = [ 'bnext', 'Next Buffer' ]
let g:leader_map.c = { 'name' : '+ Coc' }
let g:leader_map.e = { 'name' : '+ Edit Config' }
let g:leader_map.g = { 'name' : '+ Git' }
  let g:leader_map.g.d = [ 'vertical Gdiffsplit', 'Diff Split' ]
  let g:leader_map.g.g = [ 'vertical Gstatus', 'Status' ]
let g:leader_map.m = { 'name' : '+ Minimap' }
let g:leader_map.s = { 'name' : '+ Search' }
let g:leader_map.f = { 'name' : '+ Search' }
let g:leader_map.t = { 'name' : '+ Tabs' }
let g:leader_map.u = { 'name' : '+ UI' }
let g:leader_map.y = { 'name' : '+ YankStack' }

let g:leader_map[','] = {
      \ 'name' : '+Leaderless',
      \ 'cd' : ['cd %:p:h<cr>:pwd', 'CD to PWD of open Buffer']
      \}

let g:right_square_bracket_map = {}
let g:right_square_bracket_map.c = [ '<Plug>(GitGutterNextHunk)', 'Next Git Hunk' ]
let g:right_square_bracket_map.g = [ '<Plug>(coc-diagnostic-next)', 'Next Coc Problem' ]
" let g:right_square_bracket_map.s = [ '', 'Next Spell Check Problem' ]

let g:left_square_bracket_map = {}
let g:left_square_bracket_map.c = [ '<Plug>(GitGutterNextHunk)', 'Next Git Hunk' ]
let g:left_square_bracket_map.g = [ '<Plug>(coc-diagnostic-next)', 'Next Coc Problem' ]
" let g:left_square_bracket_map.s = [ '', 'Next Spell Check Problem' ]
