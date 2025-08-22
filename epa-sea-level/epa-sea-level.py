import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


df = pd.read_csv("epa-sea-level.csv")


def draw_plot():
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    slope1, intercept1, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    ax.plot(years_extended, intercept1 + slope1*years_extended, 'r', label="All data fit")


    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    ax.plot(years_recent, intercept2 + slope2*years_recent, 'g', label="2000+ data fit")


    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return fig

if __name__ == "__main__":
    draw_plot()
    print("Plot saved as sea_level_plot.png")
