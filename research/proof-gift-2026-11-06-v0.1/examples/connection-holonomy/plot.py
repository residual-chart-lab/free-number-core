"""Show actual exact comparison outputs; plotting floats are presentation only."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

parser = argparse.ArgumentParser()
parser.add_argument("--run", type=Path, required=True)
args = parser.parse_args()
for candidate in ("C:/Windows/Fonts/meiryo.ttc", "C:/Windows/Fonts/YuGothM.ttc"):
    if Path(candidate).exists():
        prop = font_manager.FontProperties(fname=candidate)
        font_manager.fontManager.addfont(candidate)
        plt.rcParams["font.family"] = prop.get_name()
        break
plt.rcParams["axes.unicode_minus"] = False
r = json.loads((args.run / "RESULTS.json").read_bytes())["display_summary"]
fig, axes = plt.subplots(1, 2, figsize=(11, 5.3))
fig.subplots_adjust(top=0.76, bottom=0.15, left=0.075, right=0.98, wspace=0.32)
fig.suptitle("自由数の残差 × 接続に沿う運搬\n有理数による厳密計算：内部状態と残差の無次元応答", fontsize=12, y=0.965)
labels = ["操作を挟まない", "完成後に追加", "途中に挟む"]
for offset, key, label, color in [(-0.17, 0, "経路A", "#3274a1"), (0.17, 1, "経路B", "#e1812c")]:
    vals = [r["unprobed"][key], r["appended"][key], r["midpoint"][key]]
    axes[0].bar([i + offset for i in range(3)], vals, width=0.31, label=label, color=color)
axes[0].set_xticks(range(3), labels, fontsize=9)
axes[0].set_ylim(-1.15, 1.15)
axes[0].set_ylabel("共通の測定への応答")
axes[0].set_title("同じ完成値でも、途中の作用は違う", fontsize=10)
axes[0].legend(fontsize=9)
axes[1].bar([0, 1], r["same_endpoint_routes_residual_response"], color=["#3274a1", "#55a868"], width=0.5)
axes[1].set_xticks([0, 1], ["直接運ぶ", "一周してから運ぶ"], fontsize=9)
axes[1].set_title("同じ地点へ届いた残差を比較", fontsize=10)
axes[1].set_ylabel("同じ基準で測った残差の応答")
for ax in axes:
    ax.axhline(0, color="#555", lw=0.8)
    ax.grid(axis="y", alpha=0.18)
fig.savefig(args.run / "transport-comparison.png", dpi=160)
fig.savefig(args.run / "transport-comparison.svg")
