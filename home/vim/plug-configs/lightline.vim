let g:lightline = {
      \ 'component': {
      \   'readonly': '%{&filetype=="help"?"":&readonly?"🔒":""}',
      \   'modified': '%{&filetype=="help"?"":&modified?"+":&modifiable?"":"-"}',
      \   'fugitive': '%{exists("*FugitiveHead")?FugitiveHead():""}'
      \ },
      \ 'component_visible_condition': {
      \   'readonly': '(&filetype!="help"&& &readonly)',
      \   'modified': '(&filetype!="help"&&(&modified||!&modifiable))',
      \   'fugitive': '(exists("*FugitiveHead") && ""!=FugitiveHead())'
      \ }
      \}

let g:lightline.colorscheme = 'jellybeans'
let g:lightline.active = {
      \ 'left': [ 
      \   ['mode', 'paste'],
      \   ['fugitive'],
      \   ['readonly', 'filename', 'modified']
      \ ],
      \ 'right': [
      \   ['lineinfo'],
      \   ['percent'],
		  \   [ 'fileformat', 'fileencoding', 'filetype' ] 
      \ ]
      \}

let g:lightline.inactive = { 
      \ 'left' : [
      \   ['fugitive'],
      \   ['readonly', 'filename', 'modified']
      \ ],
      \ 'right' : [
      \   ['lineinfo'],
      \   ['percent'],
		  \   [ 'filetype' ] 
      \ ]
      \}

let g:lightline.tab = {
	    \ 'active': [ 'tabnum', 'filename', 'modified' ],
	    \ 'inactive': [ 'tabnum', 'filename', 'modified' ]
      \}


let g:lightline.separator = { 'left': ' ', 'right': ' ' }
let g:lightline.subseparator = { 'left': '|', 'right': '|' }
let g:lightline.tabline_separator = { 'left': ' ', 'right': ' ' }
let g:lightline.tabline_subseparator = { 'left': '|', 'right': '|' }


