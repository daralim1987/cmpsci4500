#Dara Lim
#10/01/19
#cmpsci4500-002
#
#Project specification is as follow:
#Consider the following (wildly improbable) situation:
#    1    You have an N X N grid lying on the floor, where N is an integer between 2 and 15 inclusive.
#    2    You are capable of dropping blobs of paint on to the grid in such a way that
#    1    The blob lands randomly on the grid on to only one cell (each time)
#    2    The blob does not splatter into any of the other cells
#    3    The blob always falls somewhere on the grid
#    4    If subsequent blobs of paint fall on that same cell, that’s OK, and again there is no splatter
#    3    In order to “complete” your painting (and our apologies to Jackson Pollock), you continue dropping paint blobs, one at a time, until each cell has at least one paint blob dropped on to it.
#   When the painting is complete, every cell contains paint, and some cells may have LOTS of paint.

#    1    On the screen, ask the interactive user to enter an integer between 2 and 15 inclusive. This will determine the size of your square grid. I will call this number N. If the user enters something illegal, give an error message and keep asking until you get something appropriate.
#    2    Next, ask the interactive user to enter an integer between 1 and 10 inclusive. This will tell your program how many “paintings” it will make. I will call this number K. If the user enters something illegal, give an error message and keep asking until you get something appropriate.
#    3    Make an N X N random paint blob painting K times. As each of the K paintings is being made, display graphics on the screen to show the interactive user how the painting is proceeding. You have great latitude as to how you will display the painting as it fills up with paint. At the very least, the interactive user should be able to tell which cells have NO paint so far, which cells have SOME paint so far, and which cell is being painted right at the moment. This minimum would require three distinct colors. However, you might be able to think of a clever way to visually communicate more information about the painting than no paint, some paint, and currently being painted. Be thoughtful and creative about this, please. Give some thought as to how quickly you want to paint drops to appear in your simulation.
#    4    After a painting “finishes,” alert the interactive user, and inform them that they must push ENTER (or RETURN) to continue.
#    5    After all K paintings have been finished (including the final ENTER push by the user), display the following statistics from all the paintings: The minimum, maximum, and average number of paint blobs it took to paint a picture; and the minimum, maximum, and average number that describes the most paint blobs that fell into any one cell in a painting.

#The initial grid n*n of each game is colored each cell with white color fill.
#The painting colore is randomly select from the the list colore which contain about ten different colores.
#If the cell get painted more than 2 times, the latest paint color is override the previous one.


import random
import turtle
import sys

#take the size of grid from the interactive user
n = int(input("Enter an integer between 2 and 15 inclusive\n"))
while n < 2 or n > 15:
    n = int(input("Please enter size of grid between 2 and 15 inclusively\n"))

#take the number of painting from the interactive user
k = int(input("Enter an integer between 1 and 10 inclusive\n"))
while k < 1 or k > 10:
    k = int(input("Please enter number of painting between 1 and 10 inclusive\n"))

#function draw box
def draw_box(t,x,y,size,fill_color):
    t.penup() # no drawing!
    t.goto(x,y) # move the pen to a different position
    t.pendown() # resume drawing
    t.fillcolor(fill_color)
    t.begin_fill()  # Shape drawn after this will be filled with this color!
 
    for i in range(0,4):
        board.forward(size) # move forward
        board.right(90) # turn pen right 90 degrees
 
    t.end_fill() # Go ahead and fill the rectangle!
    
#list of colors
color_list = ["white","blue", "red", "green","yellow", "brown", "purple", "pink", "orange"]
#create a grid
row = []
for i in range(n):
    row.append(0)
grid = []
for i in range(n):
    grid.append(list(row))

#function draw a grid
def draw_grid():
    square_color = color_list[0]
    start_x = 0 # starting x position of the chess board
    start_y = 0 # starting y position of the chess board
    box_size = 20 # pixel size of each square in the chess board
    for i in range(0,n):
        for j in range(0,n):
            draw_box(board,start_x+j*box_size,start_y+i*box_size,box_size,square_color)
            
#declare lists
countPaintList = []
minPaintList = []
maxPaintList = []
minMaxList = []

#Start simulation of the game
for i in range(k):
    board = turtle.Turtle()
    countPaint = 0
    occupiedCells = 0
#    draw_grid()
    while(occupiedCells < (n*n)):
        r = random.randint(0, (n-1))
        c = random.randint(0, (n-1))
#        draw_box(board, 0+c*20, 0+r*20, 20, random.choice(color_list[1:]))
        countPaint += 1
        minMaxList.append(countPaint)
        if grid[r][c] == 0:
            grid[r][c] = 1
            occupiedCells += 1
    
    countPaintList.append(countPaint)
    minPaintList.append(min(minMaxList))
    maxPaintList.append(max(minMaxList))
    del grid
    row = []
    grid = []
    for i in range(n):
        row.append(0)
    for i in range(n):
        grid.append(list(row))
    board.reset()
    t = input("Press enter to continue\n")

print("The minimum number of paint blobs it took to paint a picture is: ", min(countPaintList))
print("The maximum number of paint blobs it took to paint a picture is: ", max(countPaintList))
print("The average number of paint blobs it took to paint a picture is: ", sum(countPaintList)/k)
print("\n")
print("The minimum number the most paint blobs fell into any one cell in a painting is: ", min(minPaintList))
print("The maximum number the most paint blobs fell into any one cell in a painting is: ", max(maxPaintList))
print("The average number the most paint blobs fell into any one cell in a painting is: ", (sum(minPaintList)+sum(maxPaintList))/(n*n))

sys.exit(0)
turtle.done()




