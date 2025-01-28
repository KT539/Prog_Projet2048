# Project: Prog_Projet2048
# Title: 2_Display_game1
# Author: Kilian Testard
# Version: 1.0 21.01.2025


from tkinter import *


# empty list to create the labels at 0
game0=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# game_start list
'''game=[[0,0,2,0],[0,0,0,0],[0,2,0,0],[0,0,0,0]]'''

# game_model list
game=[[8192,4096,2048,1024],[512,256,128,0],[64,32,16,0],[8,4,2,0]]


# dictionary of colors
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


# horizontal distance between labels
dx=104

# vertical distance between labels
dy=97

# horizontal beginning of the labels
x0_labels = 195

# vertical beginning of the labels
y0_labels = 130

# horizontal beginning of the title
x0_title = 115

# vertical beginning of the title
y0_title = 0


# creating the window
win = Tk()
win.geometry("800x600")


# title
(Label(text="8192",width=25, height=3,  font=("Arial", 30)).place(x=x0_title, y=y0_title))


# display game values
def display():
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col]>0:
                labels[line][col].config(text=game[line][col], bg=colors[game[line][col]])
            else:
                labels[line][col].config(text="", bg=colors[game[line][col]])


# labels creation and positioning
for line in range(len(game0)):
    for col in range(len(game0[line])):
        # creation without placement
        labels[line][col] = Label (win, text =game0[line][col], width=9, height=4, borderwidth=1, relief="solid", font=("Arial", 15), bg="#FFFFFF",)
        # label positioning in the windows
        (labels[line][col].place(x=x0_labels + dx * col, y=y0_labels + dy * line))


display()
win.mainloop()