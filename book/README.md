# The Foreign Exchange Rate: merged chapter

This folder is the whole chapter, all four members, in one LaTeX book. `main.pdf` is the compiled result.

## Build it

1. `python source/make_charts.py` redraws the data charts (only needed if the data or chart code changes).
2. `python source/build_book.py` regenerates the glossary and `word_count.md`.
3. `latexmk main.tex` compiles with XeLaTeX (`latexmkrc` selects it). On Overleaf, upload the folder and set **Menu → Compiler → XeLaTeX**.

## What's where

| Path | Contents |
|---|---|
| `main.tex` | The chapter shell; one `\input` per section |
| `fxstyle.sty` | Shared look (Member 1's style): fonts, colours, margin key terms, the 7 box types, diagram styles |
| `sections/s00`–`s12` | Introduction, Sections 1–11 and Conclusion; each file's header says who wrote it and what changed |
| `sections/e1`–`e4` | Glossary (generated), review questions, further learning, references |
| `figures/` | TikZ diagrams (`ds_*.tex`, `fx_flow.tex`, `imported_inflation.tex`) and chart PDFs |
| `source/` | Chart and build scripts, plus the downloaded data (FRED, World Bank, The Economist) |
| `CHANGELOG.md` | Every change made to each member's text at the merge |
| `word_count.md` | Main-text words per section and member |

## Writing rules (unchanged from the team style sheet)

- **Key terms:** `\keyterm{term}{one-line definition}` makes the term bold and puts the definition in the margin. The glossary is built from these, so define each term once.
- **Cross-references:** `\seesec{sec:label}` prints "(see Section N)" and `\secref{sec:label}` prints "Section N".
- **Boxes:** use only these: `didyouknow`, `workedexample`, `exercise`, `casestudy`, `economistsdisagree`, `economistsfacts`, `keypoints`.
