
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
from server import Server
#from robotics import Controller

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
            talk("OH NO, more bad guys. Except these ones have helmets this time. In that case we shall have, a dance off.")
            #x.move_right()
            #time.sleep(1)
            #x.stop_movement()
            #x.move_left()
            #time.sleep(1)
            #x.stop_movement()
            #x.turn_right()
            #time.sleep(1)
            #x.stop_movement()
            #x.turn_left()
            #time.sleep(1)
            #x.stop_movement()
            #x.tilt_head_forward()
            #time.sleep(2)
            #x.stop_movement()
            #time.sleep(8)
            talk("I beat them! and of course looted their pockets, I see a path to the West, maybe we can use our key that way.")
        else:
            talk("You've killed me...   Game over.")
            exit()
    elif symbol == "5":
        global i5
        i5 = True
        printstuff("Charging station")
        talk("It's a recharging station! I am all recharged, I see a path to the North.")

def first(N, S, E, W, MN, MS, ME, MW, position, move):
    if(move == "N"):
        if(N):
            printstuff("%s\n Moving North\n\n"% position)
            maze.set(MN, maze.get(MN))
            if position == "N":
                printstuff("go forward\n")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go 90degrees to the left\n")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go 90degrees to the right\n")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go 180degrees to either way\n")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            action(maze.get(MN), MN)
            position = "N"
            solve(maze, MN, position)
        else:
            printstuff("Cannot go that way\n")
    elif(move == "S"):
        if(S):
            printstuff("%s \nMoving South\n\n"% position)
            maze.set(MS, maze.get(MS))
            if position == "N":
                printstuff("go 180 degrees\n")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go 90degrees to the left\n")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go 90degrees to the right\n")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go forward\n")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
            action(maze.get(MS), MS)
            position = "S"
            solve(maze, MS, position)
        else:
            printstuff("Cannot go that way\n")
    elif(move == "W"):
        if(W):
            printstuff("%s\nMoving West\n\n"%position)
            maze.set(MW, maze.get(MW))
            if position == "N":
                printstuff("go 90degrees right\n")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go forward\n")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go 180 degrees\n")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go 90 degrees left\n")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            action(maze.get(MW), MW)
            position = "W"
            solve(maze, MW, position)
        else:
            printstuff("Cannot go that way\n")
    elif(move == "E"):
        if(E):
            printstuff("%s\nMoving East\n\n"%position)
            maze.set(ME, maze.get(ME))
            if position == "N":
                printstuff("go 90degrees left\n")
                #x.move_left(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "W":
                printstuff("go 180degrees\n")
                #x.move_right(2)
                #time.sleep()
                #x.stop_movement()
            elif position == "E":
                printstuff("go forward\n")
                #x.move_forward(1)
                #time.sleep()
                #x.stop_movement()
                #time.sleep()
                #x.stop_movement()
            elif position == "S":
                printstuff("go 90 degrees right\n")
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
    printstuff("\nW - North, S - South, A - West, D - East, X - End\n")
    gui(N, S, E, W, mn, ms, me, mw, position)


def move_north(app, N, S, E, W, mn, ms, me, mw, position):
    move = "N"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    app.destroy()
    #return north
def move_south(app, N, S, E, W, mn, ms, me, mw, position):
    move = "S"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    app.destroy()
    #return south
def move_east(app, N, S, E, W, mn, ms, me, mw, position):
    move = "E"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    app.destroy()
    #return east
def move_west(app, N, S, E, W, mn, ms, me, mw, position):
    move = "W"
    first(N, S, E, W, mn, ms, me, mw, position,move)
    app.destroy()
    #return west

def gui(N, S, E, W, mn, ms, me, mw, position):

    app = Tk()
    app.title("Maze Runner")
    app.geometry("700x300")

    Label(app, text= "Which direction would you like to go?").grid(row = 0)
    button_north = Button(app, text = "North", width = 10, command = lambda: move_north(app, N, S, E, W, mn, ms, me, mw, position))
    button_north.grid(row = 1, column = 2)
    button_east = Button(app, text = "East", width = 10, command = lambda: move_east(app, N, S, E, W, mn, ms, me, mw, position))
    button_east.grid(row = 2, column = 3)
    button_south = Button(app, text = "South", width = 10, command = lambda: move_south(app, N, S, E, W, mn, ms, me, mw, position))
    button_south.grid(row = 3, column = 2)
    button_west = Button(app, text = "West", width = 10, command = lambda: move_west(app, N, S, E, W, mn, ms, me, mw, position))
    button_west.grid(row = 2, column = 1)
    #button_exit = Button(app, text = "Exit", width = 10, command = app.destroy())

    button_north.grid(padx = 2, pady = 2)
    button_south.grid(padx = 2, pady = 2)
    button_east.grid(padx = 2, pady = 2)
    button_west.grid(padx = 2, pady = 2)
    #button_exit.grid(row=4, column = 2, columnspan=2)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        printstuff('Arguments: <input file> <output file>\n')

        sys.exit()
    input_file, output_file = sys.argv[1:3]
    pos = "S"
    maze = Maze()
    s = Server()
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
