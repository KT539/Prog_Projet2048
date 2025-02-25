# Project: Prog_Projet2048
# Title: main
# Author: Kilian Testard
# Version: 0.2 11.02.2025


import tkinter as tk
from tkinter import *
from src.Pack4_function import *
import random


# function to start a new game
def start_game():
    global score
    # reset the values of every tile to 0
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col] > 0:
                game[line][col] = 0
    # reset the score to 0
    if score > 0:
        score = 0
    display()
    # generate two random tiles
    gen_new_tile()
    gen_new_tile()


# function to pack a set of values downward and display the new values
def move_down():
    total_move = 0
    global score
    for col in range(4):
        [game[3][col], game[2][col], game[1][col], game[0][col], nb_move, score] = pack4(game[3][col], game[2][col], game[1][col], game[0][col], score)
        total_move += nb_move
    print(total_move)
    if total_move > 0:
        gen_new_tile()
    display()

# function to pack a set of values upward and display the new values
def move_up():
    total_move = 0
    global score
    for col in range(4):
        [game[0][col], game[1][col], game[2][col], game[3][col], nb_move, score] = pack4(game[0][col], game[1][col], game[2][col], game[3][col], score)
        total_move += nb_move
    print(total_move)
    if total_move > 0:
        gen_new_tile()
    display()

# function to pack a set of values leftward and display the new values
def move_left():
    total_move = 0
    global score
    for line in range(4):
        [game[line][0], game[line][1], game[line][2], game[line][3], nb_move, score] = pack4(game[line][0], game[line][1], game[line][2], game[line][3], score)
        total_move += nb_move
    print(total_move)
    if total_move > 0:
        gen_new_tile()
    display()

# function to pack a set of values rightward and display the new values
def move_right():
    total_move = 0
    global score
    for line in range(4):
        [game[line][3], game[line][2], game[line][1], game[line][0], nb_move, score] = pack4(game[line][3], game[line][2], game[line][1], game[line][0], score)
        total_move += nb_move
    print(total_move)
    if total_move > 0:
        gen_new_tile()
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


def gen_new_tile():
    # create a list with every empty tiles
    empty_tiles = []
    # create a list of new values with 80% of 2 and 20% of 4
    new_values = [2,2,2,2,2,2,2,2,4,4]
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col] == 0:
                empty_tiles.append([line, col])
    print(empty_tiles)
    # select a random tile from the empty_tiles list and give it a value from the new_values list
    if len(empty_tiles) > 0:
        new_tile = random.choice(empty_tiles)
        print(new_tile)
        game[new_tile[0]][new_tile[1]] = random.choice(new_values)
    display()


# set the base values at 0
game = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# set the base score at 0
score = 0


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
x0_btn = 470

# vertical beginning of the new game button
y0_btn = 115

# creating the window
win = tk.Tk()
win.geometry("800x600")


# title label
Label(text="8192", width=25, height=3, font=("Arial", 30)).place(x=x0_title, y=y0_title)

# score label
label_score = Label(text="Score : 0000", width= 10, height=1, font=("Arial", 15))
label_score.place(x=x0_score, y=y0_score)

# button to start a new game
btn_newGame = tk.Button(win, text="New game", width=10, height=1, font=("Arial", 15), command=start_game)
btn_newGame.place(x=x0_btn, y=y0_btn)


# display game values
def display():
    global score
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col]>0:
                labels[line][col].config(text=game[line][col], bg=colors[game[line][col]])
            else:
                labels[line][col].config(text="", bg=colors[game[line][col]])
    # update the displayed score
    label_score.config(text="Score = " + str(score))


# labels creation and positioning
for line in range(len(game)):
    for col in range(len(game[line])):
        # creation without placement
        labels[line][col] = Label (win, text =game[line][col], width=9, height=4, borderwidth=1, relief="solid", font=("Arial", 15), bg="#FFFFFF",)
        # label positioning in the windows
        labels[line][col].place(x=x0_labels + dx * col, y=y0_labels + dy * line)


start_game()
win.bind('<Key>', key_pressed)
display()
win.mainloop()