# Member 1: notes for the team

This file covers what Members 2, 3 and 4 need from Member 1. It also lists issues for the whole chapter that we should settle before we merge.

## 1. What Member 1's part contains

| Part | Title | Main-text words |
|---|---|---|
| Introduction | Meera's dollar problem | about 150 |
| Section 1 | What is an exchange rate? | about 290 |
| Section 2 | The foreign exchange market: who needs dollars and who supplies them? | about 330 |
| Section A | The rupee's account book: the balance of payments | about 210 |
| Conclusion | (no subtitle, closes the whole chapter) | about 95 |
| **Total** | | **about 1,070** |

The word counts leave out boxes, figures, captions, the exercise, notes and references.

Boxes and figures: Figure M1-1 (exchange board photo), the spread box, Figure M1-2 (who wants dollars), the Selvi forward-contract case study, the remittances box with Figure M1-3, the "Dollars in or dollars out?" exercise and the Khan Academy video box.

## 2. Answers to Member 4's requests

**Current account deficit.** Section A defines balance of payments, current account, capital account, current account deficit (CAD) and invisibles. Section 7 can use "current account deficit" without defining it again.

**Characters.** Please use these descriptions everywhere.

- **Meera.** A Class 12 student in Chennai. A US college has offered her a place. First-year fees are US$40,000. Her father buys the dollars from his bank.
- **Ravi.** Meera's uncle. An electrician in Dubai who earns UAE dirhams. Every month he sends part of his salary to his parents in Thanjavur.
- **Selvi.** Runs a garment unit in Tiruppur that exports T-shirts to shops in the United States.

**Video link.** Khan Academy, *Currency exchange introduction*, KA Macroeconomics Class 12:
https://www.khanacademy.org/economics-finance-domain/class-12-macroeconomics/x29cdf3f0a895464f:open-economy-macroeconomics/x29cdf3f0a895464f:foreign-exchange-market/v/currency-exchange-introduction

**References.** All 16 are in APA 7 at the end of `draft.md`. Each one has a URL. They are ready to merge into one list.

## 3. Cross-references used

Member 1's text points to these sections by title. If you rename a section, please tell Member 1.

| Placeholder in Member 1's text | Owner |
|---|---|
| [see: Appreciation and depreciation: who wins, who loses?] | Member 2 |
| [see: How the exchange rate is determined: demand and supply] | Member 2 |
| [see: What moves the rupee?] | Member 4 (used twice) |
| [see: The RBI and India's foreign exchange reserves] | Member 3 (used twice) |

In LaTeX these are `\seesec{...}`. After the merge, replace each one with a real section number (for example "see Section 4").

## 4. Overlaps that Member 1 has removed or taken over

- **Section B (spread and forward contracts).** Member 2's draft does not include it. Member 1 already covers both ideas: the spread box in Section 1 and the Selvi forward-contract case study in Section 2. Member 2 does not need to write Section B. If Member 2 does write it, Member 1 will remove these two boxes.
- **Foreign investors pulling money out.** Member 4's Selvi box and Section 7 explain how FPI leaving India weakens the rupee. Member 1 removed a sentence that said the same thing. Section 2 now only defines FDI and FPI and points to Section 7.
- **Selvi's numbers.** Member 4's Selvi box uses a US$20,000 order at ₹85 and ₹90. Member 1's case study uses US$20,000 at ₹95 and ₹90. Member 1's numbers match the 2026 rate given in the Introduction. Member 4, please consider changing ₹85 to ₹95. If you keep ₹85, the two boxes still work, but readers may notice the mismatch.

## 5. Issues for the whole chapter

1. **Word limit.** The guidelines allow 4,000 words at most. Our main text now comes to about 5,700 (Member 1 about 1,070, Member 2 about 1,100, Member 3 about 2,300, Member 4 about 1,360). We need to cut about 1,700 words. Member 3's part is the longest. Suggestion: move some of Member 3's explanation into boxes, and have each member cut repeated definitions.
2. **Ravi error in Member 2's draft.** Member 2 writes "Ravi, whose uncle works in Dubai". Ravi is Meera's uncle and Ravi himself works in Dubai. Please change it to "Meera's uncle Ravi, who works in Dubai".
3. **Placeholders in Member 3's files.** `QUESTION CONTENT` and `\DidYouKnow` are still in the text. They must be filled in or removed before submission.
4. **India's reserves in 1991.** Member 3 writes "two weeks of imports". Member 4 writes "a few weeks". The usual figure is about two to three weeks of imports (reserves fell to about US$1.1 billion in June 1991). We should agree on one wording. Suggestion: "enough for only about two weeks of imports", with Member 3's source cited in both places.
5. **Formats.** Member 1 uses Markdown plus LaTeX, Member 2 PDF only, Member 3 Markdown plus LaTeX, Member 4 Word. Member 1's LaTeX in `latex/` already has the shared style file, all the boxes and the place where the other sections slot in (see `latex/main.tex`). It would be easiest to merge everything there.
6. **Opening line of Member 2's section.** Member 2 starts with "In Section 2, we saw…". Member 1's forex market section is still Section 2, so this works. If the numbering changes, please update it.
7. **Direct quotes everywhere.** Member 1 always writes rates as rupees per dollar (₹/$), so a bigger number means a weaker rupee. All members should follow this, especially on graph axes.

## 6. Glossary of Member 1's key terms

| Term | Meaning |
|---|---|
| Exchange rate | The price of one currency in terms of another, for example ₹95 per US dollar. |
| Direct quote | The price of one unit of foreign currency in home currency (US$1 = ₹95). Used in this chapter. |
| Indirect quote | How much foreign currency one unit of home currency buys (₹1 = US$0.0105). |
| Spread | The gap between the rate at which a bank sells a currency and the rate at which it buys it. It is the bank's earning. |
| Foreign exchange (forex) market | The worldwide network of banks, dealers and firms where currencies are traded. |
| Demand for foreign exchange | Dollars wanted by importers, students and travellers abroad, Indians investing abroad and people repaying foreign loans. |
| Supply of foreign exchange | Dollars brought in by exporters, workers abroad who send remittances, foreign tourists and foreign investors. |
| Remittances | Money that people working abroad send home. |
| Foreign direct investment (FDI) | Buying a lasting stake in a business (10 per cent or more), such as a factory. It stays for years. |
| Foreign portfolio investment (FPI) | Buying shares and bonds. It can leave quickly. |
| Authorised dealer | A bank licensed by the RBI under FEMA 1999 to deal in foreign currency. |
| Spot rate | The exchange rate for a deal settled now. |
| Forward rate | An exchange rate agreed today for a deal on a future date. |
| Forward contract | An agreement with a bank to exchange currency at a fixed rate on a future date. |
| Balance of payments (BoP) | The record of all economic transactions between a country's residents and the rest of the world over a period. |
| Current account | The part of the BoP that records trade in goods and services, income and transfers. |
| Capital account | The part of the BoP that records the buying and selling of assets, such as FDI, FPI and loans. |
| Current account deficit (CAD) | When a country spends more foreign currency on its current account than it earns. |
| Invisibles | Current-account items other than goods: services, income and transfers. |

## 7. Review questions for the end-of-chapter set (with answers)

Any member who builds the final question set can use these.

1. **The rate moves from ₹90 to ₹95 per dollar. Has the rupee become stronger or weaker? Explain.**
   Weaker. Each dollar now costs more rupees, so each rupee buys fewer dollars.
2. **Write the direct quote "US$1 = ₹80" as an indirect quote.**
   ₹1 = US$0.0125 (1 ÷ 80).
3. **A money changer buys dollars at ₹94 and sells them at ₹96. What is the spread on US$100?**
   ₹200 (₹9,600 − ₹9,400).
4. **Give two sources of demand for dollars and two sources of supply of dollars in India.**
   Demand: importers of oil or gold, students paying foreign fees, Indian tourists abroad, Indians investing abroad. Supply: exporters, remittances, foreign tourists in India, FDI and FPI inflows.
5. **Why does a fall in the rupee against the dollar mean more rupees for Ravi, even though he is paid in dirhams?**
   The dirham is fixed at 3.6725 per US dollar. When the dollar costs more rupees, so does the dirham.
6. **What is the difference between FDI and FPI, and which is more likely to cause sudden moves in the rupee?**
   FDI buys a lasting stake in a business and stays for years. FPI buys shares and bonds and can leave in a day. FPI is more likely to cause sudden moves.
7. **Why might Selvi sign a forward contract?**
   To fix today the rate at which she will sell her dollars later, so that a stronger rupee does not wipe out her profit.
8. **India imports far more goods than it exports. Why is its current account deficit still small?**
   Large net earnings from invisibles, mainly software exports and remittances, cover most of the trade gap.
9. **How can a country pay for a current account deficit?**
   With a net inflow on the capital account (such as FDI, FPI or loans) or by drawing down its foreign exchange reserves.
