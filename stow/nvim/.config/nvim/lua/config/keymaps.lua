-- n, v, i, t = mode names -- n = normal, v = visual, i = insert, t = terminal

-- Set highlight on search, but clear on pressing <Esc> in normal mode
vim.opt.hlsearch = true
vim.keymap.set("n", "<Esc>", "<cmd>nohlsearch<CR>")

-- Diagnostic keymaps
vim.keymap.set("n", "[d", vim.diagnostic.goto_prev, { desc = "Go to previous [D]iagnostic message" })
vim.keymap.set("n", "]d", vim.diagnostic.goto_next, { desc = "Go to next [D]iagnostic message" })
vim.keymap.set("n", "<leader>e", vim.diagnostic.open_float, { desc = "Show diagnostic [E]rror messages" })
vim.keymap.set("n", "<leader>q", vim.diagnostic.setloclist, { desc = "Open diagnostic [Q]uickfix list" })

-- Exit terminal mode in the builtin terminal with a shortcut that is a bit easier
-- for people to discover. Otherwise, you normally need to press <C-\><C-n>, which
-- is not what someone will guess without a bit more experience.
--
-- NOTE: This won't work in all terminal emulators/tmux/etc. Try your own mapping
-- or just use <C-\><C-n> to exit terminal mode
vim.keymap.set("t", "<C-x>", "<C-\\><C-n>", { desc = "Exit terminal mode" })

vim.keymap.set("n", "<C-h>", "<C-w><C-h>", { desc = "Move focus to the left window" })
vim.keymap.set("n", "<C-l>", "<C-w><C-l>", { desc = "Move focus to the right window" })
vim.keymap.set("n", "<C-j>", "<C-w><C-j>", { desc = "Move focus to the lower window" })
vim.keymap.set("n", "<C-k>", "<C-w><C-k>", { desc = "Move focus to the upper window" })

vim.keymap.set("n", "<C-n>", ":NvimTreeToggle<CR>", { noremap = true, silent = true })

vim.keymap.set("n", "<Tab>", ":BufferLineCycleNext<CR>", { noremap = true, silent = true })

vim.keymap.set("n", "<S-Tab>", ":BufferLineCyclePrev<CR>", { noremap = true, silent = true })

vim.keymap.set("n", "<leader>x", ":bd<CR>", { noremap = true, silent = true })

-- Allows for moving up visual lines
-- vim.api.nvim_set_keymap('n', 'j', 'gj', { noremap = true })
-- vim.api.nvim_set_keymap('n', 'k', 'gk', { noremap = true })

vim.api.nvim_set_keymap("n", "j", 'v:count ? "j" : "gj"', { noremap = true, expr = true })
vim.api.nvim_set_keymap("n", "k", 'v:count ? "k" : "gk"', { noremap = true, expr = true })

vim.keymap.set("n", "gD", "<cmd>vsplit| lua vim.lsp.buf.definition()<CR>", {})
vim.keymap.set("n", "gd", vim.lsp.buf.definition, {
	desc = "Go to definition",
})

vim.keymap.set("n", "<leader>vs", ":vsplit<CR>", {})
