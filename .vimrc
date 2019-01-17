set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" " alternatively, pass a path where Vundle should install plugins
" "call vundle#begin('~/some/path/here')
"
" " let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'nvie/vim-flake8'
Plugin 'tpope/vim-fugitive'
Plugin 'scrooloose/nerdtree'
Plugin 'airblade/vim-gitgutter'
"Plugin 'hashivim/vim-terraform'
Plugin 'flazz/vim-colorschemes'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
"Plugin 'powerline/powerline', {'rtp': 'powerline/bindings/vim/'}

" " All of your Plugins must be added before the following line
 call vundle#end()            " required
 filetype plugin indent on    " required

" Python Indentions
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix |
    \ set encoding=utf-8 |
" Call Flake8 on write
autocmd BufWritePost *.py call Flake8()

" Ignore files in NERDTree
let NERDTreeIgnore=['\.pyc$', '\~$']
let g:NERDTreeNodeDelimiter = "\u00a0"

" Terraform options
"let g:terraform_align=1 " Hashicorp indention
"let g:terraform_fmt_on_save=1 " Format and style on save. Runs 'terraform fmt' cmd
"let g:terraform_fold_sections=1 " Allows folding of sections

"" YAML formatting
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType yml setlocal ts=2 sts=2 sw=2 expandtab

" Set line numbers
set nu

" No swap files
set noswapfile

" Color schemes
syntax on

" Set backspace
set backspace=indent,eol,start

" Airline fonts
let g:airline_powerline_fonts = 1 
