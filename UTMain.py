print("cum")

import tkinter as tk
from tkinter import simpledialog
from tkinter import *
from PIL import ImageTk, Image
import klasser

root = tk.Tk()
root.title("Uddannelse's Tinder")
root.iconbitmap('./bogflamme(1).ico')
mainW = True
swipeW = False

window_W = 850
window_H = 700

screenWidth = root.winfo_screenwidth() #giver bredden af skærmen
screenHeight = root.winfo_screenheight() #giver højden af skærmen

# center point
center_x = 150 #hvorlangt fra venstre side af skærmen, vinduet skal poppe op
center_y = int(screenHeight/2 - window_H/2)


def main():
    root.geometry(f'{window_W}x{window_H}+{center_x}+{center_y}')
    root.resizable(False, False)

    # Create a photoimage object of the image in the path
    bImage = Image.open("./UTBackground.png")
    bImageobject = ImageTk.PhotoImage(bImage)

    #krisser
    krisserImage = Image.open("./Krisser.jpg")
    krisserImageR = krisserImage.resize((180, 180), Image.ANTIALIAS)
    krisserImageobject = ImageTk.PhotoImage(krisserImageR)

    #jeppe
    jeppeImage = Image.open("./Jeppe.jpg")
    jeppeImageR = jeppeImage.resize((180, 180), Image.ANTIALIAS)
    jeppeImageobject = ImageTk.PhotoImage(jeppeImageR)

    #label
    label1 = tk.Label(image=bImageobject)
    label1.image = bImageobject
    L1 = tk.Label(root, text='niggas in paris', font=("Helvetica", 16)).place(x=520, y=150)


    #krisser label
    label2 = tk.Label(image=krisserImageobject)
    label2.image = krisserImageobject
    #jeppe label
    label3 = tk.Label(image=jeppeImageobject)
    label3.image = jeppeImageobject

    # Position image
    label1.place(x=0, y=0)
    label2.place(x=30, y=480)
    label3.place(x=300, y=480)

    #knapper
    knap1 = tk.Button(root, text="testknap", height=5, width=20,
                      command=button1).place(x=30, y=60)            #testknap som sender dig til nyt window

    root.mainloop()


def button1():
    swipeWindow()


def swipeWindow():
    root.destroy()
    swipe = tk.Tk()
    swipe.iconbitmap('./bogflamme(1).ico')
    swipe.title("New Window")
    swipe.geometry(f'{window_W}x{window_H}+{center_x}+{center_y}')
    swipe.resizable(False, False)
    Label(swipe, text="This is the swipe window").pack()


if mainW:
    main()
elif swipeW:
    swipeWindow()
