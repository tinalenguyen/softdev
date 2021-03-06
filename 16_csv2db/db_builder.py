#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
def open_file():
    # Opens file and formats into dictionary as Job Class: Percentage

    with open('courses.csv', newline='') as f:
         course = csv.dictReader(f)


command = "INSERT INTO ella VALUES ('shyne', 0);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement
command = "SELECT * FROM ella;"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)

#==========================================================

db.commit() #save changes
db.close()  #close database
