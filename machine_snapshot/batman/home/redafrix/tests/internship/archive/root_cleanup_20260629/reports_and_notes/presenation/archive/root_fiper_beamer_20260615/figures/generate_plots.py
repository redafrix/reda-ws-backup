import os
import matplotlib.pyplot as plt
import numpy as np

# Ensure figures folder exists
os.makedirs("/home/redafrix/tests/internship/presenation/figures", exist_ok=True)

# Data
# 4 categories:
# 1. Tâches vues - Échecs détectés
# 2. Tâches vues - Fausses alertes
# 3. Hors tâches vues - Échecs détectés
# 4. Hors tâches vues - Fausses alertes
categories = [
    "Tâches vues\n(Échecs détectés)",
    "Tâches vues\n(Fausses alertes)",
    "Hors tâches vues\n(Échecs détectés)",
    "Hors tâches vues\n(Fausses alertes)"
]

base_scores = [95.8, 14.2, 86.0, 26.0]
top8_scores = [97.5, 15.0, 89.2, 23.0]

x = np.arange(len(categories))
width = 0.3

# Palette
color_base = "#173A5E"  # Bleu foncé
color_top8 = "#E88C2A"  # Orange doux

fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)

rects1 = ax.bar(x - width/2, base_scores, width, label="Sans incertitude", color=color_base)
rects2 = ax.bar(x + width/2, top8_scores, width, label="8 signaux d'incertitude sélectionnés", color=color_top8)

ax.set_ylabel("Pourcentage (%)", fontsize=11, fontweight="bold", color="#173A5E")
ax.set_title("Comparaison Offline : Sans incertitude vs 8 signaux sélectionnés", fontsize=12, fontweight="bold", pad=15, color="#173A5E")
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10, fontweight="bold", color="#2D3748")
ax.set_ylim(0, 115)
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Remove top/right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#718096')
ax.spines['bottom'].set_color('#718096')

# Add values on top of bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f"{height:.1f}%",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9.5, fontweight="bold", color="#2D3748")

autolabel(rects1)
autolabel(rects2)

ax.legend(loc="upper right", frameon=False, fontsize=10)

plt.tight_layout()
plt.savefig("/home/redafrix/tests/internship/presenation/figures/offline_results.png", bbox_inches='tight', transparent=True)
print("Plot generated successfully at /home/redafrix/tests/internship/presenation/figures/offline_results.png")
