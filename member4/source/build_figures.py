"""Builds the Member 4 figures (Sections 7, 8 and D) as 300 dpi PNGs.

Run from anywhere:  python build_figures.py
Data comes from FRED (monthly averages of daily rates), saved in ./data.
Colours are placeholders until Member 2 shares the common figure template;
change them in one place (PALETTE) and re-run.
"""
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
OUT = HERE.parent / "figures"
OUT.mkdir(exist_ok=True)

PALETTE = {
    "navy": "#1F3A5F",
    "orange": "#D9822B",
    "green": "#4C8B4A",
    "red": "#B5443B",
    "grey": "#6B7280",
    "light": "#E8EDF3",
    "band": "#F6E3CF",
}

plt.rcParams.update({
    "font.family": "Segoe UI",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#444444",
    "axes.labelcolor": "#222222",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "axes.grid": True,
    "grid.color": "#E3E3E3",
    "grid.linewidth": 0.7,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})


def load_fred(name):
    df = pd.read_csv(DATA / f"{name}_monthly.csv", parse_dates=["observation_date"])
    df.columns = ["date", "value"]
    return df.dropna()


# ---------------------------------------------------------------------------
# Fig M4-1: the rupee since 1991, with six numbered episodes
# ---------------------------------------------------------------------------
def fig_rupee_history():
    inr = load_fred("EXINUS")
    inr = inr[inr["date"] >= "1991-01-01"]

    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.plot(inr["date"], inr["value"], color=PALETTE["navy"], lw=1.8)

    # (start, end, label position) for each episode; numbers only, the
    # matching exercise in the text asks students to name the events.
    episodes = [
        ("1991-06-01", "1991-09-01", 1),
        ("2008-09-01", "2009-03-01", 2),
        ("2013-05-01", "2013-09-01", 3),
        ("2020-02-01", "2020-04-01", 4),
        ("2022-02-01", "2022-12-01", 5),
        ("2026-03-01", "2026-05-01", 6),
    ]
    for start, end, n in episodes:
        s, e = pd.Timestamp(start), pd.Timestamp(end)
        ax.axvspan(s, e, color=PALETTE["band"], zorder=0)
        peak = inr[(inr["date"] >= s) & (inr["date"] <= e)]["value"].max()
        mid = s + (e - s) / 2
        ax.annotate(
            str(n), xy=(mid, peak), xytext=(mid, peak + 7),
            ha="center", va="center", fontsize=10, fontweight="bold",
            color="white",
            bbox=dict(boxstyle="circle,pad=0.3", fc=PALETTE["orange"], ec="none"),
            arrowprops=dict(arrowstyle="-", color=PALETTE["orange"], lw=1),
        )

    first, last = inr.iloc[0], inr.iloc[-1]
    ax.annotate(f"₹{first['value']:.0f} per $\n(Jan 1991)", xy=(first["date"], first["value"]),
                xytext=(pd.Timestamp("1994-06-01"), 6), fontsize=9, color=PALETTE["grey"],
                arrowprops=dict(arrowstyle="-", color=PALETTE["grey"], lw=0.8))
    ax.annotate(f"₹{last['value']:.1f} per $\n({last['date']:%b %Y})", xy=(last["date"], last["value"]),
                xytext=(pd.Timestamp("2016-06-01"), 98), fontsize=9, color=PALETTE["grey"],
                arrowprops=dict(arrowstyle="-", color=PALETTE["grey"], lw=0.8))

    ax.set_ylim(0, 110)
    ax.set_xlim(pd.Timestamp("1990-07-01"), pd.Timestamp("2027-06-01"))
    ax.set_ylabel("Exchange rate (₹/$)")
    ax.set_xlabel("Year")
    ax.text(pd.Timestamp("1991-06-01"), 104, "Higher = weaker rupee", fontsize=9,
            color=PALETTE["red"], style="italic")
    fig.savefig(OUT / "Fig_M4-1_rupee_per_dollar_1991_2026.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Fig M4-2: two shocks in the market for US dollars (hypothetical numbers)
# ---------------------------------------------------------------------------
def _line(ax, x0, y0, x1, y1, **kw):
    ax.plot([x0, x1], [y0, y1], **kw)


def _dashes(ax, q, p, color):
    ax.plot([0, q], [p, p], ls=":", color=color, lw=1)
    ax.plot([q, q], [70, p], ls=":", color=color, lw=1)


def _point(ax, q, p, label, color):
    ax.plot(q, p, "o", color=color, ms=6, zorder=5)
    ax.text(q + 0.25, p + 0.6, label, fontsize=10, fontweight="bold", color=color)


def fig_shocks():
    # Demand: P = 95 - Q ; Supply: P = 75 + Q  ->  E0 at Q=10, P=85
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.6))
    for ax in axes:
        ax.set_xlim(0, 20)
        ax.set_ylim(70, 100)
        ax.grid(False)
        ax.set_xticks([])
        ax.set_xlabel("Quantity of US dollars traded")
    axes[0].set_ylabel("Exchange rate (₹/$)")

    # (a) oil price rise: demand shifts right by 10 -> P = 105 - Q ; E1 Q=15, P=90
    ax = axes[0]
    _line(ax, 1, 94, 19, 76, color=PALETTE["navy"], lw=2)
    _line(ax, 6, 99, 20, 85, color=PALETTE["navy"], lw=2, ls="--")
    _line(ax, 0, 75, 20, 95, color=PALETTE["orange"], lw=2)
    ax.text(18.2, 77.6, "D₀", color=PALETTE["navy"], fontsize=11)
    ax.text(18.8, 87.2, "D₁", color=PALETTE["navy"], fontsize=11)
    ax.text(18.6, 95.3, "S", color=PALETTE["orange"], fontsize=11)
    ax.add_patch(FancyArrowPatch((12.5, 82.5), (16.0, 89.0), arrowstyle="-|>",
                                 mutation_scale=14, color=PALETTE["green"], lw=1.6))
    _dashes(ax, 10, 85, PALETTE["grey"])
    _dashes(ax, 15, 90, PALETTE["grey"])
    _point(ax, 10, 85, "E₀", PALETTE["navy"])
    _point(ax, 15, 90, "E₁", PALETTE["green"])
    ax.set_yticks([85, 90])
    ax.set_title("(a) World oil price rises", loc="left", fontsize=11, fontweight="bold")

    # (b) US interest rates rise: supply shifts left by 8 -> P = 83 + Q ; E1 Q=6, P=89
    ax = axes[1]
    _line(ax, 1, 94, 19, 76, color=PALETTE["navy"], lw=2)
    _line(ax, 0, 75, 20, 95, color=PALETTE["orange"], lw=2)
    _line(ax, 0, 83, 16, 99, color=PALETTE["orange"], lw=2, ls="--")
    ax.text(18.2, 77.6, "D", color=PALETTE["navy"], fontsize=11)
    ax.text(18.6, 95.3, "S₀", color=PALETTE["orange"], fontsize=11)
    ax.text(14.6, 99.0, "S₁", color=PALETTE["orange"], fontsize=11)
    ax.add_patch(FancyArrowPatch((13.0, 88.4), (8.6, 92.6), arrowstyle="-|>",
                                 mutation_scale=14, color=PALETTE["green"], lw=1.6))
    _dashes(ax, 10, 85, PALETTE["grey"])
    _dashes(ax, 6, 89, PALETTE["grey"])
    _point(ax, 10, 85, "E₀", PALETTE["navy"])
    _point(ax, 6, 89, "E₁", PALETTE["green"])
    ax.set_yticks([85, 89])
    ax.tick_params(labelleft=True)
    ax.set_title("(b) US interest rates rise", loc="left", fontsize=11, fontweight="bold")

    fig.tight_layout(w_pad=3)
    fig.savefig(OUT / "Fig_M4-2_two_shocks_dollar_market.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Fig M4-3: how a weaker rupee turns into imported inflation
# ---------------------------------------------------------------------------
def fig_imported_inflation():
    steps = [
        ("Rupee weakens", "₹85 → ₹90 per $"),
        ("Imports cost more", "crude oil, edible oil,\nelectronics, fertiliser"),
        ("Fuel prices rise", "petrol, diesel\nand LPG"),
        ("Costs rise", "transport and\nproduction"),
        ("Prices rise", "food and everyday\ngoods: imported inflation"),
    ]
    fig, ax = plt.subplots(figsize=(11, 2.4))
    ax.set_xlim(-1.5, 101.5)
    ax.set_ylim(0, 24)
    ax.axis("off")
    w, gap, h, y = 16.0, 5.0, 18, 3
    for i, (head, sub) in enumerate(steps):
        x = i * (w + gap)
        last = i == len(steps) - 1
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.5",
                                    fc=PALETTE["orange"] if last else PALETTE["light"],
                                    ec=PALETTE["navy"], lw=1.2))
        txt = "white" if last else PALETTE["navy"]
        ax.text(x + w / 2, y + h * 0.7, head, ha="center", va="center", fontsize=10.5,
                fontweight="bold", color=txt)
        ax.text(x + w / 2, y + h * 0.32, sub, ha="center", va="center", fontsize=8.6,
                color=txt, linespacing=1.25)
        if not last:
            ax.add_patch(FancyArrowPatch((x + w + 0.7, y + h / 2), (x + w + gap - 0.7, y + h / 2),
                                         arrowstyle="-|>", mutation_scale=14,
                                         color=PALETTE["navy"], lw=1.6))
    fig.savefig(OUT / "Fig_M4-3_imported_inflation_chain.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Fig M4-4: Sri Lanka's rupee collapse against India's gradual movement
# ---------------------------------------------------------------------------
def fig_sri_lanka_vs_india():
    lk, inr = load_fred("EXSLUS"), load_fred("EXINUS")
    start, end, base = "2021-01-01", "2024-12-01", "2022-01-01"

    fig, ax = plt.subplots(figsize=(10, 4.8))
    for df, label, color in [(lk, "Sri Lankan rupee", PALETTE["red"]),
                             (inr, "Indian rupee", PALETTE["navy"])]:
        d = df[(df["date"] >= start) & (df["date"] <= end)].copy()
        d["index"] = 100 * d["value"] / df.loc[df["date"] == base, "value"].iloc[0]
        ax.plot(d["date"], d["index"], color=color, lw=2.2, label=label)

    notes = [
        ("2022-03-01", 128, "Mar 2022:\nrupee allowed\nto float", (-120, 30)),
        ("2022-04-01", 158, "Apr 2022:\nforeign debt\npayments stopped", (-140, 12)),
        ("2023-03-01", 162, "Mar 2023:\nIMF programme\napproved", (30, 26)),
    ]
    lk_i = lk.set_index("date")["value"] / lk.loc[lk["date"] == base, "value"].iloc[0] * 100
    for date, _, text, offset in notes:
        d = pd.Timestamp(date)
        ax.annotate(text, xy=(d, lk_i[d]), xytext=offset, textcoords="offset points",
                    fontsize=8.6, color="#333333",
                    arrowprops=dict(arrowstyle="-", color=PALETTE["grey"], lw=0.8))

    ax.axhline(100, color=PALETTE["grey"], lw=0.8, ls="--")
    ax.text(pd.Timestamp("2021-01-15"), 102, "January 2022 = 100", fontsize=8.6,
            color=PALETTE["grey"])
    ax.set_ylim(85, 195)
    ax.set_ylabel("Local currency per US dollar\n(index, January 2022 = 100)")
    ax.set_xlabel("Month")
    ax.legend(frameon=False, loc="lower right", bbox_to_anchor=(1.0, 0.25))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    fig.savefig(OUT / "Fig_M4-4_sri_lanka_vs_india_index.png")
    plt.close(fig)


if __name__ == "__main__":
    fig_rupee_history()
    fig_shocks()
    fig_imported_inflation()
    fig_sri_lanka_vs_india()
    print("Figures written to", OUT)
