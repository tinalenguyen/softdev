# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask

app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign fxn to route
def hello_world():
    print("the __name__ of this module is... ") # prints in terminal
    print(__name__) # prints in terminal
    return "No hablo queso!" # prints in website


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True  # enable auto-reload upon code change
    # reloads the page if you make a change in the python file
    app.run()
