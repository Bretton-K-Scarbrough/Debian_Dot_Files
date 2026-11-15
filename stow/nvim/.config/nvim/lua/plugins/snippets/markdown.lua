local ls = require("luasnip")
local s = ls.snippet
local sn = ls.snippet_node
local t = ls.text_node
local i = ls.insert_node
local f = ls.function_node
local d = ls.dynamic_node
local fmt = require("luasnip.extras.fmt").fmt
local fmta = require("luasnip.extras.fmt").fmta
local rep = require("luasnip.extras").rep
local s = ls.snippet
local t = ls.text_node

return {
	s({ trig = "frac" }, {
		t("\\frac{"),
		i(1),
		t("}{"),
		i(2),
		t("}"),
	}),

	s(
		{ trig = "vec" },
		fmta("\\vec{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "wedge" },
		fmta("\\wedge<>", {
			i(1),
		})
	),
	s(
		{ trig = "m" },
		fmta("$<>$", {
			i(1),
		})
	),

	s(
		{ trig = "mc" },
		fmta(
			[[$$
<>
$$]],
			{
				i(1),
			}
		)
	),

	s(
		{ trig = "int" },
		fmta("\\int_{<>}^{<>}d<>", {
			i(1, "a"),
			i(2, "b"),
			i(3, "x"),
		})
	),

	s(
		{ trig = "exp" },
		fmta("e^{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "der" },
		fmta("\\frac{d}{d<>}", {
			i(1, "x"),
		})
	),

	s(
		{ trig = "E" },
		fmta("\\cdot 10^{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "sq" },
		fmta("\\sqrt{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "text" },
		fmta("\\text{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "tt" },
		fmta("\\texttt{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "ol" },
		fmta("\\overline{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "ul" },
		fmta("\\underline{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "t" },
		fmta("\\text{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "div" },
		fmta("\\nabla \\cdot <>", {
			i(1),
		})
	),

	s(
		{ trig = "curl" },
		fmta("\\nabla \\times <>", {
			i(1),
		})
	),

	s({ trig = "grad" }, fmta("\\nabla ", {})),

	s(
		{ trig = "sub" },
		fmta("\\_{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "sup" },
		fmta("\\^{<>}", {
			i(1),
		})
	),

	s(
		{ trig = "set" },
		fmta("\\{<>\\}", {
			i(1),
		})
	),

	s({ trig = "dot" }, fmta("\\cdot ", {})),

	s(
		{ trig = "begin" },
		fmta(
			[[\begin{<>}

\end{}]],
			{
				i(1),
			}
		)
	),

	s(
		{ trig = "cases" },
		fmta(
			[[\begin{cases}
  <>
\end{cases}]],
			{
				i(1),
			}
		)
	),

	s(
		{ trig = "align" },
		fmta(
			[[\begin{align}
  <>
\end{align}]],
			{
				i(1),
			}
		)
	),
	s(
		{ trig = "bmat" },
		fmta(
			[[\begin{bmatrix}
  <>
\end{bmatrix}]],
			{
				i(1),
			}
		)
	),

	s(
		{ trig = "lr" },
		fmta("\\left(<>\\right)", {
			i(1),
		})
	),

	s({ trig = "real" }, fmta("\\mathbb{R}", {})),

	s({ trig = "complex" }, fmta("\\mathbb{C}", {})),

	s({ trig = "integers" }, fmta("\\mathbb{Z}", {})),

	s({ trig = "naturals" }, fmta("\\mathbb{N}", {})),

	s({ trig = "partial" }, fmta("\\partial", {})),

	s({ trig = "forall" }, fmta("\\forall", {})),

	s({ trig = "ra" }, fmta("\\rightarrow", {})),

	s({ trig = "fat" }, fmta("\\bullet", {})),

	s({ trig = "antidual" }, fmta("^\\unicode{x2606}", {})),
	s({ trig = "dual" }, fmta("^{\\star}", {})),

	s(
		{ trig = "bm" },
		fmta("\\boldsymbol{<>}", {
			i(1),
		})
	),
}
