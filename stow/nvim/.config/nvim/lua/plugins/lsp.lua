return {
	{
		"mason-org/mason-lspconfig.nvim",
		opts = {
			ensure_installed = {
				"lua_ls",
				"pyright",
				"rust_analyzer",
				"stylua",
				"markdown_oxide",
			},
		},

		dependencies = {
			{
				"mason-org/mason.nvim",
				opts = {
					ensure_installed = { "black" },
				},
			},
			"neovim/nvim-lspconfig",
			{
				"folke/lazydev.nvim",
				ft = "lua", -- only load on lua files
				opts = {
					library = {
						-- See the configuration section for more details
						-- Load luvit types when the `vim.uv` word is found
						{ path = "${3rd}/luv/library", words = { "vim%.uv" } },
					},
				},
			},
		},
	},
}
