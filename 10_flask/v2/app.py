# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask

app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("about to print __name__...") # prints this in the terminal
    print(__name__)  # where will this go?
    #also prints in the terminal
    return "No hablo queso!" # prints on the website


app.run()
