"""
Pasta Noodles: Christopher Liu, Tina Nguyen, Tami Takeda
SoftDev
K06 -- Weighted Random Occupation Picker
2021-09-28
"""

import csv
import random


def read_occupations() -> dict:
    """Reads a CSV file containing job classes and percentages and returns a
    dictionary with the job class as the key and the percentage as a float.
    Ignores the first header line and adds an 'Other' category for percentages
    outside of the 'Total'."""

    OCCUPATIONS_FILE = "06_py-csv/occupations.csv"

    occupations = {}
    with open(OCCUPATIONS_FILE, newline="") as csvfile:
        reader = csv.reader(csvfile)

        # We ignore the first header line with the column titles.
        next(reader)

        for index, row in enumerate(reader):
            job_class = row[0] # added to dict as keys
            percentage = row[1] # added to dict as values
            occupations[job_class] = float(percentage) # float for decimals

    # We mark everything not in the occupations list as "Other".
    total_percentage = occupations["Total"]
    occupations["Other"] = 100 - total_percentage
    del occupations["Total"]

    return occupations


def choose_occupation(occupations: dict) -> str:
    """Picks an occupation randomly using the percentage weights in the given
    occupations dictionary."""

    job_classes = list(occupations.keys()) # turns keys into a list for use in random.choice
    percentages = list(occupations.values()) # turns values from dict into a list for use in random.choice

    choice = random.choices(job_classes, weights=percentages)[0] # random.choices picks a random job with weighted percentages and returns one value
    return choice


def main():
    occupations = read_occupations() 
    print(choose_occupation(occupations))


if __name__ == "__main__":
    main()
