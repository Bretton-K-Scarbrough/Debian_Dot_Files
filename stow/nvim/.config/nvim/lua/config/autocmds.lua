-- Set spellcheck on for certain filetypes.
vim.api.nvim_create_autocmd({ "BufRead", "BufNewFile" }, {
	pattern = { "*.tex", "*.md" },
	command = "setlocal spell",
})

vim.api.nvim_create_autocmd("FileType", {
	callback = function(args)
		local ok = pcall(vim.treesitter.start, args.buf)
		if not ok then
			return -- No parser available for this language
		end
	end,
})
