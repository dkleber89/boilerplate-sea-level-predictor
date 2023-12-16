"""Sea Level Plot Module"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    """Draw sea level plot

    Returns:
        Axes: Return axes for test
    """
    # Read data from file
    df_all = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    axes = df_all.plot.scatter(figsize=(10,5), y="CSIRO Adjusted Sea Level", x="Year")

    # Create first line of best fit
    all_line = linregress(df_all["Year"], df_all["CSIRO Adjusted Sea Level"])
    plt.plot(
        range(1880, 2051, 1),
        all_line.slope * range(1880, 2051, 1) + all_line.intercept
    )

    # Create second line of best fit
    df_ge_2000 = df_all[df_all["Year"] >= 2000]
    ge_2000_line = linregress(df_ge_2000["Year"], df_ge_2000["CSIRO Adjusted Sea Level"])
    plt.plot(
        range(2000, 2051, 1),
        ge_2000_line.slope * range(2000, 2051, 1) + ge_2000_line.intercept
    )

    # Add labels and title
    axes.set(
        title="Rise in Sea Level",
        ylabel="Sea Level (inches)",
        xlabel="Year"
    )

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return plt.gca()
