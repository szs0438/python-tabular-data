#!/usr/bin/env python3

"""
Basic iris data loader
"""

import pandas as pd


def load_data(filename):
    return pd.read_csv(filename, sep="\t")


def main():
    df = load_data("iris.csv")
    print(df.head())


if __name__ == "__main__":
    main()
