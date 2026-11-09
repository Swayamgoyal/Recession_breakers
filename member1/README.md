# Member 1: Introduction, Sections 1, 2 and A, Conclusion

Chapter: *The Foreign Exchange Rate*. Introduction to Economics, Monsoon 2026.

Main text: about 1,070 words. Boxes, figures, captions, exercises, notes and references are not counted.

## Files

| File | What it is |
|---|---|
| `draft.md` | The final text in Markdown, with figures in place and the APA 7 reference list. This is the source of truth. |
| `Member1_Sections.pdf` | The same text typeset in LaTeX (7 pages). |
| `Member1_Notes_for_Team.md` | Answers to Member 4's requests, the cross-references, overlaps, chapter-wide issues, a glossary and review questions. |
| `Member1_Fact_Check_List.md` | Every real-world figure in Member 1's sections, with its source and status. |
| `figures/` | Figure M1-1 (photo, CC BY 4.0), Figure M1-2 (diagram), Figure M1-3 (remittances chart). |
| `latex/` | The LaTeX project. Compile `main.tex` with XeLaTeX. `latexmkrc` selects XeLaTeX on Overleaf. Fonts are included so the ₹ sign prints. |
| `source/make_remittances_chart.py` | Script that draws Figure M1-3 from World Bank data. |

## Merging

`latex/main.tex` shows where Sections 3 to 8 go, after Section A and before the Conclusion. Cross-references are written as `\seesec{Title}` in LaTeX and `[see: Title]` in Markdown. Replace them with section numbers after the merge.
