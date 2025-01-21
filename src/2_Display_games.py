# Project: Prog_Projet2048
# Title: 2_Display_game1
# Author: Kilian Testard
# Version: 1.0 21.01.2025

from tkinter import *
import tkinter.font

# game0 list
game0=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

# game1 list
"""game1=[[0,0,2,0],
       [0,0,0,0],
       [0,2,0,0],
       [0,0,0,0]]"""

game1=[[2048,64,32,16],
       [1024,16,8,8],
       [32,512,4,0],
       [4,0,2,0]]

colors={0:"#CCCCCC",
        2:"#9FC5F8",
        4:"#597EAA",
        8:"#085394",
        16:"#B4A7D6",
        32:"#8E7CC3",
        64:"#674EA7",
        128:"#D5A6BD",
        256:"#C27BA0",
        512:"#A64D79",
        1024:"#E06666",
        2048:"#CC0000",
        4096:"#990000",
        8192:"#F1C232"}

# empty labels list
labels=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

dx=0 # horizontal distance between labels
dy=0 # vertical distance between labels

# display game1 values
def display():
    for line in range(len(game1)):
        for col in range(len(game1[line])):
            labels[line][col].config(text=game1[line][col], bg=colors[game1[line][col]])



# creating the window
win = Tk()
win.geometry("1000x750")

# Title
Label(text="8192",width=25, height=3,  font=("Arial", 15)).grid(row=0,column=0, columnspan=2,padx=0,pady=0)

#labels creation and position
for line in range(len(game0)):
    for col in range(len(game0[line])):
        # creation without placement
        labels[line][col] = Label (win, text =game0[line][col], width=15, height=5, borderwidth=1, relief="solid", font=("Arial", 15), bg="#FFFFFF")
        # label positionning in the windows
        labels[line][col].grid (row=line+1,column=col,padx=dx,pady=dy)

display()
win.mainloop()