# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask

app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("about to print __name__...") # prints in terminal
    print(__name__)  # where will this go?
    # prints in terminal
    return "No hablo queso!" # prints in website


app.debug = True # tells you details about an error if you were to get one
app.run()
