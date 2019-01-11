from Tkinter import *
import Tkinter as tk


class GUI:

    def north(north):
        if(north == "N" or north == "n"):
            return north
        else:
            printstuff("Invalid key\n")

    def east(east):
        if(east == "E" or east == "e"):
            return east
        else:
            printstuff("Invalid key\n")

    def south(south):
        if(south == "S" or south == "s"):
            return south
        else:
            printstuff("Invalid key\n")

    def west(west):
        if(west == "W" or west == "w"):
            return west
        else:
            printstuff("Invalid key\n")


    app = Tk()
    app.title("Maze Runner")
    app.geometry("275x165")

    label = Label(app, text="Which direction would you like to go?", height=0, width=100)
    #b = Button(app, text="Execute", width=10, command= execute)
    button_north = Button(app, text="North", width=10, command=north)
    button_east = Button(app, text="East", width=10, command=east)
    button_south = Button(app, text="South", width=10, command=south)
    button_west = Button(app, text="West", width=10, command=west)
    #button9 = Button(app, text="Clear Instructions", width=15, command=clear)

    label.pack()
    #b.pack(side="bottom",padx=0,pady=0)
    button_north.pack(padx=2,pady=2)
    button_east.pack(padx=2,pady=2)
    button_south.pack(padx=2,pady=2)
    button_west.pack(padx=2,pady=2)

    #button9.pack(padx=2,pady=2)
    app.mainloop()
