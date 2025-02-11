# Project: Prog_Projet2048
# Title: main
# Author: Kilian Testard
# Version: 1.0 11.02.2025

import tkinter as tk
from tkinter import *
from src.Pack4_function import *


# function to pack a set of values downward and display the new values
def move_down():
    total_move = 0
    for col in range(4):
        [game[3][col], game[2][col], game[1][col], game[0][col], nb_move] = pack4(game[3][col], game[2][col], game[1][col], game[0][col])
        total_move += nb_move
    display()

# function to pack a set of values upward and display the new values
def move_up():
    total_move = 0
    for col in range(4):
        [game[0][col], game[1][col], game[2][col], game[3][col], nb_move] = pack4(game[0][col], game[0][col], game[2][col], game[3][col])
        total_move += nb_move
    display()

# function to pack a set of values leftward and display the new values
def move_left():
    total_move = 0
    for line in range(4):
        [game[line][0], game[line][1], game[line][2], game[line][3], nb_move] = pack4(game[line][0], game[line][1], game[line][2], game[line][3])
        total_move += nb_move
    display()

# function to pack a set of values rightward and display the new values
def move_right():
    total_move = 0
    for line in range(4):
        [game[line][3], game[line][2], game[line][1], game[line][0], nb_move] = pack4(game[line][3], game[line][2], game[line][1], game[line][0])
        total_move += nb_move
    display()


# function to handle key press events and trigger corresponding movements
def key_pressed(event) :
    # get the key symbol
    touche=event.keysym
    if (touche=="Right" or touche=="d" or touche=="D"):
        move_right()
    if (touche=="Left" or touche=="a" or touche=="A"):
        move_left()
    if (touche=="Up" or touche=="w" or touche=="W"):
        move_up()
    if (touche=="Down" or touche=="s" or touche=="S"):
        move_down()


# empty list to create the labels at 0
game0 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# game_start list
'''game = [[0,0,2,0],[0,0,0,0],[0,2,0,0],[0,0,0,0]]'''

# game_model list
game = [[0,0,0,2],[4,4,2,2],[2,4,8,16],[2,0,8,16]]
#[[8192,4096,2048,1024],[512,256,128,0],[64,32,16,0],[8,4,2,0]]


# dictionary of colors
colors = {0:"#CCCCCC",
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
dx = 104

# vertical distance between labels
dy = 97

# horizontal beginning of the labels
x0_labels = 195

# vertical beginning of the labels
y0_labels = 175

# horizontal beginning of the title
x0_title = 115

# vertical beginning of the title
y0_title = 0

# horizontal beginning of the score display
x0_score = 215

# vertical beginning of the score display
y0_score = 125

# horizontal beginning of the new game button
x0_btn = 475

# vertical beginning of the new game button
y0_btn = 115

# creating the window
win = tk.Tk()
win.geometry("800x600")


# title
Label(text="8192", width=25, height=3, font=("Arial", 30)).place(x=x0_title, y=y0_title)

# best score display
Label(text="Score : 0000", width= 10, height=1, font=("Arial", 15)).place(x=x0_score, y=y0_score)

# start a new game button
btn_newGame = tk.Button(win, text="New game", width=10, height=1, font=("Arial", 15)) # add argument command=def_start_new_game
btn_newGame.place(x=x0_btn, y=y0_btn)

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
        labels[line][col].place(x=x0_labels + dx * col, y=y0_labels + dy * line)


win.bind('<Key>', key_pressed)
display()
win.mainloop()