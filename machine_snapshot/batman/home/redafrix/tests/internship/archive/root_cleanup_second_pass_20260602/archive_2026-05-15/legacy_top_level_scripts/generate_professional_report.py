import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_professional_tables():
    # ID Data
    id_data = {
        "Step": [10, 20, 50, 100, 200],
        "Accuracy (%)": [74.4, 82.0, 91.8, 95.3, 97.0],
        "AUC-ROC": [0.8295, 0.8986, 0.9676, 0.9836, 0.9677]
    }
    
    # OOD Data
    ood_data = {
        "Step": [10, 20, 50, 100, 200],
        "Accuracy (%)": [55.5, 47.2, 43.4, 40.6, 70.2],
        "AUC-ROC": [0.5388, 0.4496, 0.4472, 0.3555, 0.4210]
    }

    df_id = pd.DataFrame(id_data)
    df_ood = pd.DataFrame(ood_data)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    plt.subplots_adjust(wspace=0.3)

    # Styling function
    def render_table(ax, df, title, color):
        ax.axis('off')
        ax.set_title(title, fontsize=18, fontweight='bold', pad=20)
        
        table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
        
        # Professional Styling
        table.auto_set_font_size(False)
        table.set_fontsize(14)
        table.scale(1.2, 2.5)
        
        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor(color)
            else:
                if row % 2 == 0:
                    cell.set_facecolor('#f2f2f2')
                else:
                    cell.set_facecolor('white')
            cell.set_edgecolor('#d9d9d9')

    render_table(ax1, df_id, "In-Distribution (ID) Results", "#2E5077")
    render_table(ax2, df_ood, "Out-of-Distribution (OOD) Results", "#A91D3A")

    plt.suptitle("V8 Balanced Experiment Analysis", fontsize=22, fontweight='bold', y=1.05)
    
    plt.savefig("v8_balanced_comparison.png", bbox_inches='tight', dpi=300)
    print("Professional comparison plot saved as v8_balanced_comparison.png")

if __name__ == "__main__":
    create_professional_tables()
