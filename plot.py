from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, ListedColormap

from model import simulate


rows = simulate(count=20, dawdle_chance=0.3, steps=200, seed=1)

cmap = ListedColormap(
    ["white", "#313695", "#4575b4", "#74add1", "#fdae61", "#f46d43", "#a50026"]
)
norm = BoundaryNorm([-1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5], cmap.N)

fig, ax = plt.subplots(figsize=(12, 8))
image = ax.imshow(
    rows,
    cmap=cmap,
    norm=norm,
    aspect="auto",
    interpolation="nearest",
    origin="upper",
)
ax.set(title="Traffic space-time diagram", xlabel="Cell", ylabel="Step")
fig.colorbar(image, ax=ax, ticks=range(6), label="Car speed (cells per step)")
fig.savefig(Path(__file__).with_name("jam.png"), dpi=150, bbox_inches="tight")
