# Setting the Bar: Shyne Choi, Ella Krechmer, Tina Nguyen
# SoftDev
# K15:Sessions Greetings
# 2021-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
         #

from random import *
import os

#the conventional way:
#from flask import Flask, render_template, request

from flask import session
app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32) #creates random alphanumeric code



'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    # print("\n\n\n")
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    # print("***DIAG: request.args['password']  ***")
    # print(request.args['password'])
     if (session.get("username") != None):
         # if there's an existing session, shows welcome page
        return render_template( 'response.html', username=session.get("username"))
     return render_template('login.html' )
     #shows login page


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    '''
    Function for logging in. Checks if the user input matches the hard coded
    login info and reports back what errors there are. 
    '''
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)

    #prints username and headers in the terminal
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)


    myuser="settingthebar"
    mypass="intertoobz"
    #hardcoded login info

    #authenicate will go to the response page which will use response.html
    #we are retrieving entered username and password here
    username=request.args['username']
    password=request.args['password']
    #(username==myuser and password==mypass)
    # if (username!=myuser or password!=mypass):
    #     raise Exception("wrong login")
    # try:
    #     return render_template( 'response.html', username=request.args['username'], password=request.args['password'])  #response to a form submission
    # except if ((username!=myuser or password!=mypass)):
    #     return render_template( 'login.html' )

    if (username==myuser and password==mypass): # if login info matches
        session["username"] = username
        return render_template( 'response.html', username = session["username"])
    elif (username=="" or password==""): # checks for blank inputs
        return render_template('login.html', error="Cannot submit blank username or password")
    elif (username!=myuser):
        return render_template('login.html', error="Incorrect username")
    elif (password!=mypass):
        return render_template('login.html', error="Incorrect password")

@app.route("/logout")
def logout():
    '''
    Function for the logout button. Sets username to  None and pops the session,
    then returning to the login page.
    '''
    session["username"] = None
    session.pop("username", None)
    return disp_loginpage()

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
