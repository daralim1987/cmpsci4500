#Dara Lim
#09/04/2019
#cmpsci4500-002

##this program will take an file with integers arranged to represent
##circles and arrows pointing to the circls, This would create a map
##and the program randomly tranverses these arrows until each one has
#been seen. the program prints and creates a file with the number of circle used in the game,
##the number of arrow used in the game, the sum of all
##visits, the avg number of visits and max visits
##The main data stucture is a list of or record Arrow.
##Record Arrow is two interger values that represent the exit and
##entry points of two circles.
##The ciricles are represnted by a list of integters. This list is
##incremented at the circles index when it is visited. The current circle
##is accounted for with a single integer cooresponding to the index in the
##list.
##To randomized the arrow selection out of a circle, a random arrow is
##chosen from the array of ALL arrows and compared to the current circle
##variable. If the arrow source == current circle, curent circle is set
##to the arrow destination and circle array is incremented. if the source
##of arrow does not match, another one is chosen until there is a match.

import random
import os.path
import sys

#Declare list variables
arrowList = []
visitCounts = []
visualsList = []

#Prompt the user to type in input file to use for the game
file = input("Please enter file name to play the game: ")
fo = open("HW1limOutfile.txt", "w")
if os.path.exists(file):
    with open(file) as f:
        N = int(f.readline())
        #Check if the number of circle is not follow the specification
        if N < 2 or N > 10:
            fo.write("The file not follow the format")
            sys.exit("The file not follow the format")
        k =  int(f.readline())
        #Check if the number of arrow is less than number of circle
        if k < N:
            fo.write("The file not follow the format")
            sys.exit("The file not follow the format")
        str0 = f.readlines()
        #check if the number of arrow is not follow the specification
        if len(str0) != k:
            fo.write("The file not follow the format")
            sys.exit("The file not follow the format")
        #Read the third line from file and append the arrow to the arrow list
        f.seek(0, 0)
        for _ in range(2):
            next(f)
        for i in range(k):
            str = f.readline()
            str = list(map(int, str.split()))
            arrowList.append( (str[0] - 1, str[1] - 1) )
#            arrowList.append( (int(str[0]) - 1, int(str[2]) - 1) )
    currentCircle = 0
    circlesSeen = 1
    for i in range(N):
        visitCounts.append(0)
    visitCounts[0] = 1
    #Play the game while all the circle have not been visited
    while circlesSeen < N:
        thisArrow = random.choice(arrowList)
        if thisArrow[0] == currentCircle:
            currentCircle = thisArrow[1]
            if visitCounts[currentCircle] == 0:
                circlesSeen += 1
            visitCounts[currentCircle] += 1
            
            visualsList.append(thisArrow)

    #Output to the screen and file
    print("The number of circle that were used for the game is: ",N)
    print("The number of arrow that were used for the game is: ",k)
    print("The total number of checks on all the circles combined is: ", sum(visitCounts))
    print("The average number of checks in a circle marked during the game is: ", sum(visitCounts)/N)
    print("The maximum number of checks in any one circle is: ", max(visitCounts))

    fo.write("The number of circle that were used for the game is: {}\n".format(N))
    fo.write("The number of arrow that were used for the game is: {}\n".format(k))
    fo.write("The total number of checks on all the circles combined is: {}\n".format(sum(visitCounts)))
    fo.write("The average number of checks in a circle marked during the game is: {}\n".format(sum(visitCounts)/N))
    fo.write("The maximum number of checks in any one circle is: {}\n".format(max(visitCounts)))

else:
    sys.exit("The file not exists")
    fo.write("The file not exists")
#close the files
f.close()
fo.close()



















