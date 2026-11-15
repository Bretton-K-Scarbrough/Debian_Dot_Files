return {
	{
		"nvim-treesitter/nvim-treesitter",
		branch = "main",
		lazy = false,
		build = ":TSUpdate",

		config = function()
			local treesitter = require("nvim-treesitter")

			treesitter.setup({
				install_dir = vim.fn.stdpath("data") .. "/site",
			})

			treesitter.install({
				"python",
				"lua",
				"markdown",
				"markdown_inline",
				"vim",
				"vimdoc",
			})

			vim.api.nvim_create_autocmd("FileType", {
				pattern = {
					"python",
					"lua",
					"markdown",
					"vim",
					"help",
				},

				callback = function(args)
					local lang = vim.treesitter.language.get_lang(vim.bo[args.buf].filetype)

					if not lang then
						return
					end

					local queries = vim.treesitter.query.get_files(lang, "highlights")

					if #queries > 0 then
						vim.treesitter.start(args.buf)
					end
				end,
			})
		end,
	},
}
