
#
# Solves a maze stored in a text file, and outputs the solution
# path to a second text file in the same format.
#
# Required command-line arguments: <input_file> <output_file
#


import operator
import time
import sys
from thread import *
from Tkinter import *
import Tkinter as tk
import threading
from threading import Thread

#from server import Server
#from robotics import Controller
#from finalgui import GUI

key = False
i4 = False
i5 = False

class Maze(object):
    """Represents a two-dimensional maze, where each cell can hold a
       single marker."""

    def __init__(self):
        self.data = []



    def read_file(self, path):
        """Read a maze text file and split out each character. Return
           a 2-dimensional list where the first dimension is rows and
           the second is columns."""
        maze = []
        with open(path) as f:
            for line in f.read().splitlines():
                maze.append(list(line))
        self.data = maze

    def write_file(self, path):
        """Write the specified 2-dimensional maze to the specified
           file, writing one line per row and with columns
           side-by-side."""
        with open(path, 'w') as f:
            for r, line in enumerate(self.data):
                f.write('%s\n' % ''.join(line))

    def find(self, symbol):
        """Find the first instance of the specified symbol in the
           maze, and return the row-index and column-index of the
           matching cell. Return None if no such cell is found."""
        for r, line in enumerate(self.data):
            try:
                return r, line.index('1')
            except ValueError:
                pass

    def get(self, where):
        """Return the symbol stored in the specified cell."""
        r, c = where
        return self.data[r][c]

    def set(self, where, symbol):
        """Store the specified symbol in the specified cell."""
        r, c = where
        self.data[r][c] = symbol



    def __str__(self):
        return '\n'.join(''.join(r) for r in self.data)

def printstuff(input):
    while True:
        try:
            sys.stdout.write("%s"%input)
            sys.stdout.flush()
        except IOError:
            continue
        break

def talk(input):
###########################
#    conn, id = s.startConn(sock)
#    start_new_thread(s.serverthread ,(conn,id,input))
###########################
    printstuff(input)
def action(symbol, input):
    if symbol == '1':
        talk("Nothing here, I see a path to the South.")
    elif symbol == "2":
        printstuff("Box of Gold")
        if (key):
            talk("We found the box again, and we have the Key!  We survived the maze, congratulations")
            time.sleep(.9)
            exit()
        else:
            talk(" I see a mysterious box, but we haven't found the key yet, I see a path to the East. maybe thats where the key is")
    elif symbol == "3":
        if(i4):
            talk("I see a path to the South, North, East, West, which way do you want to go?")
        else:
            global i4
            i4 = True
            talk("There is a bad guy up ahead but he doesn't have a helmet, i think i will headbutt him")
            #x.tilt_head_backward()
            #time.sleep(2)
            #x.stop_movement()
            #x.tilt_head_forward()
            time.sleep(8)
            talk("I gave him a headache. I see a path to the South, North, East, West, which way do you want to go?")
    elif symbol == "4":
        printstuff("more bad guys")
        if (i5):
            global key
            key = True
            talk("OH NO, more bad guys. Except these ones have helmets this time.")
            #need to do some action here
            time.sleep(8)
            talk("I beat them! and of course looted their pockets, I see a path to the West, maybe we can use our key that way.")
        else:
            talk("You've killed me...   Game over.")
            exit()
    elif symbol == "5":
        global i5
        i5 = True
        printstuff("Charging station")
        talk("It's a recharding station! I am all recharged, i see a path to the North.")

def first(N, S, E, W, MN, MS, ME, MW, position):
    #printstuff("\nW - North, S - South, A - West, D - East, X - End\n")
    #move = gui(N, S, E, W, mn, ms, me, mw, position)
    if(move == "W" or move == "w"):
        if(N):
            printstuff("%s\n Moving North\n\n"% position)
            maze.set(MN, maze.get(MN))
            if position == "N":
                printstuff("go forward")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go 90degrees to the left")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go 90degrees to the right")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go 180degrees to either way")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            action(maze.get(MN), MN)
            position = "N"
            solve(maze, MN, position)
        else:
            printstuff("Cannot go that way\n")
    elif(move == "S" or move == "s"):
        if(S):
            printstuff("%s \nMoving South\n\n"% position)
            maze.set(MS, maze.get(MS))
            if position == "N":
                printstuff("go 180 degrees")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go 90degrees to the left")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go 90degrees to the right")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go forward")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
            action(maze.get(MS), MS)
            position = "S"
            solve(maze, MS, position)
        else:
            printstuff("Cannot go that way\n")
    elif(move == "A" or move == "a"):
        if(W):
            printstuff("%s\nMoving West\n\n"%position)
            maze.set(MW, maze.get(MW))
            if position == "N":
                printstuff("go 90degrees right")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go forward")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go 180 degrees")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go 90 degrees left")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            action(maze.get(MW), MW)
            position = "W"
            solve(maze, MW, position)
        else:
            printstuff("Cannot go that way\n")
    elif(move == "D" or move == "d"):
        if(E):
            printstuff("%s\nMoving East\n\n"%position)
            maze.set(ME, maze.get(ME))
            if position == "N":
                printstuff("go 90degrees left")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go 180degrees")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go forward")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go 90 degrees right")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            action(maze.get(ME), ME)
            position = "E"
            solve(maze, ME, position)
        else:
            printstuff("Cannot go that way\n")
    elif(move == "X" or move == "x"):
        exit()

    #first(N, S, E, W, MN, MS, ME, MW, position)

def solve(maze, where, position):
    """Finds a path through the specified maze beginning at where (or
       a cell marked 'S' if where is not provided), and a cell marked
       'E'. At each cell the four directions are tried in the order
       RIGHT, DOWN, LEFT, UP. When a cell is left, a marker symbol
       (one of '>', 'v', '<', '^') is written indicating the new
       direction, and if backtracking is necessary, a symbol ('.') is
       also written. The return value is None if no solution was
       found, and a (row_index, column_index) tuple when a solution
       is found."""
    start_symbol = '1'
    end_symbol = 'E'
    wall_symbol = '#'
    east = (0,1)
    south = (1,0)
    west = (0,-1)
    north = (-1,0)
    N = False;
    S = False;
    E = False;
    W = False;
    mn = (0,0)
    ms = (0,0)
    me = (0,0)
    mw = (0,0)

    where = where or maze.find(start_symbol)
    if not where:
        printstuff("\n\n***No Start state***\n\n")
        return
    if maze.get(where) == end_symbol:
        # standing on the end cell
        printstuff("Found the End")
        exit()

    if(maze.get(map(operator.add , where, north)) != wall_symbol):
        N = True;
        mn = map(operator.add , where, north)

    if( maze.get(map(operator.add , where, south)) != wall_symbol):
        S = True;
        ms = map(operator.add , where, south)

    if(maze.get(map(operator.add , where, east)) != wall_symbol):
        E = True;
        me = map(operator.add , where, east)

    if(maze.get(map(operator.add, where, west)) != wall_symbol):
        W = True;
        mw = map(operator.add, where, west)

    maze.write_file(output_file)
    gui(N, S, E, W, mn, ms, me, mw, position)

def create_gui(self):
    gui = GUI()


def north(N, S, E, W, mn, ms, me, mw, position):
    move = "N"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    #app.destroy()
    #return north
def south(N, S, E, W, mn, ms, me, mw, position):
    move = "S"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    #app.destroy()
    #return south
def east(N, S, E, W, mn, ms, me, mw, position):
    move = "E"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    #app.destroy()
    #return east
def west(N, S, E, W, mn, ms, me, mw, position):
    move = "W"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    #app.destroy()
    #return west


def gui(N, S, E, W, mn, ms, me, mw, position):
    app = Tk()
    app.title("Maze Runner")
    app.geometry("275x165")

    label = Label(app, text="Which direction would you like to go?", height=0, width=100)
    #b = Button(app, text="Execute", width=10, command= execute)
    button_north = Button(app, text="North", width=10, command= lambda : north(N, S, E, W, mn, ms, me, mw, position))
    button_east = Button(app, text="East", width=10, command= lambda : east(N, S, E, W, mn, ms, me, mw, position))
    button_south = Button(app, text="South", width=10, command= lambda : south(N, S, E, W, mn, ms, me, mw, position))
    button_west = Button(app, text="West", width=10, command= lambda : west(N, S, E, W, mn, ms, me, mw, position))
    #button9 = Button(app, text="Clear Instructions", width=15, command=clear)

    label.pack()
    #b.pack(side="bottom",padx=0,pady=0)
    button_north.pack(padx=2,pady=2)
    button_east.pack(padx=2,pady=2)
    button_south.pack(padx=2,pady=2)
    button_west.pack(padx=2,pady=2)

    #button9.pack(padx=2,pady=2)
    #app.mainloop()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        printstuff('Arguments: <input file> <output file>\n')

        sys.exit()
    input_file, output_file = sys.argv[1:3]
    pos = "S"
    maze = Maze()
    #s = Server()
    #g = GUI()
#####################################
    #x = Controller()
    #x.setRange(0, 4300, 7100)
    #x.setRange(3, 4300, 7100)
    #x.setRange(4, 4300, 7100)
    #x.stop_movement()
#####################################

    maze.read_file(input_file)


###########################
    #sock = s.startServer()
    # conn, id = s.startConn(sock)
    # start_new_thread(s.serverthread ,(conn,id,"connecting"))
    # conn, id = s.startConn(sock)
    # start_new_thread(s.serverthread ,(conn,id,"You're on start,    i see a path to the South."))
    # time.sleep(3)
###########################
    where = None
    solve(maze,where,pos)
mainloop()
