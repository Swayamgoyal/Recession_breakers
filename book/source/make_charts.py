"""Data charts for the merged chapter, drawn in the same style as Figure 3
(Member 1's remittances chart): Source Sans 3, chapter navy/orange, light grid.

Run:  python make_charts.py      (writes PDFs into ../figures)

Data (in ./data):
  EXINUS_monthly.csv, EXSLUS_monthly.csv  FRED, Board of Governors of the Federal
                                          Reserve System, monthly averages
  wb_reserves.json                        World Bank WDI, FI.RES.TOTL.CD (total
                                          reserves incl. gold, end of year)
"""
import csv
import json
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE.parent / "figures"
for f in (HERE.parent / "fonts").glob("SourceSans3_*.ttf"):
    font_manager.fontManager.addfont(str(f))

NAVY, ORANGE, TEAL = "#1F3A5F", "#C8641E", "#2A7072"
RED, INK, MUTED, GRID = "#B5443B", "#222222", "#6B6B6B", "#E3E3E3"
BAND = "#F6E3CF"

plt.rcParams.update({
    "font.family": "Source Sans 3",
    "font.size": 8.5,
    "axes.edgecolor": "#9A9A9A",
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
})


def style(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.yaxis.grid(True, color=GRID, linewidth=0.7, zorder=0)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", length=2.5)


def save(fig, name):
    fig.tight_layout(pad=0.4)
    fig.savefig(OUT / f"{name}.pdf")
    fig.savefig(OUT / f"{name}.png", dpi=300)
    plt.close(fig)


def fred(name):
    with open(DATA / f"{name}_monthly.csv", newline="") as fh:
        rows = [r for r in csv.reader(fh)][1:]
    return [(date.fromisoformat(d), float(v)) for d, v in rows if v not in ("", ".")]


# ---------------------------------------------------------------------------
# The rupee since 1991, six numbered episodes (Section 9)
# ---------------------------------------------------------------------------
def rupee_history():
    inr = [(d, v) for d, v in fred("EXINUS") if d >= date(1991, 1, 1)]
    dates, vals = zip(*inr)
    fig, ax = plt.subplots(figsize=(4.9, 3.0))
    style(ax)
    ax.plot(dates, vals, color=NAVY, lw=1.5, zorder=3)

    episodes = [((1991, 6), (1991, 9)), ((2008, 9), (2009, 3)), ((2013, 5), (2013, 9)),
                ((2020, 2), (2020, 4)), ((2022, 2), (2022, 12)), ((2026, 3), (2026, 5))]
    for n, (s, e) in enumerate(episodes, start=1):
        s, e = date(*s, 1), date(*e, 1)
        ax.axvspan(s, e, color=BAND, zorder=1)
        peak = max(v for d, v in inr if s <= d <= e)
        mid = s + (e - s) / 2
        ax.annotate(str(n), xy=(mid, peak), xytext=(mid, peak + 9), ha="center", va="center",
                    fontsize=8.5, fontweight="bold", color="white", zorder=4,
                    bbox=dict(boxstyle="circle,pad=0.28", fc=ORANGE, ec="none"),
                    arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.8))

    first, last = inr[0], inr[-1]
    ax.annotate(f"₹{first[1]:.0f} per $\n(Jan 1991)", xy=first, xytext=(date(1994, 6, 1), 4),
                fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
    ax.annotate(f"₹{last[1]:.1f} per $\n({last[0]:%b %Y})", xy=last, xytext=(date(2015, 1, 1), 98),
                fontsize=8, color=INK, fontweight="semibold",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
    ax.text(date(1991, 9, 1), 104, "Higher = weaker rupee", fontsize=8, color=RED, style="italic")
    ax.set_ylim(0, 112)
    ax.set_xlim(date(1990, 6, 1), date(2027, 6, 1))
    ax.set_ylabel("₹ per US dollar")
    save(fig, "rupee_history")


# ---------------------------------------------------------------------------
# India's reserves since 1990 (Section 7) -- redraw of Member 3's chart
# ---------------------------------------------------------------------------
def reserves():
    raw = json.load(open(DATA / "wb_reserves.json"))[1]
    pts = sorted((int(r["date"]), r["value"] / 1e9) for r in raw
                 if r["value"] is not None and int(r["date"]) >= 1990)
    years, vals = zip(*pts)
    fig, ax = plt.subplots(figsize=(4.9, 2.9))
    style(ax)
    colors = [ORANGE if y in (1990, years[-1]) else NAVY for y in years]
    ax.bar(years, vals, width=0.72, color=colors, edgecolor="white", linewidth=0.5, zorder=3)
    ax.annotate("1990: US$5.6 bn.\nBy mid-1991, enough for only\nabout two weeks of imports",
                xy=(1990, vals[0]), xytext=(1991.2, 190), fontsize=8, color=INK,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
    ax.annotate(f"US${vals[-1]:.0f} bn\n({years[-1]})", (years[-1], vals[-1]), xytext=(-4, 4),
                textcoords="offset points", ha="right", va="bottom", fontsize=8.5,
                color=INK, fontweight="semibold")
    ax.set_xticks([1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025])
    ax.set_xlim(1989.3, years[-1] + 0.7)
    ax.set_ylim(0, 800)
    ax.set_yticks([0, 200, 400, 600, 800])
    ax.set_ylabel("US$ billion (end of year)")
    save(fig, "reserves")


# ---------------------------------------------------------------------------
# Real exchange rate: Member 3's worked example as a picture (Section 8)
# ---------------------------------------------------------------------------
def real_rate():
    fig, ax = plt.subplots(figsize=(4.9, 2.4))
    style(ax)
    groups = ["Start of year", "End of year"]
    india, usa = [10.00, 10.80], [10.00, 10.20]
    x = [0, 1]
    w = 0.34
    b1 = ax.bar([i - w / 2 for i in x], india, w, color=ORANGE, label="Indian product (₹800 → ₹864, at ₹80 per $)", zorder=3)
    b2 = ax.bar([i + w / 2 for i in x], usa, w, color=NAVY, label="American product", zorder=3)
    for bars in (b1, b2):
        for r in bars:
            ax.text(r.get_x() + r.get_width() / 2, r.get_height() + 0.12, f"${r.get_height():.2f}",
                    ha="center", va="bottom", fontsize=8.5, color=INK)
    ax.set_xticks(x, groups)
    ax.tick_params(axis="x", colors=INK, labelsize=9)
    ax.set_ylim(0, 13.8)
    ax.set_yticks([0, 4, 8, 12])
    ax.set_ylabel("Price in US dollars")
    ax.legend(frameon=False, loc="upper left", fontsize=8, ncols=2)
    save(fig, "real_rate")


# ---------------------------------------------------------------------------
# Sri Lanka's rupee collapse against India's gradual movement (Section 11)
# ---------------------------------------------------------------------------
def sri_lanka():
    start, end, base = date(2021, 1, 1), date(2024, 12, 1), date(2022, 1, 1)
    fig, ax = plt.subplots(figsize=(4.9, 2.9))
    style(ax)
    series = {}
    for name, label, color in (("EXSLUS", "Sri Lankan rupee", RED), ("EXINUS", "Indian rupee", NAVY)):
        data = dict(fred(name))
        idx = [(d, 100 * v / data[base]) for d, v in sorted(data.items()) if start <= d <= end]
        series[name] = dict(idx)
        ax.plot(*zip(*idx), color=color, lw=1.8, label=label, zorder=3)
    lk = series["EXSLUS"]
    for d, text, off in [(date(2022, 3, 1), "Mar 2022: rupee\nallowed to float", (-82, 8)),
                         (date(2022, 4, 1), "Apr 2022: foreign debt\npayments stopped", (22, -38)),
                         (date(2023, 3, 1), "Mar 2023: IMF\nprogramme approved", (18, 22))]:
        ax.annotate(text, xy=(d, lk[d]), xytext=off, textcoords="offset points", fontsize=8,
                    color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.6))
    ax.axhline(100, color=MUTED, lw=0.6, ls="--", zorder=2)
    ax.text(date(2021, 1, 15), 103, "January 2022 = 100", fontsize=8, color=MUTED)
    ax.set_ylim(85, 200)
    ax.set_ylabel("Local currency per US dollar\n(index, Jan 2022 = 100)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.legend(frameon=False, loc="lower right", bbox_to_anchor=(1.0, 0.22))
    save(fig, "srilanka_index")


if __name__ == "__main__":
    rupee_history()
    reserves()
    real_rate()
    sri_lanka()
    print("Charts written to", OUT)
