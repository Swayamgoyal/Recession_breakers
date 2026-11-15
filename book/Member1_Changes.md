# Member 1: changes to cut words and tighten the text

**Applies to:** the Introduction, Sections 1, 2 and 3, and the Conclusion in `main.pdf` (15 Nov 2026 build).

**Goal:** Member 1's part falls from about **2,140 words** to about **1,385 words**, counting boxes, captions, figure text and margin notes. That takes about 750 words off the chapter total, or about 790 with the optional diagram change in Section 2.

**How to read the replacement text below**

- `**word**` marks a key term. Use the existing `\keyterm{}` or bold, as the current file does.
- `[n]` marks a citation to reference number *n* in the current reference list. Keep the existing citation command for that source. The key is in Part 4.
- `(see Section n)` should stay as the existing cross-reference command.
- None of the new text contains a semicolon. Please don't add any.

---

## Part 1: Delete these items completely

| # | What to delete | Where | Words saved |
|---|---|---|---|
| 1 | **Exercise box "Dollars in or dollars out?"**, all of items (a) to (g) | End of Section 2, pages 4–5 | about 95 |
| 2 | **The footnote "\* Answers. Supply: (b), (c), (d), (g). Demand: (a), (e), (f)."** and the `*` after "supply of dollars" | Bottom of page 5 | about 12 |
| 3 | **Box "How economists learn from facts: Ravi is one of millions"**, including Figure 3 (remittances chart), its caption, source line and the paragraph under it | Section 2, page 4 | about 130 |
| 4 | **Box "Key points: Questions this chapter answers"** (the five opening questions). The Conclusion's Key points box already covers the same ground. | Introduction, page 1 | about 60 |
| 5 | **The margin note defining FDI and FPI** | Section 2, page 3 | about 30 |
| 6 | **The subheading "Why everyone watches the dollar"** | Section 1 | 5 |
| 7 | **The subheading "Most currency trading is not about trade"** | Section 2 | 7 |
| 8 | **The line "Where next? The balance of payments, monetary policy…"** | End of the Conclusion's Key points box | about 19 |

If the LaTeX uses separate files, items 1 and 3 are the `exercise` and `economistsfacts` environments in the Section 2 file. `figures/remittances.pdf` and `make_remittances_chart.py` are then no longer needed.

---

## Part 2: Replace the text, section by section

### Introduction: Meera's dollar problem

Keep the heading. **Replace all three body paragraphs** with:

```text
In October 2026, Meera, a Class 12 student in Chennai, won a place at a college in the United States. Its first-year fees were US$40,000, the same as a year earlier. Yet in rupees they now cost about ₹2.5 lakh more. The college had not raised its price. The price of the dollar had gone up.

Her uncle Ravi, an electrician in Dubai, saw the other side. The money he sends his parents in Thanjavur every month now arrives as more rupees. One price, two opposite outcomes. This chapter explains what that price is, who sets it and why it keeps moving.
```

**Replace the margin note** ("The fees are hypothetical…") with:

```text
The fees are hypothetical. The rates are real closing rates: ₹88.67 per US$ on 13 October 2025 [1] and ₹95.05 on 15 October 2026 [2]. 40,000 × 6.38 = ₹2,55,200.
```

### 1 What is an exchange rate?

Keep the heading. **Replace all body paragraphs in Section 1**, including the two paragraphs under the deleted subheading, with:

```text
Rupees buy chai in Chennai, but coffee in New York needs dollars and a meal in Dubai needs dirhams. Whenever goods, services or savings cross a border, one currency must be swapped for another. The price of that swap is the **exchange rate**: the price of one currency in terms of another [3]. In India it is set mainly by buyers and sellers in a market, so it changes minute by minute.

Indian banks use the **direct quote**, the number of rupees needed to buy one unit of foreign currency, as in US$1 = ₹95 [4]. The **indirect quote** flips this to ₹1 = US$0.0105. This chapter always uses the direct quote (₹/$), so a bigger number means a weaker rupee (see Section 5).

The rupee is watched mostly against the US dollar, the world's working currency, which was on one side of 89 per cent of all currency trades in April 2025 [6]. Crude oil, India's biggest import, is priced in dollars, and only about 6 per cent of India's exports are invoiced in rupees [7], even though the Reserve Bank of India (RBI) has allowed trade to be settled in rupees since July 2022 [8]. The dollar even reaches the UAE dirham, which has been fixed, or **pegged**, at 3.6725 per US dollar since 1997 [9] (see Section 6). So when a dollar costs more rupees, so does every dirham Ravi sends home.
```

**Replace the Figure 1 caption** with:

```text
Figure 1. Exchange board at Kathmandu airport, January 2023. Each row is a direct quote in Nepalese rupees (NRs). A US dollar costs NRs 127.10 and a UAE dirham, the currency Ravi earns, about NRs 34.
Source: Photograph by Chainwit, Wikimedia Commons, CC BY 4.0, cropped [5].
```

**Replace the "Did you know? Every board hides two prices" box text** with (keep the box and its title):

```text
A bank buys a currency from you at a lower rate and sells it to you at a higher one. Suppose it buys dollars at ₹93.50 and sells them at ₹96.50. Then ₹10,000 buys US$103.63, which sells straight back for only ₹9,689. The missing ₹311 is the bank's earning, the **spread**. Spreads are widest for cash at airport counters.
(The rates are hypothetical.)
```

### 2 The foreign exchange market: who needs dollars and who supplies them?

Keep the heading. **Replace all body paragraphs in Section 2** with:

```text
Currencies are traded in the **foreign exchange (forex) market**, a worldwide electronic network of banks, dealers and large firms with no building and no closing bell [10].

Anyone who must pay abroad needs dollars: importers, students like Meera, travellers, Indians investing abroad and borrowers repaying foreign loans. They make up the **demand for foreign exchange**. Anyone who earns from abroad brings dollars in: exporters like Selvi, whose garment unit in Tiruppur sells T-shirts to American shops, foreign tourists, foreign investors and workers like Ravi. Their **remittances** made India the world's largest recipient in 2025, at US$150.7 billion [12]. Together they make up the **supply of foreign exchange** [3]. Each deal is two purchases at once, because Meera's father buys dollars by selling rupees [10]. The exchange rate is the price at which the two sides match (Figure 2, see Section 4).

Yet most forex trading is not about trade. About US$9.6 trillion changed hands every day in April 2025 [6], so the market turns over a year of world exports (US$33 trillion in 2024 [11]) in under four days. Most of it is investors moving savings. **Foreign direct investment (FDI)** buys a lasting stake of 10 per cent or more in a business, such as a car factory near Chennai, and stays for years. **Foreign portfolio investment (FPI)** buys shares and bonds and can leave in a day, so it can jolt the rupee [10] (see Section 9).

Under the Foreign Exchange Management Act, 1999, only dealers licensed by the RBI, such as banks (**authorised dealers**) and money changers, may deal in foreign currency. The RBI sets the rules and at times buys or sells dollars itself (see Section 7).
```

**Replace the Figure 2 caption** with:

```text
Figure 2. Who wants dollars and who brings them in.
Source: Based on NCERT and Greenlaw et al. [3, 10]
```

**Figure 2 diagram, optional (saves about 45 words):** in `figures/fx_flow.tex`, delete the small grey second line in each of the eight boxes, such as "crude oil, gold, electronics, machines" and "e.g. Meera's college fees". Keep the main labels, such as Importers and Exporters. The new body text already gives the examples.

**Replace the "Case study: Selvi's three-month gamble" box text** with (keep the box and its title):

```text
In October, Selvi sells T-shirts worth US$20,000 to a New York shop that will pay in January. At today's **spot rate**, the rate for a deal settled now, of ₹95, that is ₹19 lakh. If the rupee strengthens to ₹90 by January, she gets only ₹18 lakh and her profit could vanish. So she signs a **forward contract** with her bank, which fixes today a **forward rate** at which the bank will buy her dollars in January. Importers use the same tool against a weaker rupee.
(The figures are hypothetical.)
```

### 3 The rupee's account book: the balance of payments

Keep the heading. **Replace both body paragraphs** with:

```text
Every dollar that enters or leaves India is recorded in the **balance of payments (BoP)**, the record of all economic transactions between a country's residents and the rest of the world over a period such as a year [3]. The **current account** records trade in goods and services, income and transfers such as remittances. The **capital account** records the buying and selling of assets, such as FDI, FPI and foreign loans. When a country spends more foreign currency on its current account than it earns, it runs a **current account deficit (CAD)**, which must be paid for by net capital inflows or by drawing down reserves [3].

India imports far more goods than it exports, mainly oil, gold and electronics. But **invisibles**, which are services such as software, income and transfers such as remittances, brought in a net US$312 billion in 2025-26. That left a CAD of only US$25.2 billion, about 0.6 per cent of GDP [15]. Capital flows did not cover even this, because foreign portfolio investors took out a net US$16.4 billion. So the RBI drew about US$23.6 billion from its reserves (see Section 7).
```

### Conclusion

Keep the heading. **Replace the body paragraph** with:

```text
Now look again at Meera's fees. In 2026, dearer oil raised India's demand for dollars, while foreign investors selling Indian assets cut the supply (see Section 9). The RBI sold dollars from its reserves to slow the rupee's fall but could not stop it, so her bill rose by ₹2.5 lakh and Ravi's family got more rupees for every dirham. An exchange rate is just one price, but so much of India's trade, savings and borrowing passes through it that it reaches almost every household.
```

**Replace the bullets in the "Key points: What this chapter has shown" box** with (keep the box and its title):

```text
• **Why a currency has a price.** The exchange rate is the price of swapping one currency for another (Section 1).
• **Who trades currencies.** Those who pay abroad demand dollars and those who earn from abroad supply them (Sections 2 and 3).
• **What sets the rate.** Demand and supply, shifted by inflation, interest rates, capital flows, oil prices and expectations (Sections 4, 8 and 9).
• **How it is managed.** Since 1993 India has had a managed float, with the RBI using reserves to smooth sharp swings (Sections 6, 7 and 11).
• **Who gains and who loses.** A weaker rupee helps exporters and remittance families but hurts importers, students abroad and dollar borrowers (Sections 5 and 10).
```

---

## Part 3: Follow-on changes elsewhere in the chapter

1. **Figure numbers.** Deleting Figure 3 moves every later figure down by one: Figure 4 becomes Figure 3, and so on up to Figure 11, which becomes Figure 10.
   - If the figures use `\label` and `\ref`, this happens automatically.
   - If any figure number is typed by hand, update these places:
     - Section 4: "Figure 4(a) shows this intersection", "(b) of Figure 4"
     - Section 7: "Figure 5", "(Figure 6)"
     - Section 8: "(Figure 7)"
     - Section 9: "Figure 8 traces the rupee", "(Figure 9a)", "(Figure 9b)"
     - Section 10: "(Figure 10)"
     - Section 11: "(Figure 11)"
2. **Reference list.**
   - Delete reference **13** (Gajbhiye et al., 2025, RBI Bulletin on remittances). It was cited only in the deleted box.
   - Delete reference **14** (World Bank, 2017, remittances decline). Nothing in the chapter cites it now.
   - **Keep reference 12** (World Bank, 2026a). The new Section 2 text cites it for the US$150.7 billion figure.
   - If the list is generated automatically from citations, steps 13 and 14 happen on their own. If it is typed by hand, delete both and renumber the later references and their in-text numbers.
3. **Cross-references into Member 1's sections still work.** Section 9's "Portfolio money is the quickest to leave (see Section 2)" still points to the FPI definition, which stays in Section 2. Section 7 can still use "current account deficit", because Section 3 still defines it.

---

## Part 4: Citation key used above

| [n] | Source |
|---|---|
| 1 | Business Standard (2025b, Oct 13) |
| 2 | HDFC Sky (2026, Oct 15) |
| 3 | NCERT (2007) |
| 4 | Jayadev (2021), CORE |
| 5 | Chainwit (2023), Wikimedia Commons |
| 6 | Bank for International Settlements (2025) |
| 7 | Reserve Bank of India (2026a) |
| 8 | Reserve Bank of India (2022) |
| 9 | Nagraj (2024) |
| 10 | Greenlaw et al. (2022), OpenStax |
| 11 | UNCTAD (2025) |
| 12 | World Bank (2026a) |
| 15 | Reserve Bank of India (2026b) |

---

## Part 5: Word count after the changes (all text counted)

| Part | Before | After |
|---|---|---|
| Title block | 20 | 20 |
| Introduction (body, margin note, box) | 243 | about 130 |
| Section 1 (body, Figure 1 caption, spread box) | 487 | about 345 |
| Section 2 (body, Figure 2 text and caption, Selvi box, margin note, deleted boxes) | 861 | about 485 (about 445 with the optional diagram change) |
| Section 3 | 230 | about 195 |
| Conclusion (body and Key points box) | 296 | about 205 |
| **Member 1 total** | **about 2,140** | **about 1,385** (about 1,345 with the optional diagram change) |

The whole chapter would then come to about 6,620 words (all text counted), down from about 7,370.

Before you recompile:

- Search the whole file for `;` (should find none in Member 1's text).
- Rebuild the PDF and check that pages 1–5 have no gaps left by the deleted boxes.
