#!/usr/bin/env python3

"""
Basic iris data loader
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def load_data(filename):
    return pd.read_csv(filename)


def run_regression(data):
    x = data["petal_length_cm"]
    y = data["sepal_length_cm"]
    return stats.linregress(x, y)

def plot_regression(data, species, regression):
    x = data["petal_length_cm"]
    y = data["sepal_length_cm"]

    plt.figure()
    plt.scatter(x, y)
    plt.plot(x, regression.slope * x + regression.intercept)

    plt.xlabel("Petal length")
    plt.ylabel("Sepal length")
    plt.title(species)

    plt.savefig(f"{species}.png")
    plt.close()


def main():
    df = load_data("iris.csv")

    species_list = df["species"].unique()

    for species in species_list:
        species_data = df[df["species"] == species]
        reg = run_regression (species_data)
        print (species, reg.slope)
        plot_regression (species_data, species, reg)


if __name__ == "__main__":
    main()
