"""Builds the Member 4 section packet (Sections 7, 8 and D) as a Word file.

Run:  python build_docx.py   (run build_figures.py first if the figures changed)

All chapter text lives in the CONTENT lists below, so wording can be edited
here and the document rebuilt. Markup inside strings:
    **term**   bold (key term on first use)
    *text*     italic
    [see: …]   cross-reference to another member's section (converted at merge)
"""
import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = Path(__file__).resolve().parent
FIG = HERE.parent / "figures"
OUT = HERE.parent / "Member4_Sections_7_8_D.docx"

NAVY = RGBColor(0x1F, 0x3A, 0x5F)
ORANGE = RGBColor(0xD9, 0x82, 0x2B)
GREEN = RGBColor(0x4C, 0x8B, 0x4A)
GREY = RGBColor(0x6B, 0x72, 0x80)
BODY_FONT, HEAD_FONT = "Georgia", "Segoe UI"

FRED_INR = ("Board of Governors of the Federal Reserve System (2026a), Indian rupees to "
            "U.S. dollar spot exchange rate [EXINUS], monthly averages, retrieved from FRED, "
            "Federal Reserve Bank of St. Louis, 1 November 2026.")

# ---------------------------------------------------------------------------
# CONTENT
# ---------------------------------------------------------------------------
SECTION_7 = {
    "number": "7",
    "title": "What moves the rupee?",
    "budget": 450,
    "blocks": [
        ("p", "Newspapers report the rupee's movements almost every day: 'Rupee falls 30 paise "
              "against the dollar'. Behind each such headline sits the model from [see: How the "
              "exchange rate is determined: demand and supply]. Whenever the rupee moves, ask one "
              "question: did something change the demand for dollars, the supply of dollars, or both?",
         None),
        ("p", "Figure M4-1 traces the rupee since 1991. The line climbs from about ₹18 per US dollar "
              "to about ₹95, a level first crossed in 2026 (Shivalkar, 2026). Long, quiet stretches "
              "are broken by sudden jumps, and each jump has a story behind it.",
         None),
        ("fig", "Fig_M4-1_rupee_per_dollar_1991_2026.png", "M4-1",
         "The rupee against the US dollar, January 1991 to September 2026",
         "Each point is the average exchange rate for one month. A rise in the line means it takes "
         "more rupees to buy one dollar, so the rupee has weakened. The shaded bands, numbered 1 to 6, "
         "mark six sharp falls in the rupee. The box 'Reading the rupee's history' asks you to "
         "identify them.",
         FRED_INR),
        ("p", "The slow part of the climb is mainly about inflation. Prices in India have usually "
              "risen faster than in the United States, which slowly makes Indian goods dearer for "
              "foreign buyers and American goods cheaper for Indians [see: Nominal and real exchange "
              "rates, and purchasing power parity]. "
              "Fewer dollars come in through "
              "exports, more are needed for imports, and the rupee drifts down year after year.",
         None),
        ("p", "The sudden jumps are usually about money crossing borders. When foreigners buy Indian "
              "shares, bonds or businesses, dollars flow in; when they sell, dollars flow out. These "
              "movements are called **capital flows**. Portfolio investors can sell and leave within "
              "a day, which is why they matter so much for short-run swings.",
         ("Capital flows", "Money that moves between countries to buy or sell financial assets, "
                           "such as shares and bonds, or real assets, such as factories.")),
        ("p", "What makes this money move? Very often, interest rates. Investors compare what they "
              "can earn on an American government bond with what they can earn on an Indian one. The "
              "gap between the two is the **interest rate differential**. When the US Federal Reserve "
              "raises its interest rate, the gap narrows. Foreign investors sell Indian assets and "
              "take their dollars home, and the supply of dollars shifts to the left (Figure M4-2b). "
              "This is why a decision taken in Washington is front-page news in Mumbai.",
         ("Interest rate differential", "The difference between the interest rates paid in two "
                                        "countries. Funds tend to move towards the higher return, "
                                        "after allowing for risk.")),
        ("p", "Crude oil is the other big mover. India imports about 88 per cent of the crude oil it "
              "uses (Petroleum Planning & Analysis Cell [PPAC], 2025). When the world price of oil "
              "rises, refiners need more dollars to buy the same number of barrels, and the demand "
              "for dollars shifts to the right (Figure M4-2a). A widening current account deficit "
              "[see: The rupee's account book: the balance of payments] has a similar effect.",
         None),
        ("fig", "Fig_M4-2_two_shocks_dollar_market.png", "M4-2",
         "Two shocks in the market for US dollars (hypothetical numbers)",
         "(a) A rise in the world price of oil. 1. The market starts at E₀, where demand D₀ meets "
         "supply S at ₹85 per dollar. 2. Oil now costs more, so refiners want more dollars at every "
         "exchange rate. Demand shifts right to D₁. 3. At ₹85 there is excess demand for dollars, "
         "and buyers bid the price up. 4. The new equilibrium is E₁ at ₹90: the rupee has "
         "depreciated and more dollars change hands.\n"
         "(b) A rise in US interest rates. 1. Start again at E₀, ₹85 per dollar. 2. Foreign "
         "investors move funds to the United States, so fewer dollars are offered in India at every "
         "exchange rate. Supply shifts left to S₁. 3. The new equilibrium is E₁ at ₹89: the rupee "
         "has depreciated and fewer dollars change hands.",
         "Hypothetical figures drawn by the authors. To be redrawn in the common figure template "
         "[see: How the exchange rate is determined: demand and supply]."),
        ("p", "Markets also look ahead. If traders expect the rupee to fall, importers rush to buy "
              "dollars today and exporters hold on to the dollars they already have. Buying or "
              "selling a currency to profit from its expected future price is called **speculation**. "
              "It can turn a fear into a fact: the rupee falls partly because so many people acted "
              "on the belief that it would.",
         ("Speculation", "Buying or selling an asset, such as a currency, in the hope of profiting "
                         "from a change in its price.")),
        ("p", "Real episodes usually mix several of these forces. In the global financial crisis of "
              "2008 and the COVID-19 panic of 2020, investors everywhere fled to the safety of the US "
              "dollar. India caused neither crisis, yet the rupee fell both times. Table M4-1 sums up "
              "the forces, and the box that follows asks you to read the rupee's history for yourself.",
         None),
        ("table", "M4-1", "What moves the rupee: a summary",
         ["What happens", "Effect in the market for dollars", "₹/$ rate", "Rupee"],
         [
             ["Inflation in India runs ahead of US inflation", "Demand rises and supply falls, slowly, over years", "Rises", "Depreciates"],
             ["US interest rates rise", "Supply shifts left as foreign investors take money home", "Rises", "Depreciates"],
             ["Foreign investors pour money into India", "Supply shifts right", "Falls", "Appreciates"],
             ["World crude oil price rises", "Demand shifts right", "Rises", "Depreciates"],
             ["Current account deficit widens", "Demand for dollars runs ahead of supply from trade", "Rises", "Depreciates"],
             ["Traders expect the rupee to fall", "Demand shifts right and supply shifts left", "Rises", "Depreciates"],
             ["Global panic ('flight to safety')", "Supply shifts left as money leaves emerging economies", "Rises", "Depreciates"],
         ],
         "Each change is assumed to happen on its own, with everything else held constant. The "
         "opposite change has the opposite effect.",
         None),
        ("box", "How economists learn from facts", "Reading the rupee's history", [
            "Figure M4-1 marks six sharp jumps in the price of the dollar, numbered 1 to 6. Each "
            "matches one of the events below, which are listed in no particular order.",
            "A. The US Federal Reserve raises interest rates at its fastest pace in four decades, "
            "while war in Ukraine pushes up oil prices.",
            "B. India, with reserves for only a few weeks of imports, devalues the rupee.",
            "C. Conflict in West Asia sends crude oil above $110 a barrel, and foreign investors "
            "sell Indian assets.",
            "D. A giant American investment bank collapses and a global financial crisis spreads.",
            "E. The US central bank hints that it will soon slow its support for the American "
            "economy, and investors pull money out of emerging markets.",
            "F. A new virus shuts down economies around the world.",
            "1. Match each number to an event. 2. For each, say whether the main change was in the "
            "demand for dollars, the supply of dollars, or both. 3. One event does not fit the "
            "demand and supply story. Which one, and why? (Hint: [see: Exchange rate systems: "
            "fixed, flexible and managed].)",
        ]),
    ],
}

SECTION_8 = {
    "number": "8",
    "title": "Why exchange rates matter for India",
    "budget": 350,
    "blocks": [
        ("p", "You have already met the winners and losers from a change in the rupee [see: "
              "Appreciation and depreciation: who wins, who loses?]. Here we follow those effects "
              "through the wider economy. "
              "Whether you gain or lose depends on whether you earn dollars, spend them or owe them.",
         None),
        ("p", "Start with those who earn dollars. When the rupee weakens, every dollar an exporter "
              "earns turns into more rupees. The exporter can keep the dollar price unchanged and "
              "enjoy a bigger income, or cut the price abroad to win more orders. Either way, Indian "
              "goods become easier to sell, and we say that their **export competitiveness** has "
              "improved. The gain is smaller than it looks for firms that import their own raw "
              "materials or machines, as the story of Selvi's unit shows.",
         ("Export competitiveness", "The ability of a country's firms to sell goods and services "
                                    "abroad at prices that foreign buyers are willing to pay.")),
        ("box", "Real-life example", "A weaker rupee in Selvi's unit", [
            "Selvi's unit in Tiruppur sells cotton T-shirts to a buyer in the United States, priced "
            "in dollars. Suppose she ships an order worth $20,000 (hypothetical). At ₹85 per dollar "
            "it brings in ₹17 lakh; at ₹90, the same order brings in ₹18 lakh. The extra ₹1 lakh "
            "can pay for overtime wages, or let her offer a small discount to win the next order.",
            "This is not just a classroom story. In early 2025, the Tiruppur Exporters' Association "
            "estimated that the rupee's fall during 2024 accounted for about 5 per cent of the growth "
            "in the town's garment exports (Business Standard, 2025).",
            "But Selvi's gain is not pure profit. Some of her dyes, accessories and machine parts "
            "are imported, and these now cost more. Her American buyer reads the same news, too, "
            "and may ask her to share the gain through a lower price.",
        ]),
        ("p", "Now consider those who spend dollars. India imports crude oil, gold, electronics, "
              "fertiliser and edible oil, almost all priced in dollars. A weaker rupee makes each of "
              "them dearer in rupees, even when the dollar price has not changed. Diesel runs the "
              "trucks that carry vegetables, grain and medicines, so costlier fuel spreads into the "
              "price of almost everything (Figure M4-3). A rise in prices that comes from dearer "
              "imports is called **imported inflation**.",
         ("Imported inflation", "A rise in the general price level caused by higher rupee prices "
                                "of imported goods, often because the rupee has depreciated.")),
        ("fig", "Fig_M4-3_imported_inflation_chain.png", "M4-3",
         "How a weaker rupee becomes imported inflation",
         "Read the chain from left to right. Each step takes time, so the full effect on prices can "
         "take several months to appear. The exchange rates shown are hypothetical.",
         "Drawn by the authors."),
        ("box", "Worked example", "The same barrel, a different price", [
            "Suppose a barrel of crude oil costs $80 on the world market (hypothetical figures).",
            "• At ₹85 per US dollar, India pays 80 × 85 = ₹6,800 per barrel.",
            "• At ₹90 per US dollar, India pays 80 × 90 = ₹7,200 per barrel.",
            "The oil has not become any dearer in dollars, yet India pays ₹400 more for every "
            "barrel, a rise of about 5.9 per cent.",
            "Now you try: the dollar price of oil rises to $90 while the rupee stays at ₹90 per "
            "dollar. What is the new rupee price of a barrel, and by what percentage has it risen "
            "compared with ₹6,800? (Answer: ₹8,100, a rise of about 19 per cent. When oil prices "
            "rise and the rupee weakens together, the two effects multiply.)",
        ]),
        ("p", "Then there are those who owe dollars. A company that borrowed in dollars, such as an "
              "airline paying for new aircraft, must now find more rupees to repay the same loan. A "
              "sharp fall in the rupee can turn a healthy balance sheet into a worrying one.",
         None),
        ("p", "All of this matters to the Reserve Bank of India. When the RBI raises its policy "
              "interest rate (the repo rate), Indian assets pay more, foreign money tends to flow in "
              "and the rupee strengthens. Imports become cheaper and inflation cools, although "
              "exporters find life harder. This route from interest rates to spending and prices, "
              "working through the exchange rate, is called the **exchange rate channel** of "
              "monetary policy (Jayadev, 2021, Section 15.9). It is one reason the RBI keeps a close "
              "eye on the rupee whenever it sets interest rates.",
         ("Exchange rate channel", "The way a change in the central bank's policy interest rate "
                                   "affects spending and prices by moving the exchange rate, and "
                                   "through it exports and imports.")),
    ],
}

SECTION_D = {
    "number": "D",
    "title": "When currencies collapse: crises in South Asia",
    "budget": 500,
    "blocks": [
        ("p", "Foreign exchange reserves work like a family's savings for a bad year [see: The RBI "
              "and India's foreign exchange reserves]. But what happens when the savings run out? A country "
              "that cannot find enough dollars to pay for its imports and repay its foreign loans can "
              "no longer protect its currency. The result is a **currency crisis**: a sudden, steep "
              "fall in the value of a currency, usually together with shortages and soaring prices. "
              "Two of India's neighbours have lived through one recently.",
         ("Currency crisis", "A sudden and large fall in the value of a country's currency, usually "
                             "because the country has run short of foreign exchange.")),
        ("p", "**Sri Lanka, 2022.** Sri Lanka's troubles built up over several years. Large tax cuts "
              "in 2019 reduced the government's income. The COVID-19 pandemic then emptied the tourist "
              "hotels that had earned much of the country's foreign currency, while big repayments on "
              "foreign loans kept falling due. The central bank held the Sri Lankan rupee at about 200 "
              "per dollar and spent its reserves to do so. By the end of March 2022, gross reserves "
              "were down to about US$1.9 billion, and most of that could not easily be spent (Daily "
              "Mirror, 2022).",
         None),
        ("p", "Once the currency was allowed to float in March 2022, it crashed, from about 202 rupees "
              "per dollar in February to about 356 by May (Figure M4-4). Fuel, cooking gas and "
              "medicines ran short, and people queued for hours outside petrol pumps. In April 2022 "
              "the government stopped paying its foreign debts, Sri Lanka's first **sovereign "
              "default**. Inflation reached 69.8 per cent in September 2022 (Central Bank of Sri "
              "Lanka [CBSL], 2022). In March 2023 the IMF approved a loan of about US$3 billion "
              "(International Monetary Fund [IMF], 2023a), and prices slowly began to settle.",
         ("Sovereign default", "When a government fails to make the payments on its debt that it "
                               "has promised.")),
        ("fig", "Fig_M4-4_sri_lanka_vs_india_index.png", "M4-4",
         "The Sri Lankan and Indian rupees against the US dollar, 2021 to 2024",
         "Both lines show how many units of local currency it takes to buy one dollar, scaled so "
         "that January 2022 = 100. A rise means the currency has weakened. Once Sri Lanka stopped "
         "defending its rupee, it lost value within weeks. The Indian rupee also weakened over 2022, "
         "but gradually.",
         "Board of Governors of the Federal Reserve System (2026a, 2026b), series EXINUS and EXSLUS, "
         "monthly averages, retrieved from FRED, Federal Reserve Bank of St. Louis, 1 November 2026. "
         "Index calculated by the authors."),
        ("p", "**Pakistan, 2022–23.** Pakistan came close to the same edge. High oil prices widened its "
              "current account deficit, floods in the summer of 2022 destroyed crops and homes, and "
              "talks with the IMF stalled. In early February 2023, the State Bank of Pakistan's "
              "reserves fell to about US$2.9 billion, their lowest level in nine years and barely "
              "enough for a few weeks of imports (Business Recorder, 2023a). The government restricted "
              "imports and the Pakistani rupee slid, reaching a record low of about 307 per dollar in "
              "September 2023 (Xinhua, 2023). Inflation hit 38 per cent in May 2023 (Business "
              "Recorder, 2023b). A US$3 billion **IMF programme**, approved in July 2023, helped "
              "Pakistan avoid default (IMF, 2023b).",
         ("IMF programme", "A loan from the International Monetary Fund to a country short of "
                           "foreign currency, paid in instalments on condition that the country "
                           "carries out agreed policy changes.")),
        ("p", "**What about India?** Both stories echo India's own crisis of 1991 [see: Exchange rate "
              "systems: fixed, flexible and managed], when reserves covered only a few weeks of "
              "imports. India's position today is much stronger. Its reserves stood at about US$700 "
              "billion in April 2026 (Reserve Bank of India [RBI], 2026). Under a managed float, the "
              "rupee adjusts a little every day, so pressure is released gradually instead of building "
              "up behind a fixed rate. And earnings from software services and remittances cover a "
              "large part of the gap in goods trade.",
         None),
        ("table", "M4-2", "Three currency crises compared",
         ["", "India, 1991", "Sri Lanka, 2022", "Pakistan, 2022–23"],
         [
             ["Main triggers",
              "Oil price spike during the Gulf War; fall in remittances; large fiscal and current account deficits",
              "Tax cuts; collapse of tourism during COVID-19; heavy foreign debt repayments; a sudden ban on chemical fertilisers that hurt harvests",
              "High oil prices; large current account deficit; 2022 floods; political uncertainty; stalled IMF talks"],
             ["Reserves at the worst point",
              "Enough for only a few weeks of imports",
              "About US$1.9 billion (March 2022)",
              "About US$2.9 billion (February 2023)"],
             ["What happened to the currency",
              "Devalued in two steps in July 1991; about ₹21 per dollar in June to about ₹26 by August",
              "Fell from about 202 to about 356 per dollar within three months of floating",
              "Slid to a record low of about 307 per dollar (September 2023)"],
             ["Peak inflation",
              "About 14% (1991–92)",
              "69.8% (September 2022)",
              "38% (May 2023)"],
             ["The way out",
              "IMF loan, gold pledged abroad and wide-ranging economic reforms",
              "Default on foreign debt (April 2022); IMF programme of about US$3 billion (March 2023); debt restructuring",
              "IMF Stand-By Arrangement of US$3 billion (July 2023); curbs on imports"],
         ],
         None,
         "Board of Governors of the Federal Reserve System (2026a); Business Recorder (2023a, 2023b); "
         "CBSL (2022); Daily Mirror (2022); IMF (2023a, 2023b); Xinhua (2023). India 1991 details "
         "follow [see: Exchange rate systems: fixed, flexible and managed]."),
        ("p", "The lesson from all three cases is that currencies rarely collapse because of a single "
              "bad event. Low reserves, heavy foreign-currency debt and a large current account "
              "deficit are like dry wood. A pandemic, an oil shock or a flood only supplies the spark.",
         None),
        ("box", "When economists disagree", "Is the IMF's medicine too bitter?", [
            "IMF loans come with conditions. Under its 2023 programme, for example, Sri Lanka agreed "
            "to raise taxes and to price fuel and electricity so that they cover their costs.",
            "Supporters argue that the conditions fix the problems that caused the crisis in the "
            "first place. They also reassure other lenders and investors, who return only when they "
            "trust the government's plans. Without reform, they say, the loan would simply be spent "
            "and the crisis would return.",
            "Critics reply that raising taxes and cutting spending in the middle of a crisis makes "
            "the slump deeper. The burden falls hardest on poor families, who spend most of their "
            "income on food and fuel. And conditions drawn up in Washington may not suit local "
            "circumstances.",
            "What do you think? Should help in a crisis come with strings attached?",
        ]),
    ],
}

SECTIONS = [SECTION_7, SECTION_8, SECTION_D]

KEY_TERMS = [
    ("7", "Capital flows", SECTION_7),
    ("7", "Interest rate differential", SECTION_7),
    ("7", "Speculation", SECTION_7),
    ("8", "Export competitiveness", SECTION_8),
    ("8", "Imported inflation", SECTION_8),
    ("8", "Exchange rate channel", SECTION_8),
    ("D", "Currency crisis", SECTION_D),
    ("D", "Sovereign default", SECTION_D),
    ("D", "IMF programme", SECTION_D),
]

QUESTIONS = [
    ("Multiple choice (Section 7)",
     "The US Federal Reserve raises its interest rate sharply. Assuming nothing else changes, what "
     "is most likely to happen in the market for US dollars in India?",
     ["(a) The demand curve for dollars shifts left and the rupee appreciates.",
      "(b) The supply curve of dollars shifts left and the rupee depreciates.",
      "(c) The supply curve of dollars shifts right and the rupee appreciates.",
      "(d) Nothing changes, because the RBI has not changed its own interest rate."],
     "(b). The interest rate differential narrows, so foreign investors move funds out of India. "
     "Fewer dollars are offered at every exchange rate, and the ₹/$ rate rises."),
    ("Multiple choice (Section 8)",
     "Which of the following is an example of imported inflation?",
     ["(a) Vegetable prices rise after a weak monsoon.",
      "(b) Diesel prices rise after the rupee falls from ₹85 to ₹90 per US dollar.",
      "(c) House rents rise in Bengaluru as more IT firms open offices.",
      "(d) Wages rise after a new minimum wage law."],
     "(b). Only (b) starts with imports becoming dearer in rupees. The others are caused by "
     "domestic supply or demand conditions."),
    ("Short answer with diagram (Section 7, 4 marks)",
     "In 2022, two things happened at the same time: world crude oil prices rose, and the US Federal "
     "Reserve raised interest rates. (i) Draw a diagram of the market for US dollars in India showing "
     "both changes. (ii) Explain why we can be sure what happened to the value of the rupee, but not "
     "to the quantity of dollars traded.",
     [],
     "(i) Demand for dollars shifts right (refiners need more dollars for oil); supply of dollars "
     "shifts left (foreign investors take funds to the United States). (ii) Both shifts push the "
     "₹/$ rate up, so the rupee clearly depreciates. But the demand shift raises the quantity of "
     "dollars traded while the supply shift lowers it, so the net effect on quantity depends on "
     "which shift is larger."),
    ("Extra multiple choice (Section D, optional)",
     "Which combination of conditions left Sri Lanka most exposed to a currency crisis in 2022?",
     ["(a) High reserves, little foreign debt and a booming tourism sector.",
      "(b) Low reserves, heavy foreign debt repayments and a collapse in tourism earnings.",
      "(c) A flexible exchange rate and fast-growing exports.",
      "(d) Rising remittances and falling world oil prices."],
     "(b). Low reserves, heavy foreign-currency debt and a sudden loss of foreign earnings are the "
     "'dry wood' described in the section."),
]

BOX_ANSWERS = [
    ("1", "B (1991)", "Does not fit: the rate was set by an official devaluation, not by the market "
                      "[see: Exchange rate systems: fixed, flexible and managed]."),
    ("2", "D (2008)", "Supply of dollars shifted left as investors fled to the safety of the dollar."),
    ("3", "E (2013, the 'taper tantrum')", "Supply shifted left as foreign money left; India's large "
                                            "current account deficit kept demand for dollars high."),
    ("4", "F (2020)", "Supply shifted left: a global flight to safety."),
    ("5", "A (2022)", "Both: supply shifted left (US rate rises) and demand shifted right (dearer oil)."),
    ("6", "C (2026)", "Both: demand shifted right (oil above $110) and supply shifted left (foreign "
                      "investors sold Indian assets) (Shivalkar, 2026)."),
]

FURTHER_LEARNING = [
    "Khan Academy. (n.d.). *Open economy: International trade and finance* [Video lessons, AP "
    "Macroeconomics]. See 'Exchange rate primer' and 'Causes of shifts in currency supply and demand "
    "curves'. https://www.khanacademy.org/economics-finance-domain/ap-macroeconomics/ap-open-economy-international-trade-and-finance",
    "Jayadev, A. (2021). Section 15.9, 'The exchange rate channel of monetary policy'. In *The "
    "economy: A South Asian perspective*. CORE Econ. "
    "https://books.core-econ.org/the-economy-south-asia/book/text/15.html",
]

REFERENCES = [
    "Board of Governors of the Federal Reserve System (US). (2026a). *Indian rupees to U.S. dollar "
    "spot exchange rate* [EXINUS] [Data set]. FRED, Federal Reserve Bank of St. Louis. Retrieved "
    "November 1, 2026, from https://fred.stlouisfed.org/series/EXINUS",
    "Board of Governors of the Federal Reserve System (US). (2026b). *Sri Lankan rupees to U.S. "
    "dollar spot exchange rate* [EXSLUS] [Data set]. FRED, Federal Reserve Bank of St. Louis. "
    "Retrieved November 1, 2026, from https://fred.stlouisfed.org/series/EXSLUS",
    "Business Recorder. (2023a, February 9). *Highly critical: SBP-held foreign exchange reserves "
    "fall $170mn, now stand at mere $2.92bn*. https://www.brecorder.com/news/40225346",
    "Business Recorder. (2023b, June 1). *Pakistan's headline inflation hits new record at 38% in "
    "May 2023*. https://www.brecorder.com/news/40245453",
    "Business Standard. (2025, January 6). *Textile hub Tiruppur threads a recovery on sliding rupee "
    "as exports surge*. https://www.business-standard.com/industry/news/textile-hub-tiruppur-threads-a-recovery-on-sliding-rupee-as-exports-surge-125010600927_1.html",
    "Central Bank of Sri Lanka. (2022, September 30). *CCPI based headline inflation recorded at "
    "69.8% on year-on-year basis in September 2022* [Press release]. https://www.cbsl.gov.lk",
    "Daily Mirror. (2022, April 9). *Sri Lanka's foreign reserves down by US $372mn to US $1.93bn by "
    "end-March*. https://www.dailymirror.lk/business-news/Sri-Lankas-foreign-reserves-down-by-US-372mn-to-US-1-93bn-by-end-March/273-234865",
    "International Monetary Fund. (2023a, March 20). *IMF Executive Board approves US$3 billion under "
    "the new Extended Fund Facility (EFF) arrangement for Sri Lanka* (Press Release No. 23/79). "
    "https://www.imf.org/en/News/Articles/2023/03/20/pr2379-imf-executive-board-approves-under-the-new-eff-arrangement-for-sri-lanka",
    "International Monetary Fund. (2023b, July 12). *IMF Executive Board approves US$3 billion "
    "Stand-By Arrangement for Pakistan* (Press Release No. 23/261). "
    "https://www.imf.org/en/News/Articles/2023/07/12/pr23261-pakistan-imf-exec-board-approves-us3bil-sba",
    "Jayadev, A. (2021). *The economy: A South Asian perspective* (Version 1.0.1). CORE Econ. "
    "https://books.core-econ.org/the-economy-south-asia/",
    "Petroleum Planning & Analysis Cell. (2025). *Snapshot of India's oil & gas data*. Ministry of "
    "Petroleum and Natural Gas, Government of India. https://ppac.gov.in",
    "Reserve Bank of India. (2026, April 17). *Weekly statistical supplement* [Foreign exchange "
    "reserves, week ended April 10, 2026]. https://www.rbi.org.in",
    "Shivalkar, A. (2026, April 30). *Rupee slips past 95 per dollar to record low on April 30, "
    "2026*. Angel One. https://www.angelone.in/news/economy/rupee-slips-past-95-per-dollar-to-record-low-on-april-30-2026",
    "Xinhua. (2023, September 6). Pakistani rupee picks up crash mode against USD, touching record "
    "low. *The Star*. https://www.thestar.com.my/news/world/2023/09/06/pakistani-rupee-picks-up-crash-mode-against-usd-touching-record-low",
]

TEAM_NOTES = [
    "Member 2: Figure M4-2 uses placeholder colours (navy demand, orange supply, green shift "
    "arrows). Please share the common template and I will redraw it; the source script is "
    "source/build_figures.py, and colours change in one place (PALETTE).",
    "Member 3: the India 1991 column of Table M4-2 must match your case study box. Please confirm "
    "the reserve level, the size of the devaluation and the 1991–92 inflation figure (about 14% "
    "used here).",
    "Member 1: nine glossary terms are listed above with one-line definitions. 'Current account "
    "deficit' is used in Sections 7 and D but not defined, since Section A owns it.",
    "Optional photograph for Section D: a fuel queue in Colombo, 2022. Use a Creative Commons "
    "image (for example from Wikimedia Commons) with full credit, or skip it.",
    "The word count at the top of each section covers main text only (paragraphs). Boxes, "
    "captions and tables are excluded, as the plan assumes.",
]

CROSS_REFS = [
    ("7", "How the exchange rate is determined: demand and supply", "Member 2, Section 3"),
    ("7", "Nominal and real exchange rates, and purchasing power parity", "Member 3, Section 6"),
    ("7", "The rupee's account book: the balance of payments", "Member 1, Section A"),
    ("7 (box)", "Exchange rate systems: fixed, flexible and managed", "Member 3, Section 5"),
    ("8", "Appreciation and depreciation: who wins, who loses?", "Member 2, Section 4"),
    ("D", "The RBI and India's foreign exchange reserves", "Member 3, Section C"),
    ("D", "Exchange rate systems: fixed, flexible and managed", "Member 3, Section 5"),
]


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
TOKEN = re.compile(r"(\*\*.+?\*\*|\*.+?\*|\[see: .+?\])")


def smart_quotes(text):
    text = re.sub(r"(^|[\s(\[])'", r"\1‘", text)
    return text.replace("'", "’")


def plain(text):
    return re.sub(r"\*\*|\*", "", text)


def word_count(section):
    return sum(len(plain(b[1]).split()) for b in section["blocks"] if b[0] == "p")


def set_font(run, size=None, bold=None, italic=None, color=None, font=None):
    if font:
        run.font.name = font
        run._element.rPr.rFonts.set(qn("w:eastAsia"), font)
    if size:
        run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color is not None:
        run.font.color.rgb = color


def add_rich(par, text, size=None, color=None):
    for part in TOKEN.split(smart_quotes(text)):
        if not part:
            continue
        if part.startswith("**"):
            set_font(par.add_run(part[2:-2]), size=size, bold=True, color=color)
        elif part.startswith("[see:"):
            set_font(par.add_run(part), size=size, italic=True, color=GREY)
        elif part.startswith("*"):
            set_font(par.add_run(part[1:-1]), size=size, italic=True, color=color)
        else:
            set_font(par.add_run(part), size=size, color=color)
    return par


def shade(cell, hex_fill):
    tc_pr = cell._element.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    tc_pr.append(shd)


def borders(table, color="FFFFFF", size=0, sides=("top", "left", "bottom", "right", "insideH", "insideV")):
    tbl_pr = table._element.tblPr
    el = OxmlElement("w:tblBorders")
    for side in sides:
        b = OxmlElement(f"w:{side}")
        b.set(qn("w:val"), "single" if size else "nil")
        b.set(qn("w:sz"), str(size))
        b.set(qn("w:color"), color)
        el.append(b)
    tbl_pr.append(el)


def left_rule(cell, hex_color, size=24):
    tc_pr = cell._element.get_or_add_tcPr()
    b = OxmlElement("w:tcBorders")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), str(size))
    left.set(qn("w:color"), hex_color)
    b.append(left)
    tc_pr.append(b)


def widths(table, cms):
    table.autofit = False
    for row in table.rows:
        for cell, w in zip(row.cells, cms):
            cell.width = Cm(w)


def spacing(par, before=0, after=6, line=None):
    pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    if line:
        pf.line_spacing = line


def heading(doc, text, level_size, color=NAVY, before=14, after=6):
    p = doc.add_paragraph()
    set_font(p.add_run(smart_quotes(text)), size=level_size, bold=True, color=color, font=HEAD_FONT)
    spacing(p, before, after)
    p.paragraph_format.keep_with_next = True
    return p


# ---------------------------------------------------------------------------
# BLOCK WRITERS
# ---------------------------------------------------------------------------
def write_paragraph(doc, text, note):
    if not note:
        p = add_rich(doc.add_paragraph(), text)
        spacing(p, after=8, line=1.25)
        return
    t = doc.add_table(rows=1, cols=2)
    borders(t)
    widths(t, [12.4, 4.2])
    left, right = t.rows[0].cells
    p = add_rich(left.paragraphs[0], text)
    spacing(p, after=4, line=1.25)
    shade(right, "EEF3EE")
    left_rule(right, "4C8B4A", 18)
    rp = right.paragraphs[0]
    set_font(rp.add_run(note[0]), size=9, bold=True, color=GREEN, font=HEAD_FONT)
    rp2 = right.add_paragraph()
    set_font(rp2.add_run(smart_quotes(note[1])), size=8.5, font=HEAD_FONT)
    spacing(rp, after=2)
    spacing(rp2, after=2)
    spacing(doc.add_paragraph(), after=2)


def write_figure(doc, filename, number, title, caption, source):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(FIG / filename), width=Cm(16.4))
    spacing(p, before=6, after=2)
    p.paragraph_format.keep_with_next = True
    cap = doc.add_paragraph()
    set_font(cap.add_run(f"Figure {number}  "), size=10, bold=True, color=NAVY, font=HEAD_FONT)
    set_font(cap.add_run(smart_quotes(title)), size=10, bold=True, font=HEAD_FONT)
    spacing(cap, after=2)
    cap.paragraph_format.keep_with_next = True
    for line in caption.split("\n"):
        line_par = add_rich(doc.add_paragraph(), line, size=9.5)
        line_par.paragraph_format.space_after = Pt(2)
        line_par.paragraph_format.keep_with_next = True
    src = doc.add_paragraph()
    set_font(src.add_run("Source: "), size=8.5, bold=True, color=GREY)
    add_rich(src, source, size=8.5, color=GREY)
    spacing(src, after=12)


def write_box(doc, kind, title, paras):
    t = doc.add_table(rows=1, cols=1)
    borders(t)
    widths(t, [16.6])
    cell = t.rows[0].cells[0]
    shade(cell, "FBF3EA")
    left_rule(cell, "D9822B", 30)
    p = cell.paragraphs[0]
    set_font(p.add_run(kind.upper()), size=8.5, bold=True, color=ORANGE, font=HEAD_FONT)
    spacing(p, before=4, after=0)
    p = cell.add_paragraph()
    set_font(p.add_run(smart_quotes(title)), size=11.5, bold=True, color=NAVY, font=HEAD_FONT)
    spacing(p, after=4)
    for text in paras:
        p = add_rich(cell.add_paragraph(), text, size=10)
        spacing(p, after=4, line=1.15)
        if text.startswith(("•", "A.", "B.", "C.", "D.", "E.", "F.")):
            p.paragraph_format.left_indent = Cm(0.5)
    spacing(doc.add_paragraph(), after=4)


def write_table(doc, number, title, header, rows, note, source):
    cap = doc.add_paragraph()
    set_font(cap.add_run(f"Table {number}  "), size=10, bold=True, color=NAVY, font=HEAD_FONT)
    set_font(cap.add_run(smart_quotes(title)), size=10, bold=True, font=HEAD_FONT)
    spacing(cap, before=6, after=4)
    cap.paragraph_format.keep_with_next = True
    t = doc.add_table(rows=1 + len(rows), cols=len(header))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    borders(t, color="C9D2DC", size=4)
    col_w = [3.4, 4.4, 4.4, 4.4] if len(header) == 4 and header[0] == "" else [5.0, 7.0, 2.2, 2.4]
    widths(t, col_w)
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]
        shade(c, "1F3A5F")
        set_font(c.paragraphs[0].add_run(h), size=9, bold=True, color=RGBColor(255, 255, 255), font=HEAD_FONT)
    for tr in t.rows:
        tr._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
    for r, row in enumerate(rows, start=1):
        for i, val in enumerate(row):
            c = t.rows[r].cells[i]
            if r % 2 == 0:
                shade(c, "F3F5F8")
            add_rich(c.paragraphs[0], val, size=9)
            if i == 0:
                for run in c.paragraphs[0].runs:
                    run.bold = header[0] == ""
    if note:
        n = add_rich(doc.add_paragraph(), note, size=8.5, color=GREY)
        spacing(n, before=3, after=2)
    if source:
        s = doc.add_paragraph()
        set_font(s.add_run("Source: "), size=8.5, bold=True, color=GREY)
        add_rich(s, source, size=8.5, color=GREY)
        spacing(s, before=3, after=12)
    else:
        spacing(doc.add_paragraph(), after=6)


def write_section(doc, sec):
    p = doc.add_paragraph()
    set_font(p.add_run(f"{sec['number']}  "), size=18, bold=True, color=GREEN, font=HEAD_FONT)
    set_font(p.add_run(smart_quotes(sec["title"])), size=18, bold=True, color=NAVY, font=HEAD_FONT)
    spacing(p, before=6, after=2)
    wc = doc.add_paragraph()
    set_font(wc.add_run(f"Main text: {word_count(sec)} words (budget about {sec['budget']})"),
             size=8.5, italic=True, color=GREY, font=HEAD_FONT)
    spacing(wc, after=10)
    for block in sec["blocks"]:
        kind = block[0]
        if kind == "p":
            write_paragraph(doc, block[1], block[2])
        elif kind == "fig":
            write_figure(doc, *block[1:])
        elif kind == "box":
            write_box(doc, *block[1:])
        elif kind == "table":
            write_table(doc, *block[1:])


def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


# ---------------------------------------------------------------------------
# DOCUMENT
# ---------------------------------------------------------------------------
def build():
    doc = Document()
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21.0), Cm(29.7)
        s.left_margin = s.right_margin = Cm(2.2)
        s.top_margin = s.bottom_margin = Cm(2.0)
    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)
    normal.font.size = Pt(11)

    footer = doc.sections[0].footer.paragraphs[0]
    set_font(footer.add_run("The Foreign Exchange Rate  |  Member 4: Sections 7, 8 and D  |  "
                            "Introduction to Economics, Monsoon 2026"), size=8, color=GREY, font=HEAD_FONT)

    # Cover block
    p = doc.add_paragraph()
    set_font(p.add_run("INTRODUCTION TO ECONOMICS · MONSOON 2026 · MEMBER 4 SECTION PACKET"),
             size=8.5, bold=True, color=ORANGE, font=HEAD_FONT)
    p = doc.add_paragraph()
    set_font(p.add_run("The Foreign Exchange Rate"), size=26, bold=True, color=NAVY, font=HEAD_FONT)
    spacing(p, after=0)
    p = doc.add_paragraph()
    set_font(p.add_run("Real-world applications: what moves the rupee, why it matters, and what "
                       "happens when a currency collapses"), size=12, italic=True, color=GREY,
             font=HEAD_FONT)
    spacing(p, after=12)

    t = doc.add_table(rows=1, cols=2)
    borders(t, color="C9D2DC", size=4)
    widths(t, [5.0, 11.6])
    contents = [
        ("Sections", "7 What moves the rupee?  ·  8 Why exchange rates matter for India  ·  "
                     "D When currencies collapse: crises in South Asia"),
        ("Main text", " · ".join(f"{s['number']}: {word_count(s)} words" for s in SECTIONS)
         + f"  (total {sum(word_count(s) for s in SECTIONS)})"),
        ("Figures", "M4-1 to M4-4 (PNG, 300 dpi, in figures/; editable source in source/)"),
        ("Tables", "M4-1 What moves the rupee · M4-2 Three currency crises compared"),
        ("Boxes", "How economists learn from facts · Real-life example · Worked example · "
                  "When economists disagree"),
        ("Handover", "Key terms · Questions and answers · Box answer key · Further learning · "
                     "References · Cross-references · Notes for the team"),
        ("Builds on", "Members 1–3; see Member4_Prerequisites_from_Members_1-3.md"),
    ]
    for i, (k, v) in enumerate(contents):
        row = t.rows[0] if i == 0 else t.add_row()
        set_font(row.cells[0].paragraphs[0].add_run(k), size=9, bold=True, color=NAVY, font=HEAD_FONT)
        set_font(row.cells[1].paragraphs[0].add_run(v), size=9, font=HEAD_FONT)
    widths(t, [5.0, 11.6])
    page_break(doc)

    for i, sec in enumerate(SECTIONS):
        write_section(doc, sec)
        page_break(doc)

    # Handover material
    heading(doc, "Handover: material for the shared end matter", 16, before=0)

    heading(doc, "Key terms for the glossary", 12, color=GREEN)
    t = doc.add_table(rows=1, cols=3)
    borders(t, color="C9D2DC", size=4)
    for i, h in enumerate(["Section", "Term", "Definition"]):
        shade(t.rows[0].cells[i], "1F3A5F")
        set_font(t.rows[0].cells[i].paragraphs[0].add_run(h), size=9, bold=True,
                 color=RGBColor(255, 255, 255), font=HEAD_FONT)
    for num, term, sec in KEY_TERMS:
        definition = next(b[2][1] for b in sec["blocks"] if b[0] == "p" and b[2] and b[2][0] == term)
        row = t.add_row()
        for i, val in enumerate([num, term, definition]):
            set_font(row.cells[i].paragraphs[0].add_run(smart_quotes(val)), size=9, bold=(i == 1))
    widths(t, [1.6, 4.2, 10.8])

    heading(doc, "Review questions with answers", 12, color=GREEN)
    for label, q, options, answer in QUESTIONS:
        p = doc.add_paragraph()
        set_font(p.add_run(label), size=9, bold=True, color=ORANGE, font=HEAD_FONT)
        spacing(p, before=6, after=2)
        spacing(add_rich(doc.add_paragraph(), q, size=10.5), after=2)
        for o in options:
            op = add_rich(doc.add_paragraph(), o, size=10)
            op.paragraph_format.left_indent = Cm(0.6)
            spacing(op, after=1)
        a = doc.add_paragraph()
        set_font(a.add_run("Answer: "), size=10, bold=True, color=GREEN)
        add_rich(a, answer, size=10)
        spacing(a, before=2, after=6)

    heading(doc, "Answer key: 'Reading the rupee's history' box", 12, color=GREEN)
    t = doc.add_table(rows=1, cols=3)
    borders(t, color="C9D2DC", size=4)
    for i, h in enumerate(["Band", "Event", "What shifted"]):
        shade(t.rows[0].cells[i], "1F3A5F")
        set_font(t.rows[0].cells[i].paragraphs[0].add_run(h), size=9, bold=True,
                 color=RGBColor(255, 255, 255), font=HEAD_FONT)
    for band, event, why in BOX_ANSWERS:
        row = t.add_row()
        for i, val in enumerate([band, event, why]):
            add_rich(row.cells[i].paragraphs[0], val, size=9)
    widths(t, [1.6, 4.6, 10.4])

    heading(doc, "Further learning", 12, color=GREEN)
    for item in FURTHER_LEARNING:
        p = add_rich(doc.add_paragraph(), item, size=10)
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.first_line_indent = Cm(-1.0)
        spacing(p, after=4)

    heading(doc, "References (APA 7th edition)", 12, color=GREEN)
    for ref in REFERENCES:
        p = add_rich(doc.add_paragraph(), ref, size=10)
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.first_line_indent = Cm(-1.0)
        spacing(p, after=4)

    heading(doc, "Cross-references made in these sections", 12, color=GREEN)
    t = doc.add_table(rows=1, cols=3)
    borders(t, color="C9D2DC", size=4)
    for i, h in enumerate(["Used in", "Section referred to", "Owner"]):
        shade(t.rows[0].cells[i], "1F3A5F")
        set_font(t.rows[0].cells[i].paragraphs[0].add_run(h), size=9, bold=True,
                 color=RGBColor(255, 255, 255), font=HEAD_FONT)
    for used, title, owner in CROSS_REFS:
        row = t.add_row()
        for i, val in enumerate([used, title, owner]):
            set_font(row.cells[i].paragraphs[0].add_run(smart_quotes(val)), size=9)
    widths(t, [2.2, 10.0, 4.4])

    heading(doc, "Notes for the team", 12, color=GREEN)
    for note in TEAM_NOTES:
        p = add_rich(doc.add_paragraph(), "• " + note, size=10)
        p.paragraph_format.left_indent = Cm(0.5)
        spacing(p, after=4)

    doc.save(OUT)
    for s in SECTIONS:
        print(f"Section {s['number']}: {word_count(s)} words (budget {s['budget']})")
    print("Saved", OUT)


if __name__ == "__main__":
    build()
