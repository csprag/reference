Making Vim your IDE
-------

A few things an eecs201 student did to make his vim like an IDE.

---

## Basic additions to your .vimrc
* The following require no vim plugins, but will improve your vim in basic ways to make it faster. Some of the
	remaps can be changed to your liking so you maneuver more efficiently through vim.

```
" will underline where your cursor is currently
set cursorline

" remaps <esc> to jk because its faster and on the home row
inoremap jk <esc> 

" adds numbers to line 
set number

" changes it so that numbers are relative to the line you're on making precise navigation easy
set relativenumber

syntax on
syntax enable

" remaps the command to move to the beginning / end of line 
nnoremap B ^
nnoremap E $

" makes it so that $ / ^ now don't do anything (they used to move to beginning / end line respectively)
nnoremap $ <nop>
nnoremap ^ <nop>

" shows command in bottom bar
set showcmd

```

### vim-plug  

* But by using plugins you can also add a lot more features

* Go to the vim-plug (plugin manager I use) site : 

- https://github.com/junegunn/vim-plug/wiki/tutorial

* Now that you have the plugin, you can add the following plugins that I find really useful 

* You should look at the documentation for them, but I'll tell you about some of them

	1. ***nerdtree*** shows a tree view of the project you have open and lets you opens files in splits and more

	1. ***ale*** is a linter for vim that will tell you when you're making precompile errors like unused variables ... etc

	1. ***surround*** lets you add (or remove) quotes or parathenses to textobjects

	1. ***lightline*** makes your status bar look a lot cooler

	1. ***clang*** is a autocomplete for c family languages (requires that you have clang installed) 

	1. ***fugitive*** lets you run git commands in vim like commit, add, push ... etc

	1. ***delimitMate*** automatically creates the pair to curly brace or parantheses or brackets 

```
call plug#begin('~/.vim/plugged')

Plug 'junegunn/vim-easy-align'
Plug 'scrooloose/nerdtree', {'on': 'NERDTreeToggle'}
Plug 'sjl/gundo.vim'
Plug 'w0rp/ale'
Plug 'tpope/vim-eunuch'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-repeat'
Plug 'itchyny/lightline.vim'
Plug 'Raimondi/delimitMate'
Plug 'justmao945/vim-clang'
Plug 'tpope/vim-fugitive'

call plug$#end()
```

###  After adding that to your .vimrc, run the following while in vim.

```
:source %

:PlugInstall
```

* Now your vim should be more like an IDE. You can add even more plugins by searching the internet. Vim has a 
	steep learning curve but it can make you a lot faster at changing code if you take the time to learn it and 
	add a few usefule plugins to provide the benefits of a full IDE.
