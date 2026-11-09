"""Figure M1-3: India's remittance inflows, 2000-2025 (World Bank WDI).

Data: World Bank, World Development Indicators, series BX.TRF.PWKR.CD.DT
"Personal remittances, received (current US$)", last updated 8 Oct 2026.
Values below are in US$ billion, rounded to one decimal.
Run:  python3 make_remittances_chart.py   (writes remittances.pdf and remittances.png)
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
FONT_DIR = HERE.parent / "fonts"
for f in FONT_DIR.glob("SourceSans3_*.ttf"):
    font_manager.fontManager.addfont(str(f))
plt.rcParams["font.family"] = "Source Sans 3"

years = list(range(2000, 2026))
usd_bn = [12.9, 14.3, 15.7, 21.0, 18.8, 22.1, 28.3, 37.2, 50.0, 49.2,
          53.5, 62.5, 68.8, 70.0, 70.4, 68.9, 62.7, 69.0, 78.8, 83.3,
          83.1, 89.4, 111.2, 119.5, 137.7, 150.7]

NAVY = "#1F3A5F"      # chapter navy (main series)
ORANGE = "#C8641E"    # chapter accent (latest year)
INK = "#222222"
MUTED = "#6B6B6B"
GRID = "#E3E3E3"

fig, ax = plt.subplots(figsize=(4.7, 2.6), dpi=300)
colors = [NAVY] * (len(years) - 1) + [ORANGE]
ax.bar(years, usd_bn, width=0.72, color=colors, edgecolor="white", linewidth=0.6, zorder=3)

# Recessive axes and grid
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.spines["bottom"].set_color("#9A9A9A")
ax.yaxis.grid(True, color=GRID, linewidth=0.7, zorder=0)
ax.tick_params(axis="y", length=0, colors=MUTED, labelsize=8.5)
ax.tick_params(axis="x", colors=MUTED, labelsize=8.5, length=2.5)
ax.set_xticks([2000, 2005, 2010, 2015, 2020, 2025])
ax.set_xlim(1999.3, 2025.7)
ax.set_ylim(0, 170)
ax.set_yticks([0, 40, 80, 120, 160])
ax.set_ylabel("US$ billion", color=MUTED, fontsize=8.5)

# Selective direct labels (first and last year only)
ax.annotate("$12.9 bn", (2000, 12.9), xytext=(0, 4), textcoords="offset points",
            ha="center", va="bottom", fontsize=8.5, color=INK)
ax.annotate("$150.7 bn\n(2025)", (2025, 150.7), xytext=(-4, 4), textcoords="offset points",
            ha="right", va="bottom", fontsize=8.5, color=INK, fontweight="semibold")

fig.tight_layout(pad=0.4)
fig.savefig(HERE / "remittances.pdf")
fig.savefig(HERE / "remittances.png", dpi=300)
print("saved")
