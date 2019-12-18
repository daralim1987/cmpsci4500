# Dara Lim
# 09/04/2019
# cmpsci4500-002
##this program will take an file with integers arranged to represent
##circles and arrows pointing to the circls, This would create a map
##and the program randomly tranverses these arrows until each one has
# been seen. the program prints and creates a file with the number of circle used in the game,
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

#In HW1, you simulated one game of circles and arrows after reading in the file. For HW2, if the input file correctly defines a connected system of circles and arrows, you will do something different. Although you will read in the input file information once (like before), for HW2 you’ll run that simulated game ten (10) times. Before each simulated game, reinitialize to the start of a game. Keep statistics on the 10 game simulations, and then print out to the screen and to the output file the following information:
#The average number of total checks per game
#The maximum number of total checks in a single game
#The minimum number of total checks in a single game
#The average number of checks on a single circle over all the games
#The minimum number of single circle checks
#The maximum number of single circle checks
#In HW1, the maximum number of circles was 10. Increase that to 20.
#
#It wasn’t mentioned in the HW1 specification, but it is at least theoretically possible for the game to go on for a very long time because arrows are selected randomly. In order to avoid waiting too long for a game to continue, impose a limit of a million checks on any one game. (Think about this: is that a reasonable number?) If that limit is reached, stop the program with a sensible output that helps the user know what happened.
#The geeks for geeks website is helpful for checking if the input file is strongly connected graph.
# Python program to check if a given directed graph is strongly
# connected or not

import random
import os.path
from collections import defaultdict
import sys


# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by isSC() to perform DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):

        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # The main function that returns true if graph is strongly connected
    def isSC(self):

        # Step 1: Mark all the vertices as not visited (For first DFS)
        visited = [False] * (self.V)

        # Step 2: Do DFS traversal starting from first vertex.
        self.DFSUtil(0, visited)

        # If DFS traversal doesnt visit all vertices, then return false
        if any(i == False for i in visited):
            return False

        # Step 3: Create a reversed graph
        gr = self.getTranspose()

        # Step 4: Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Step 5: Do DFS for reversed graph starting from first vertex.
        # Staring Vertex must be same starting point of first DFS
        gr.DFSUtil(0, visited)

        # If all vertices are not visited in second DFS, then
        # return false
        if any(i == False for i in visited):
            return False
        return True


# Declare list variables
numMax = []
numMin = []
sumAverage = 0.00
sumTotalCount = 0
maxTotalCheck = []
minTotalCheck = []
arrowList = []
# Prompt the user to type in input file to use for the game
file = input("Please enter file name to play the game: ")
fo = open("HW2limOutfile.txt", "w")
if os.path.exists(file):
    #    with open(file) as f:
    f = open(file, "r")
    N = int(f.readline())
    # Check if the number of circle is not follow the specification
    if N < 2 or N > 20:
        fo.write("The file not follow the format")
        sys.exit("The file not follow the format")
    k = int(f.readline())
    # Check if the number of arrow is less than number of circle
    if k < N:
        fo.write("The file not follow the format")
        sys.exit("The file not follow the format")
    str0 = f.readlines()
    # check if the number of arrow is not follow the specification
    if len(str0) != k:
        fo.write("The file not follow the format")
        sys.exit("The file not follow the format")
    # Read the third line from file and append the arrow to the arrow list
    g = Graph(N)
    f.seek(0, 0)
    for _ in range(2):
        next(f)
    for i in range(k):
        str = f.readline()
        str = list(map(int, str.split()))
        arrowList.append((str[0] - 1, str[1] - 1))
        g.addEdge(str[0] - 1, str[1] - 1)
    #            arrowList.append( (int(str[0]) - 1, int(str[2]) - 1) )
    # Simulation of game start from here
    if g.isSC():
        for i in range(10):
            visitCounts = []
            visualsList = []
            thisArrow = []
            currentCircle = 0
            circlesSeen = 1
            for j in range(N):
                visitCounts.append(0)
            visitCounts[0] = 1
            while circlesSeen < N:
                thisArrow = random.choice(arrowList)
                if thisArrow[0] == currentCircle:
                    currentCircle = thisArrow[1]
                    if visitCounts[currentCircle] == 0:
                        circlesSeen += 1
                    visitCounts[currentCircle] += 1
                    visualsList.append(thisArrow)
                #set the total checks limit condition
                if sum(visitCounts) == 1000000:
                    sys.exit("The total checks have reached the limit")
                    fo.write("The total checks have reached the limit")
            sumAverage += sum(visitCounts)
            sumTotalCount += sum(visitCounts)
            maxTotalCheck.append(sum(visitCounts))
            minTotalCheck.append(sum(visitCounts))
            numMin.append(min(visitCounts))
            numMax.append(max(visitCounts))
        # Output to the screen and file
        print("The average number of total checks per game is: ", sumAverage / 10)
        print("The maximum number of total checks in a single game is: ", max(maxTotalCheck))
        print("The minimum number of total checks in a single game is: ", min(minTotalCheck))
        print("The average number of checks on a single circle over all the games is: ", sumTotalCount / (10 * N))
        print("The minimum number of single circle checks is: ", min(numMin))
        print("The maximum number of single circle checks is: ", max(numMax))

        fo.write("The average number of total checks per game is: {}\n".format(sumAverage / 10))
        fo.write("The maximum number of total checks in a single game is: {}\n".format(max(maxTotalCheck)))
        fo.write("The minimum number of total checks in a single game is: {}\n".format(min(minTotalCheck)))
        fo.write("The average number of checks on a single circle over all the game is: {}\n".format(
            sumTotalCount / (10 * N)))
        fo.write("The minimum number of single circle checks is: {}\n".format(min(numMin)))
        fo.write("The maximum number of single circle checks is: {}\n".format(max(numMax)))
    else:
        print("The input file is not a strongly connected graph")
        fo.write("The input file is not a strongly connected graph")
else:
    sys.exit("The file not exists")
    fo.write("The file not exists")
# close the files
f.close()
fo.close()
