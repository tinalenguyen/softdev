"""
Pasta Noodles: Christopher Liu, Tina Nguyen, Tami Takada
SoftDev
K06 -- Weighted Random Occupation Picker
2021-09-28
"""

# Our approach.
# The program has two parts: reading the CSV file and picking a random
# occupation, weighted by the specified percentages. The first part involves
# csv module, which allows us to not worry about edge cases like when commas
# are within a cell. Ignoring the first header line, we convert all of the rows
# to dictionary entries, converting the percentage to a float in the process.
# The last important note is that we replace "Total" with "Other" and assign
# it a percentage equal to 100 minus the total percentage, assuming that jobs
# not listed in the occupations list take up the remaining percentage points.
# Lastly, we can use random.choices(), which is a weighted selection method
# that works quite easily with the dictionary entries we have. We then return
# the selected job class.

import csv
import random


def read_occupations(filename: str) -> dict:
    """Reads a CSV file containing job classes and percentages and returns a
    dictionary with the job class as the key and the percentage as a float.
    Ignores the first header line and adds an 'Other' category for percentages
    outside of the 'Total'."""

    occupations = {}
    with open(filename, newline="") as csvfile:
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


def choose_from_dict(occupations: dict) -> str:
    """Picks an occupation randomly using the percentage weights in the given
    occupations dictionary."""

    job_classes = list(occupations.keys()) # turns keys into a list for use in random.choice
    percentages = list(occupations.values()) # turns values from dict into a list for use in random.choice

    choice = random.choices(job_classes, weights=percentages)[0] # random.choices picks a random job with weighted percentages and returns one value
    return choice


def random_occupation(filename: str) -> str:
    """Returns a random occupation based on the job classes and percentage
    weights provided in the given CSV file."""

    occupations = read_occupations(filename) # reads the file
    return choose_from_dict(occupations) # returns a random occupation to print in the main function


def main():
    print(random_occupation("occupations.csv"))


if __name__ == "__main__":
    main()
