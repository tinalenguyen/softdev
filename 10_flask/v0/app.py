# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask

app = Flask(__name__)  # Q0: Where have you seen similar syntax in other langs?


@app.route("/")  # Q1: What points of reference do you have for meaning of '/'?
# this makes the app go to what is essentially the main directory
def hello_world():
    print(__name__)  # Q2: Where will this print to? Q3: What will it print?
    # this will print the name in the terminal
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?
    # this will return in the website URL provided in the terminal


app.run()  # Q4: Where have you seen similar construcs in other languages?
# this just runs the app, i've never seen this construct anywhere else
