"""Competitor landscape analysis: which capabilities do existing Saudi/GCC players cover, and where are the gaps?
Input: landscape.csv, built from desk research (public descriptions of each player).
Scores: 1 = clearly offered, 0.5 = partial/emerging, 0 = not a focus. These are my own judgements from public
descriptions, not measured data."""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("landscape.csv").set_index("player")
caps = [c for c in df.columns if c != "type"]
labels = {"growth_strategy": "Growth strategy", "training": "Training",
          "freelancer_marketplace": "Freelancer marketplace", "managed_services": "Managed services",
          "ai_data_positioning": "AI / data positioning"}

others = df[df.type != "BAS"]
summary = pd.DataFrame({
    "players_covering": (others[caps] >= 1).sum(),
    "players_partial": ((others[caps] > 0) & (others[caps] < 1)).sum(),
}).rename(index=labels)
summary["coverage_pct"] = (summary.players_covering / len(others) * 100).round(0)
summary = summary.sort_values("coverage_pct")
print(summary)
summary.to_csv("gap_summary.csv")

# Breadth: how many capabilities each player combines
df["capabilities_combined"] = (df[caps] >= 1).sum(axis=1)
print(df["capabilities_combined"].sort_values(ascending=False))

# Heatmap
fig, ax = plt.subplots(figsize=(9, 5))
ax.imshow(df[caps].values, cmap="Greens", vmin=0, vmax=1.2)
ax.set_xticks(range(len(caps)), [labels[c] for c in caps], rotation=25, ha="right")
ax.set_yticks(range(len(df)), df.index)
for i in range(len(df)):
    for j, c in enumerate(caps):
        v = df.iloc[i][c]
        ax.text(j, i, {1: "Yes", 0.5: "Partial", 0: ""}[v], ha="center", va="center", fontsize=9)
ax.set_title("Capability coverage across the Saudi/GCC landscape (desk research)")
plt.tight_layout(); plt.savefig("landscape_heatmap.png", dpi=130)
