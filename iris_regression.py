#!/usr/bin/env python3

"""
Basic iris data loader
"""

import pandas as pd
from scipy import stats


def load_data(filename):
    return pd.read_csv(filename, sep="\t")


def run_regression(data):
    x = data["petal_length_cm"]
    y = data["sepal_length_cm"]
    return stats.linregress(x, y)


def main():
    df = load_data("iris.csv")

    species_list = df["species"].unique()

    for species in species_list:
        species_data = df[df["species"] == species]
        result = run_regression(species_data)
        print(species, result.slope)


if __name__ == "__main__":
    main()
