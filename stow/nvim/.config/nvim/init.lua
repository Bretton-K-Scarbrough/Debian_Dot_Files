vim.g.mapleader = " "
vim.g.maplocalleader = " "

vim.g.python3_host_prog = vim.fn.expand("~/.virtualenvs/nvim/bin/python")

require("config.options")
require("config.keymaps")
require("config.autocmds")
require("config.lazyboots")
require("Comment.ft").set("zsh", "# %s")

vim.opt.termguicolors = true
require("bufferline").setup({
	options = {
		style_preset = require("bufferline").style_preset.default,
		diagnostics = "nvim_lsp",
	},
})

vim.opt.runtimepath:append(vim.fn.stdpath("data") .. "/lazy/nvim-treesitter/runtime")
