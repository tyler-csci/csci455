# coding: utf-8
import sys
from Tkinter import *
import time
import threading
from threading import Thread
#from robotics import Test
#from robotics import Controller

list = []

def __init__(self, parent, *args, **kwargs):
    Tk.Frame.__init__(self, parent, *args, **kwargs)
    self.parent = parent

def left_head():
    list.append("left_head")
    parameter_box()

def right_head():
    list.append("right_head")
    parameter_box()

def up_head():
    list.append("up_head")
    parameter_box()

def down_head():
    list.append("down_head")
    parameter_box()

def left_torso():
    list.append("left_torso")
    parameter_box()

def right_torso():
    list.append("right_torso")
    parameter_box()

def forward():
    list.append("forward")
    parameter_box()

def backward():
    list.append("backward")
    parameter_box()

def drive_left():
    list.append("drive_left")
    parameter_box()

def drive_right():
    list.append("drive_right")
    parameter_box()

def speak_hello():
    list.append("speak_hello")
    result(1)

def speak_forward():
    list.append("speak_forward")
    result(1)

def speak_backward():
    list.append("speak_backward")
    result(1)

def speak_smell():
    list.append("speak_smell")
    result(1)

def speak_tired():
    list.append("speak_tired")
    result(1)

def speak_heads():
    list.append("speak_heads")
    result(1)

def undo():
    del list[-1]

def clear():
    del list[:]

def sleep():
    list.append("sleep")
    parameter_box()

def execute():
    while len(list) > 0 :
        item, run_time = list[:2]
        del list[:2]
        close_time = time.time() + run_time
        if(item == "left_head"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.turn_left(3)
                        t.testing("left_head")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "right_head"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.turn_right(3)
                        t.testing("right_head")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "up_head"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.tilt_head_backward()
                        t.testing("up_head")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "down_head"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.tilt_head_forward()
                        t.testing("down_head")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "left_torso"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.turn_left(0)
                        t.testing("left_torso")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "right_torso"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.turn_right(0)
                        t.testing("right_torso")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "forward"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.move_forward(1)
                        t.testing("forward")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "backward"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.move_backward(1)
                        t.testing("backward")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "drive_left"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.move_left(2)
                        t.testing("drive_left")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "drive_right"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.move_right(2)
                        t.testing("drive_right")
                   #x.stop_movement()
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "speak_hello"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.speak("Hello")
                        t.testing("Hello")
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "speak_forward"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.speak("Moving Forward")
                        t.testing("Moving Forward")
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "speak_backward"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.speak("Beep Beep Beep")
                        t.testing("Beep Beep Beep")
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "speak_smell"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.speak("I smell something")
                        t.testing("I smell something")
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "speak_tired"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.speak("I'm tired")
                        t.testing("I'm tired")
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "speak_heads"):
            while True:
                try:
                    while time.time() < close_time:
                       #x.speak("Heads Up")
                        t.testing("Heads Up")
                    time.sleep(.9)
                except IOError:
                    continue
                break
        elif(item == "sleep"):
            while True:
                try:
                    while time.time() < close_time:
                        t.testing("sleep")
                except IOError:
                    continue
                break
        else:
            print("nothing")

def gifPlay():
    new_canvas = Toplevel(app)
    class Alien(object):
        def __init__(self, canvas, *args, **kwargs):
            self.canvas = canvas
            self.id = canvas.create_oval(*args, **kwargs)
            self.vx = 5
            self.vy = 0

        def move(self):
            x1, y1, x2, y2 = self.canvas.bbox(self.id)
            if x2 > 400:
                self.vx = -5
            if x1 < 0:
                self.vx = 5
            self.canvas.move(self.id, self.vx, self.vy)

    


def clickAbout():
    toplevel = Toplevel()
    Label(toplevel, text = "Turn Head:").grid(row = 0)
    button_head_left = Button(toplevel, text = "Left", width = 20, command=left_head)
    button_head_left.grid(row = 0, column = 1)
    button_head_right = Button(toplevel, text = "Right", width = 20, command=right_head)
    button_head_right.grid(row = 0, column = 2)

    Label(toplevel, text = "Tilt Head:").grid(row = 1)
    button_tilt_up = Button(toplevel, text = "Up", width = 20, command=up_head)
    button_tilt_up.grid(row = 1, column = 1)
    button_tilt_down = Button(toplevel, text = "Down", width = 20, command=down_head)
    button_tilt_down.grid(row = 1,column = 2)

    Label(toplevel, text = "Turn Torso:").grid(row = 2)
    button_torso_left = Button(toplevel, text = "Left", width = 20, command=left_torso)
    button_torso_left.grid(row = 2,column = 1)
    button_torso_right = Button(toplevel, text = "Right", width = 20, command=right_torso)
    button_torso_right.grid(row = 2, column = 2)

    Label(toplevel, text = "Drive:").grid(row = 3)
    button_move_forward = Button(toplevel, text = "Forward", width = 20, command=forward)
    button_move_forward.grid(row = 3, column = 1)
    button_move_backward = Button(toplevel, text = "Backward", width = 20, command=backward)
    button_move_backward.grid(row = 3, column = 2)

    button_move_left = Button(toplevel, text = "Left", width = 20, command=drive_left)
    button_move_left.grid(row = 4, column = 1)
    button_move_right = Button(toplevel, text = "Right", width = 20, command=drive_right)
    button_move_right.grid(row = 4, column = 2)

    Label(toplevel, text = "Speak:").grid(row = 5)
    button_speak_1 = Button(toplevel, text = "'Hello'", width = 20, command=speak_hello)
    button_speak_1.grid(row = 5, column = 1)
    button_speak_2 = Button(toplevel, text = "'Going Forward'", width = 20, command=speak_forward)
    button_speak_2.grid(row = 5, column = 2)
    button_speak_3 = Button(toplevel, text = "'Beep Beep Beep'", width = 20, command=speak_backward)
    button_speak_3.grid(row = 6, column = 1)
    button_speak_4 = Button(toplevel, text = "'What's that smell'", width = 20, command=speak_smell)
    button_speak_4.grid(row = 6, column = 2)
    button_speak_5 = Button(toplevel, text = "'I'm tired", width = 20, command=speak_tired)
    button_speak_5.grid(row = 7, column = 1)
    button_speak_6 = Button(toplevel, text = "'Head's Up'", width = 20, command=speak_heads)
    button_speak_6.grid(row = 7, column = 2)

    button_pause = Button(toplevel, text = "Sleep", width = 20, command=sleep)
    button_pause.grid(row =8, column = 1, columnspan = 2)
    button_undo = Button(toplevel, text = "Undo", width = 20, command = undo)
    button_undo.grid(row = 9, column = 1, columnspan = 2)
    button_finished = Button(toplevel, text = "Done", width = 20, command=toplevel.destroy)
    button_finished.grid(row = 10, column = 1, columnspan = 2)

    button_move_left.grid(padx = 2, pady = 2)
    button_move_right.grid(padx = 2, pady = 2)
    button_head_left.grid(padx = 2, pady = 2)
    button_head_right.grid(padx = 2, pady = 2)
    button_tilt_up.grid(padx = 2, pady = 2)
    button_tilt_down.grid(padx = 2, pady = 2)
    button_torso_left.grid(padx = 2, pady = 2)
    button_torso_right.grid(padx = 2, pady = 2)
    button_move_forward.grid(padx = 2, pady = 2)
    button_move_backward.grid(padx = 2, pady = 2)
    button_speak_1.grid(padx = 2, pady = 2)
    button_speak_2.grid(padx = 2, pady = 2)
    button_speak_3.grid(padx = 2, pady = 2)
    button_speak_4.grid(padx = 2, pady = 2)
    button_speak_5.grid(padx = 2, pady = 2)
    button_speak_6.grid(padx = 2, pady = 2)
    button_pause.grid(padx = 2, pady = 5)
    button_undo.grid(padx = 2, pady = 5)
    button_finished.grid(padx = 2, pady = 5)

def result(duration):
    list.append(duration)

def parameter_box():
    counter = IntVar()
    new_root = Toplevel(app)

    def param_dialog():
        increase_button = Button(new_root, text="▲", command=increase, width=3, height=1, fg="black", bg = "white")
        var_counter = Label(new_root, textvariable=counter)
        decrease_button = Button(new_root, text="▼", command=decrease, width=3, height=1, fg="black", bg = "white")
        button_finished = Button(new_root, text = "Done", width = 20, command=quit)

        increase_button.pack(padx=0.1,pady=0.1)
        var_counter.pack(padx=0.1, pady=0.1)
        decrease_button.pack(padx=0.1,pady=0.1)
        button_finished.pack(padx=0.1,pady=0.1)

    def increase(event=None):
        while True:
            try:
                counter.set(counter.get() + 1)
            except IOError:
                continue
            break

    def decrease(event=None):
        while True:
            try:
                counter.set(counter.get() - 1)
            except IOError:
                continue
            break

    def quit():
        new_root.destroy()
        result(counter.get())

    param_dialog()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func



app = Tk()
app.title("Robot Programming")
app.geometry("500x325")

label = Label(app, text="Select the action you would like to set:", height=0, width=100)
b = Button(app, text="Execute", width=10, command= execute)
button1 = Button(app, text="Action 1", width=10, command=clickAbout)
button2 = Button(app, text="Action 2", width=10, command=clickAbout)
button3 = Button(app, text="Action 3", width=10, command=clickAbout)
button4 = Button(app, text="Action 4", width=10, command=clickAbout)
button5 = Button(app, text="Action 5", width=10, command=clickAbout)
button6 = Button(app, text="Action 6", width=10, command=clickAbout)
button7 = Button(app, text="Action 7", width=10, command=clickAbout)
button8 = Button(app, text="Action 8", width=10, command=clickAbout)
button9 = Button(app, text="Clear Instructions", width=15, command=clear)

label.pack()
b.pack(side="bottom",padx=0,pady=0)
button1.pack(padx=2,pady=2)
button2.pack(padx=2,pady=2)
button3.pack(padx=2,pady=2)
button4.pack(padx=2,pady=2)
button5.pack(padx=2,pady=2)
button6.pack(padx=2,pady=2)
button7.pack(padx=2,pady=2)
button8.pack(padx=2,pady=2)
button9.pack(padx=2,pady=2)

if __name__=='__main__':
    Thread(target = execute()).start()
    #Thread(target = gifPlay()).start()

#t = Test()

#x = Controller()
#x.setRange(0, 4300, 7100)
#x.setRange(3, 4300, 7100)
#x.setRange(4, 4300, 7100)

#initial setup for centering everything
#x.stop_movement()




mainloop()
