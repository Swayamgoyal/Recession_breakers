# What changed in each member's work at the merge

The merged chapter is in `book/`. Every member's original files are untouched in `member1/` to `member4/`. This list records every change made to each person's text, so that each of you can check your own section and say if something should go back.

In the `.tex` files, sentences added at the merge carry a `% [added at merge]` comment. Each section file also lists its changes in its header comment.

## Decisions agreed for the whole book

| Topic | Decision |
|---|---|
| Format | LaTeX in Member 1's style (`fxstyle.sty`), compiled with XeLaTeX |
| Word limit | Agreed at merge: 5,000 words of main text. Project guidelines say 4,000 maximum. Main text after the 15 Nov review: **4,660** (see `word_count.md`) |
| Section B | Dropped. Member 1's spread box and forward-contract case study already cover it |
| Numbering | Sections 1–11 in order. Figures and tables numbered 1, 2, 3… Cross-references read "(see Section 4)" |
| Notation | ₹ with lower-case "rupee" and "dollar", "₹82 per US dollar" in text, "per cent" in prose, % in tables |
| 1991 reserves | "about two weeks of imports" everywhere |
| End matter | Generated glossary, review questions, further learning, one combined APA reference list |

## Section map

| New | Old | Owner |
|---|---|---|
| Introduction, 1, 2 | Introduction, 1, 2 | Member 1 |
| 3 The balance of payments | A | Member 1 |
| 4 Demand and supply | 3 | Member 2 |
| 5 Appreciation and depreciation | 4 | Member 2 |
| 6 Exchange rate systems | 5 | Member 3 |
| 7 The RBI and India's reserves | C | Member 3 |
| 8 Real exchange rates and PPP | 6 | Member 3 |
| 9 What moves the rupee? | 7 | Member 4 |
| 10 Why exchange rates matter | 8 | Member 4 |
| 11 Currency crises in South Asia | D | Member 4 |
| Conclusion | Conclusion | Member 1 |

## Member 1 (Introduction, Sections 1–3, Conclusion)

The text is unchanged. Only these mechanical edits were made:
- `\seesec{Title}` cross-references now point to section numbers.
- Section A became numbered Section 3.
- The draft "M1-" figure numbering was removed, so figures are numbered through the whole book.
- Citation years gained letters because the book now has more than one source per author and year:
  - "World Bank (2026)" became "World Bank (2026a)".
  - "Business Standard (2025)" in the Introduction became "Business Standard (2025b)".
- The remittances chart (Figure 3) was redrawn from Member 1's own script at a smaller size, so its text matches the other charts. The data and design are unchanged.
- Member 1's 9 review questions and Khan Academy video went into the end matter as written.

## Member 2 (Sections 4 and 5)

Member 2's sentences are kept. Changes:
- **Fixed:** "Ravi, whose uncle works in Dubai" now reads "Meera's uncle Ravi, who works in Dubai".
- **Added (Section 4):**
  - a paragraph on why demand slopes down and supply slopes up;
  - a paragraph on how excess demand and excess supply push the rate back to equilibrium;
  - two sentences on shifts versus movements along a curve.

  Later sections rely on these ideas.
- **Added (Section 5):** two sentences defining devaluation and revaluation, which Sections 6, 9 and 11 use.
- **Key terms:** equilibrium exchange rate, excess demand, excess supply, depreciation, appreciation, devaluation and revaluation now have margin definitions.
- **Notation:** "₹82/$" became "₹82 per US dollar", and "In Section 2" now uses a live cross-reference.
- **Figure 4 (was Figure 3.1):** redrawn in the shared style, on a white background, with the ₹82, ₹86 and ₹79 values from the text marked on the axes. It keeps the same three panels.
- **Table 1:** the winners-and-losers table now uses the book's table style, with the same content.

## Member 3 (Sections 6, 7 and 8)

Member 3's sentences are kept wherever possible. The main text was trimmed from about 2,300 to about 1,180 words, mostly by moving material into boxes.

**Section 6:**
- **Opening line:** "how are exchange rates actually determined?" became "does the market always set the rate?", because Section 4 has already covered how the rate is determined.
- **Pros and cons:** the pros and cons of each system moved into a "When economists disagree: Fixed or floating?" box, which the team plan asked for. The text is Member 3's own.
- **Box types:**
  - "Think about it" became an Exercise box ("Spot the switch"), with an answer added.
  - The history box is now a Case study box.
- **Facts corrected:**
  - **1947–71:** the rupee was about ₹3.31 per dollar at first, ₹4.76 after the 1949 sterling devaluation, and ₹7.50 after India's June 1966 devaluation. The 1966 devaluation was missing.
  - **1991 gold:** about 47 tonnes were pledged with the Bank of England and the Bank of Japan, after 20 tonnes had been sold abroad with an option to buy them back. The draft said 67 tonnes went to the two banks. Cited to Business Standard (2013).
  - **1991 reserves:** "barely two weeks" became "only about two weeks", to match the book-wide wording.
- **Figure 5 (timeline):** redrawn with 8 stages, now including 1949 and 1966, and the rupee's rate at each stage.

**Section 7:**
- **Did you know box:**
  - Wikipedia and Deccan Chronicle were replaced with RBI (2026c): US$682 billion on 29 May 2026, about 11 months of import cover.
  - World Bank figures were added: US$5.6 billion in 1990 and US$700 billion in 2025.
  - The "US$1.2 billion" figure was dropped because sources disagree on it; the text keeps "about two weeks of imports".
- **Figure 6 (reserves chart):** rebuilt from the full World Bank annual series for 1990–2025, which has 36 years against 10 points before. The "1,991" year-label bug and the cut-off label are gone.
- **New Figure 7:** RBI intervention shown on the demand-and-supply diagram.
- **Key terms:** foreign exchange reserves, SDR, import cover and intervention now have margin definitions.

**Section 8:**
- **Maharaja Mac box:** the undervaluation was corrected from "over 40%" to about 53% (₹38.6 against ₹81.7). The source is now The Economist's own Big Mac data.
- **GNI box:** updated to World Bank 2025 figures ($2,760 nominal, $11,600 PPP, about 4.2 times). The draft's $9,700 was the 2023 PPP figure. Macrotrends was removed as a source.
- **New Figure 8:** Member 3's worked example drawn as a bar chart.
- **Key terms:** nominal exchange rate, real exchange rate and PPP now have margin definitions.

**Throughout:** "Rs." became "₹", "Rupee" and "Dollar" became lower case, and "%" became "per cent" in prose.

**New review questions:** Members 2 and 3 supplied no questions, so 5 new ones (questions 10–14) were written for Sections 4–8.

## Member 4 (Sections 9, 10 and 11)

- **Selvi box:** changed from ₹85 → ₹90 to ₹90 → ₹95 to match Member 1's ₹95. It is now a Case study box, with one added sentence linking it to Member 1's forward-contract case study.
- **Portfolio money:** the sentence repeating Member 1's "can leave within a day" now just points to Section 2.
- **1991:** "a few weeks" became "about two weeks". The devaluation size now matches Section 6 ("about 18–20 per cent").
- **India's reserves:** "about US$700 billion in April 2026" became "about US$682 billion in May 2026, enough for about 11 months of imports", the same figure and source as Section 7.
- **Figures:** all redrawn in the shared style (Source Sans font, chapter colours).

## Second pass: correctness and flow check (10 November 2026)

- **Conclusion (Member 1):** the paragraph is unchanged. A "Key points: What this chapter has shown" box was added below it. It answers the five questions from the Introduction and points to the next topics, as the plan asks. Boxes don't count toward the word limit.
- **Section 2 (Member 1):** the "Watch and learn" box was removed, because its Khan Academy video is already first in Further learning. This also breaks up a run of four boxes in a row.
- **Section 4 (Member 2):** added a "Draw the shift" exercise with three scenarios and answers, so students practise the model before Section 9 uses it.
- **Section 5 (Member 2):** added three rows to Table 1 (foreign tourists in India, Indian tourists abroad, firms with dollar loans). These are the groups the plan listed, and they set up the debt point in Section 10.
- **Section 6 (Member 3):**
  - The basket sentence now says the RBI did not disclose the basket's make-up. The unconfirmed list of five currencies was removed.
  - Added a "Did you know? A fixed rate next door" box on Nepal's peg (1.6 Nepalese rupees per Indian rupee since 1993, The Kathmandu Post, 2026) and Bhutan's one-for-one peg. The Bhutan peg has no citation; add the Royal Monetary Authority of Bhutan as a source if you can.
- **Table 3 (Member 4):** India's 1991–92 inflation is now "13.7% (wholesale prices)", cited to the RBI Handbook of Statistics, replacing "about 14%".

## Third pass: review highlights from Rahul and Kris (15 November 2026)

Made from the comments in `eco_porject.pdf` (51 highlights). The pre-review book is saved in `old_files/book_before_review_edits_2026-11-15/`. Sentences changed in this pass carry a `% [review 15 Nov 2026]` comment where a whole item was removed.

**Book-wide rules**
- **Citations:** author-date citations such as "(Reserve Bank of India [RBI], 2026a)" are now superscript numbers (`\cite{key}`), so they add no words. The reference list is numbered in order of first citation. APA entries live in `source/references.tex`, and `source/number_references.py` writes `sections/e4_references.tex`, leaving out sources no longer cited (Business Standard 2025a, RBI n.d., Khan Academy, which stays in Further learning).
- **Margin notes:** dropped wherever the sentence already defines the term (new `\defterm`). Margin notes stay only for FDI, FPI, export competitiveness and IMF programme, plus a one-line note on the interest rate differential (`\termnote`).
- **Glossary:** now lists only the terms the text does not define in its own sentence (4 terms).
- **Answers:** every box's answer is now a page-foot note marked *, †, ‡ (restarting on each page), not a line under the question.
- **Semicolons:** removed everywhere in the text, boxes, captions, tables and end matter.
- **Figure sources:** "Drawn by the authors" and "values are hypothetical" source lines removed. Data sources shortened to one line with a citation number.

**By section**
- **1 (M1):** "foreign trade" now reads "payments for their imports and exports". The dirham sentence now says this is a peg (see Section 6). RBI is spelt out once.
- **2 (M1):** the demand-side list now gives importers as the example and points to Figure 2. The supply side keeps Selvi and Ravi. The FDI sentence no longer repeats its margin note. FPI: "it can leave" became "this investment can leave". Remittances question (a) removed, (b) kept. Figure 2: the "the price that clears it: ₹ per US dollar" label removed.
- **3 (M1):** the "software exports and remittances earn so much" sentence was reworded.
- **4 (M2):** the two "increase in demand/supply" subsections were compressed into one paragraph each. The "other things remain constant" sentences were removed. "Draw the shift" was rewritten so both curves move in every case: one sure depreciation, one case where the answer depends on which shift is bigger, and one sure appreciation.
- **6 (M3):** the four margin notes were removed, and the list's definitions now use their wording.
- **7 (M3):** "Did you know? From crisis to confidence" removed (it repeated the chart and Section 11).
- **9 (M4):** Figure 10 caption: "the rupee has depreciated" is now explained as "each dollar now costs more rupees, which is exactly what a depreciation of the rupee means". The economics is unchanged.
- **10 (M4):** Selvi box cut to its first paragraph (the Tiruppur fact and the "not pure profit" paragraph removed). The lead-in now reads "The story of Selvi's unit shows how this works." "Now you try" removed from the oil worked example.
- **11 (M4):** Table 3 (three crises compared) removed.

**Word version:** `eco_project.docx` is built from the LaTeX by `source/build_docx.py`. Boxes become shaded Word styles, answers become Word footnotes, and margin notes become small "Key Term" paragraphs. Edit it by hand if needed, but changes made only in Word won't flow back into the LaTeX.
