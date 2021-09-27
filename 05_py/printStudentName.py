# Tina Nguyen
# Trio: Tami Takada, Tina Nguyen, Yusuf Elsharawy
# SoftDev
# K05 -- A program that can print a student from period 1 or 2, either at random or by the user's choice.
# 2021-09-27

# Summary: We worked together to revise the name printing code, and
# we decided to incorporate Yusuf's idea of having two separate functions, one
# for printing a random name, and one for printing a name at a specific index.
# Yusuf agreed that using files was probably better than hard-coding the array
# of names, so we kept that part. Tina also had the idea of using command-line
# arguments, so we used them to tell the program what to do.

# Discoveries: I learned a lot about Python syntax and how it differs from Java.
# I learned about dictionaries in Python and how they're used as well.
# I learned a lot about command line arguments in Python and how they're used in code.

# Questions: How else could one write this program?
# Comments: N/A

import random
import sys

# First argument is period, second argument is either "random" or a number
# If the second argument is "random", the output is a random name from that period
# If the second argument is a number, the output is a name that corresponds with that index in the alpabetical lsit

# A tuple to represent all softdev periods:
usedPeriods = (1, 2) # Add more periods here (eg. `(1, 2, 5, 9)`) if necessary

# Using a dict to store the mapping between period #'s and lists of names
# e.g. {1: ["John Doe", "Mary Jane"], 2: ["Abraham Lincoln", "Thomas Jefferson"]}
# Better than a list for this purpose, especially since periods may be disjoint (such as 3 & 9)
# And we can access period X with `periodLists[X]` as opposed to `periodLists[X - 1]`
nameLists = {}

# List of ALL student names, used to print a completely random student's name
allNames = []

# Converts a name to a case-insensitive key, to sort by last name
# e.g. "Yusuf Elsharawy" -> "ELSHARAWY YUSUF"
def alphSortKey(name):
    words = name.split()

    return ' '.join(        # joins by spaces
        map(str.upper,      # converts to uppercase
            reversed(words) # reverses order of words
        )                   # ^ from bottom to top
    )

# Reads from files to obtain student names:
# Each file contains the list of names for one period, has one student's name on each line.
def initNameList():
    for i in usedPeriods:
        pd = []

        with open(f"students_pd{i}.txt") as file:
            for line in file:
                name = line.strip()
                pd.append(name)

        pd.sort(key=alphSortKey)
        nameLists[i] = pd
        allNames.extend(pd)

def printRandomName():
    print(random.choice(allNames))

# Writes message (+ newline) to standard error & exits
def exitWithError(errorMsg):
    sys.stderr.write(errorMsg+'\n')
    sys.stderr.flush()
    exit()

# Parses string as integer & returns; exits with error if it fails
def tryParseInt(s):
    try:
        return int(s)
    except ValueError:
        exitWithError(f'could not parse as int: "{s}"')


def main():
    initNameList()
    if 1 >= len(sys.argv):
        exitWithError(f"missing required argument #1")
    if sys.argv[1] == 'random':
        printRandomName()
    else:
        periodNum = tryParseInt(sys.argv[1])
        if periodNum not in usedPeriods:
            exitWithError(f"invalid period number {periodNum}")

        nameList = nameLists[periodNum]
        if 2 >= len(sys.argv):
            exitWithError(f"missing required argument #2")
        if sys.argv[2] == 'random':
            print(random.choice(nameList))
        else:
            nameIdx = tryParseInt(sys.argv[2])
            if nameIdx >= len(nameList) or nameIdx < -len(nameList):
                exitWithError(f"invalid student number {nameIdx} of period {periodNum}")
            print(nameList[nameIdx])

def testWithArgs(*args):
    global nameLists, allNames
    nameLists = {}
    allNames = []
    sys.argv = ['print_name.py', *args]
    main()

def tests():
    testWithArgs('random')
    testWithArgs('1', 'random')
    testWithArgs('2', 'random')
    testWithArgs('1', '10')
    testWithArgs('2', '10')
    testWithArgs('1', '-10')
    testWithArgs('2', '-10')

if __name__ == '__main__':
    main()
##    tests()
