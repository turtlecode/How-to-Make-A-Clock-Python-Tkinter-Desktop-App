from tkinter import *
import time


root = Tk()
root.geometry("600x400")

def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")

    my_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
    my_label.after(1000, clock)

    my_label2.config(text = day)

def update():
    my_label.config(text="New Text")

my_label = Label(root, text="", font=("Helvetica", 48), fg="green", bg="black")
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=("Helvetica", 14))
my_label2.pack(pady=10)

clock()

root.mainloop()