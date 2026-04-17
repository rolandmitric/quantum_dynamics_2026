from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 400)
f = np.exp(x)

p = 3.5
x0 = np.log(p)
g = p * x0 - np.exp(x0)

y_blue = p * x
y_green = p * x - g
y0 = np.exp(x0)

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, f, label=r'$f(x)=e^x$', color='red', lw=4)
ax.plot(x, y_blue, label=r'$px$', color='blue', lw=2)
ax.plot(x, y_green, label=r'$px-g(p)$', color='green', lw=2)

ax.scatter([x0], [y0], color='black', zorder=5)
ax.axvline(x0, color='gray', ls='--', lw=1)

label_box = dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.9)

ax.annotate(
    r'$x_0=\ln p$',
    xy=(x0, 0),
    xytext=(x0 - 0.38, -1.15),
    arrowprops=dict(arrowstyle='->', color='black', lw=1),
    fontsize=11,
    bbox=label_box
)

ax.annotate(
    r'$(x_0,f(x_0))$',
    xy=(x0, y0),
    xytext=(x0 + 0.18, y0 + 1.0),
    arrowprops=dict(arrowstyle='->', color='black', lw=1),
    fontsize=11,
    bbox=label_box
)

ax.plot([0, 0], [-g, 0], color='purple', lw=3, zorder=4)
ax.annotate(
    r'$g(p)$ at $x=0$',
    xy=(0, -g / 2),
    xytext=(0.22, -0.45),
    arrowprops=dict(arrowstyle='->', color='purple', lw=1),
    color='purple',
    fontsize=11,
    bbox=label_box
)

ax.plot([x0, x0], [y0, p * x0], color='purple', lw=2, ls='--', zorder=4)
ax.annotate(
    r'$g(p)$ at $x=x_0$',
    xy=(x0, y0 + g / 2),
    xytext=(x0 - 0.78, y0 + 0.28),
    arrowprops=dict(arrowstyle='->', color='purple', lw=1),
    color='purple',
    fontsize=11,
    bbox=label_box
)

ax.set_xlim(0, 2)
ax.set_ylim(-1.5, 8)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

fig.tight_layout()

output_dir = Path("_static/figures")
output_dir.mkdir(parents=True, exist_ok=True)

png_path = output_dir / "legendre_tangent_geometry.png"
pdf_path = output_dir / "legendre_tangent_geometry.pdf"

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")

print(f"Saved to {png_path}")
print(f"Saved to {pdf_path}")

plt.show()
