"""
Wanderers: Shriya Anand, Lucas Lee, Tina Nugget
SoftDev
K13 -- Occupation Flask App Template
2021-10-13
"""

from flask import Flask, render_template
import occupations
# imports methods from occupations.py

app = Flask(__name__)  # create instance of class Flask


@app.route("/occupyflaskst")  # assign fxn to route
def display_occupation():
    jobs = occupations.read_occupations("./data/occupations.csv")
    # creates dictionary called jobs which is a dictionary returned
    # from read_occupations() which reads through occupations.csv and makes the
    # keys job occupations and the values the percentages associated with it

    choice = occupations.choose_from_dict(jobs)
    # this prints out a randomly chosen occupation (weighted by the percents)
    # that is returned from choose_from_dict() and skips two lines


    return render_template('tablified.html', choice=choice, occupations=jobs)


    return output


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True  # enable auto-reload upon code change
    app.run()
