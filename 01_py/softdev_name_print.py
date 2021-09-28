#Tina Nguyen
#Trio: Tami Takada, Tina Nguyen, Naomi Naranjo
#SoftDev
#K01 -- Printing SoftDev Student Names
#2021-09-22

def printNames(period, index):
    pd1 = []
    pd2 = []

    with open('softdev_students_pd1.txt') as reader:
        name = reader.readline()
        while name != '':
            pd1.append(name.rstrip('\n'))
            name = reader.readline()

    with open('softdev_students_pd2.txt') as reader:
        name = reader.readline()
        while name != '':
            pd2.append(name.rstrip('\n'))
            name = reader.readline()
    pd1.sort()
    pd2.sort()


    if period == 1:
        if index < len(pd1):
            print(pd1[index])
        else:
            print('Student does not exist')
    elif period == 2:
        if index < len(pd2):
            print(pd2[index])
        else:
            print('Student does not exist')
    else:
        print('Period does not exist')
