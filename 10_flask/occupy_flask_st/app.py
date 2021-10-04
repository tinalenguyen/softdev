# STD Trio: Christopher Liu, Tina Nguyen, Tami Takada
# SoftDev
# K10 -- Occupation Selector Flask App
# 2021-10-04

from flask import Flask

import occupations
# imports methods from occupations.py

app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def display_occupation():
    output = "STD Trio: Christopher Liu, Tina Nguyen, Tami Takada</br></br>"
    # prints out trio name and roster and skips two lines

    jobs = occupations.read_occupations("occupations.csv")
    # creates dictionary called jobs which is a dictionary returned
    # from read_occupations() which reads through occupations.csv and makes the
    # keys job occupations and the values the percentages associated with it

    output += "<strong>Selected Job:</strong> "
    # the randomly chosen job will be printed after this string
    output += occupations.choose_from_dict(jobs) + "</br></br>"
    # this prints out a randomly chosen occupation (weighted by the percents)
    # that is returned from choose_from_dict() and skips two lines


    output += "<strong>List of Jobs:</strong></br>"
    # precedes a printed list of all the jobs in occupations.csv
    for job in jobs.keys():
    # loops through all the keys in the dictionary and prints the job out,
    # going to the next line each time it prints
        output += job + "</br>"

    return output


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True  # enable auto-reload upon code change
    app.run()
