#!/usr/bin/env python3

#hw01 etch_a_sketch
#12/7/2022
#ECE434
#Ryan Su
#simple etch a sketch board
#1. enter any size to create a square board
#2. enter X and Y coordinates for initial pen location
#3. start sketching with the display
#4. action includes (1)up: move pen up a slot and draw
#                   (2)down: move pen down a slot and draw
#                   (3)left: move pen left a slot and draw
#                   (4)right: move pen right a slot and draw
#                   (5)erase: erase current slot, pen stays
#                   (6)dump: dump the current drawing and start new page, pen stays
#                   (7)quit: quit drawing
#5. current pen location is shown under the sketch board after each action
#

# functions
#function printing the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(str(element) for element in row))

#grid board initialization
def initialization(dimensions):
    grid = [[]]
    grid[0].append('   ')
    for k in range(0, dimensions):
        grid[0].append(k+1)
        grid.append([k+1])
        grid[k+1].append(':')
        for i in range(0,dimensions):
            grid[k+1].append(' ')
    return grid

#main
#prompt for board size
dimensions = int(input("enter a size for the sketch grid: "))
grid = initialization(dimensions)

#prompt for initial pen location
currX = int(input("enter a initial pen location(x): "))
currY = int(input("enter a initial pen location(y): "))
#prompt again if invalid initial location entered
while((currX > dimensions) or (currY > dimensions)):
    print("out of range, another try")
    currX = int(input("enter a initial pen location(x): "))
    currY = int(input("enter a initial pen location(y): "))

offsetY = 1
grid[currX][offsetY+currY] = 'x'
print_grid(grid)
print("Current Pen location: "+str(currX)+", "+str(currY))

#join while loop to keep prompting actions after first set
while(1 + 1 == 2):
    action = str(input("action? (up, down, left, right, erase, dump, quit): "))
    while(action!="up" and action!="down" and action!="left" and action!="right" and action!="erase" and action!="quit" and action!="dump"):
            action = str(input("wrong input, another try (up, down, left, right, erase, dump, quit): "))
    if(action == "up"):
        currX = currX-1
        currY = currY
        grid[currX][offsetY+currY] = 'x'
    elif(action == "down"):
        currX = currX+1
        currY = currY
        grid[currX][offsetY+currY] = 'x'
    elif(action == "left"):
        currX = currX
        currY = currY-1
        grid[currX][offsetY+currY] = 'x'
    elif(action == "right"):
        currX = currX
        currY = currY+1
        grid[currX][offsetY+currY] = 'x'
    elif(action == "erase"):
        currX = currX
        currY = currY
        grid[currX][offsetY+currY] = ' '
    elif(action == "dump"):
        grid = initialization(dimensions)
    elif(action == "quit"):
        break

    print_grid(grid)
    print("Current Pen location: "+str(currX)+", "+str(currY))

    






