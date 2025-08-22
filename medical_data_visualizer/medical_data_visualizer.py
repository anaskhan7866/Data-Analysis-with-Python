import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)


df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():
    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    df_cat = df_cat.value_counts().reset_index(name='total')

    g = sns.catplot(x="variable", y="total", hue="value", col="cardio",
                    data=df_cat, kind="bar")

    fig = g.fig
    fig.savefig("catplot.png")
    return fig

def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, cmap="coolwarm", ax=ax)

    fig.savefig("heatmap.png")
    return fig

if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
    print("Plots saved as catplot.png and heatmap.png")
