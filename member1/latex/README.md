# Foreign Exchange Rate chapter — Member 1 sections (Overleaf project)

## Put it in Overleaf
1. In Overleaf: **New Project → Upload Project** and choose `fx_m1_overleaf.zip`
   (or, in your existing project, **Upload** the files keeping the same folders).
2. **Menu → Compiler → XeLaTeX** (the `latexmkrc` file already sets this, but check).
3. Recompile. `main.tex` is the file to compile.

## What's inside
| File | What it is |
|---|---|
| `main.tex` | Chapter shell. Members 2–4 add `\input{...}` lines where marked. |
| `fxstyle.sty` | Shared look: colours, fonts, the 7 allowed box types, key-term margin notes, `[see: ...]` cross-refs. |
| `sections/m1_intro.tex` | Introduction: Meera's dollar problem |
| `sections/m1_sec1_exchange_rate.tex` | 1 What is an exchange rate? |
| `sections/m1_sec2_forex_market.tex` | 2 The foreign exchange market |
| `sections/m1_conclusion.tex` | Conclusion |
| `figures/fx_flow.tex` | Figure M1-2, TikZ flow diagram (editable text) |
| `figures/remittances.pdf/.png` + `make_remittances_chart.py` | Figure M1-3, World Bank data chart and the script that draws it |
| `images/kathmandu_board.jpg` | Figure M1-1, CC BY 4.0 photo (credit is in the caption) |
| `fonts/` | Source Serif 4 and Source Sans 3 (SIL Open Font Licence), bundled so ₹ prints everywhere |

## Macros other members can use
- `\keyterm{term}{one-line definition}` — bold term + definition in the margin.
- `\seesec{Section title}` — cross-reference placeholder, converted to numbers at merge.
- Boxes: `didyouknow`, `workedexample`, `exercise`, `casestudy`, `economistsdisagree`, `economistsfacts`, `keypoints` — each takes its title as the argument.
- `\answers{...}` for answers at the foot of a box, `\figsource{...}` for source lines.
- Figure numbers print as "M1-1, M1-2…"; delete the `\renewcommand{\thefigure}` line in `fxstyle.sty` at merge.

## Word count (main text only; boxes, captions, margin notes excluded)
Introduction 148 · Sections 1–2: 305 · Section 3: 382 · Conclusion 82 · **Total about 920** (+ about 25 words of headings).
