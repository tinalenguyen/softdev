# Tami Takada, Tina Nguyen, Yusuf Elsharawy
# SoftDev
# A function that prints the name of a student from either period 1 or 2, at the index-th position in the list of all students for that period when sorted alphabetically.
# 2021-09-22

# Summary: I worked with Tina and Yusuf to revise the name printing code, and
# we decided to incorporate Yusuf's idea of having two separate functions, one
# for printing a random name, and one for printing a name at a specific index.
# Yusuf agreed that using files was probably better than hard-coding the array
# of names, so we kept that part.

# Discoveries: From looking at Yusuf's code, I re-discovered using random in
# Python. I also didn't know about the random choice function.

# Questions: N/A
# Comments: N/A

import random
import sys
# first argument is period, second argument is either "random" or a number
# if the second argument is random, the output is a random name from that period
# if the second argument is a number, the output is a name that corresponds with that index in the alpabetical lsit
pds = []

try:
    asInt = int(sys.argv[1])
except ValueError:
    print("Enter a period number")

    int ind = int(sys.argv[2])

    if int(sys.argv[1]) = 1:
        printNames(1, ind)

    if int(sys.argv[1]) = 2:
        printNames(2, ind)






def initNameList():
    for i in range(2):
        pd = []
        fileName = 'softdev_students_pd' + str(i + 1) + '.txt'

        with open(fileName) as reader:
            name = reader.readline()
            while name != '':
                pd.append(name.rstrip('\n'))
                name = reader.readline()

        pd.sort()
        pds.append(pd)

def printNames(period, index):
    if period > 0 and period < 3:
        if index < len(pds[period - 1]):
            print(pds[period - 1][index])
        else:
            print('Student does not exist')
    else:
        print('Period does not exist')

def printRandomName():
    singleArr = []
    for i in range(len(pds)):
        singleArr += pds[i]

    print(random.choice(singleArr))

initNameList()
print('Random name:')
printRandomName()
print('\nName in pd 1 @ index 2:')
printNames(1, 2)
