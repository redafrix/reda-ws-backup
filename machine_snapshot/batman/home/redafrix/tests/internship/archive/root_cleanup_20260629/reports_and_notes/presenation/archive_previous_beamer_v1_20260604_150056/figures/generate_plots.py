import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure directory exists
os.makedirs("/home/redafrix/tests/internship/presenation/figures", exist_ok=True)

# Data
# metrics = [False Alarm (FA), Recall (Det), Early Det@25, Early Det@50]
labels = ["Faux Positifs\n(FA)", "Taux de Détection\n(Recall)", "Détection précoce\n(Det@25%)", "Détection tardive\n(Det@50%)"]

# all_tasks_full (seen split)
base_seen = [14.23, 95.78, 54.01, 89.03]
top8_seen = [15.01, 97.47, 64.98, 89.45]

# ood_last2_taskids_full (OOD split)
base_ood = [25.96, 86.02, 39.78, 78.49]
top8_ood = [22.98, 89.25, 37.63, 77.42]

x = np.arange(len(labels))
width = 0.35

# Color Palette: steel blue for base, muted orange for top-8
color_base = "#3A6073"
color_top8 = "#F28E2B"

# Plot 1: Split Vu / Toutes tâches (all_tasks_full)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Plot Left: Seen split
rects1_1 = ax1.bar(x - width/2, base_seen, width, label="Sans incertitude (Base)", color=color_base)
rects1_2 = ax1.bar(x + width/2, top8_seen, width, label="8 signaux d'incertitude sélectionnés", color=color_top8)

ax1.set_title("Split Vu / Toutes tâches (all_tasks_full)", fontsize=11, fontweight="bold", pad=12, color="#1A365D")
ax1.set_xticks(x)
ax1.set_xticklabels(labels, fontsize=8.5)
ax1.set_ylabel("Pourcentage (%)", fontsize=9.5)
ax1.set_ylim(0, 115)
ax1.grid(axis='y', linestyle='--', alpha=0.5)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color('#718096')
ax1.spines['bottom'].set_color('#718096')

# Add values on top of bars
def autolabel(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f"{height:.1f}%",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, color="#2D3748")

autolabel(rects1_1, ax1)
autolabel(rects1_2, ax1)

# Plot Right: OOD split
rects2_1 = ax2.bar(x - width/2, base_ood, width, label="Sans incertitude (Base)", color=color_base)
rects2_2 = ax2.bar(x + width/2, top8_ood, width, label="8 signaux d'incertitude sélectionnés", color=color_top8)

ax2.set_title("Split Hors Distribution (ood_last2_taskids_full)", fontsize=11, fontweight="bold", pad=12, color="#1A365D")
ax2.set_xticks(x)
ax2.set_xticklabels(labels, fontsize=8.5)
ax2.set_ylabel("Pourcentage (%)", fontsize=9.5)
ax2.set_ylim(0, 115)
ax2.grid(axis='y', linestyle='--', alpha=0.5)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color('#718096')
ax2.spines['bottom'].set_color('#718096')

autolabel(rects2_1, ax2)
autolabel(rects2_2, ax2)

# Global Legend placed at the bottom
handles, labels_legend = ax1.get_legend_handles_labels()
fig.legend(handles, labels_legend, loc='lower center', ncol=2, fontsize=9.5, frameon=False)
plt.subplots_adjust(bottom=0.2, wspace=0.3)

plt.savefig("/home/redafrix/tests/internship/presenation/figures/offline_comparison.png", bbox_inches='tight', transparent=True)
print("Plot generated successfully at /home/redafrix/tests/internship/presenation/figures/offline_comparison.png")
