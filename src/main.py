# Project: Prog_Projet2048
# Title: main
# Author: Kilian Testard
# Version: 0.4 11.03.2025

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from src.Pack4_function import *
import random
import copy


# function to start a new game
def start_game():
    global score, game, time_count
    # labels creation and positioning
    for line in range(len(game)):
        for col in range(len(game[line])):
            # creation without placement
            labels[line][col] = Label(win, text=game[line][col], width=9, height=4, borderwidth=1, relief="solid", font=("Arial", 15), bg="#FFFFFF", )
            # label positioning in the windows
            labels[line][col].place(x=x0_labels + dx * col, y=y0_labels + dy * line)
    # reset the values of every tile to 0
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col] > 0:
                game[line][col] = 0
    # reset the score to 0
    score = 0
    # reset the timer
    time_count = 0
    # generate two random tiles
    gen_new_tile()
    gen_new_tile()


# function to switch to 6x6 mode
def init_6x6():
    global game, labels, grid_size
    win.geometry("1000x850")
    grid_size = 6
    clear_labels()
    labels = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    game = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    label_title.place(x=x0_title + 105, y=y0_title)
    label_timer.place(x=x0_timer + 105, y=y0_timer + 200)
    btn_newGame.place(x=x0_btn_ng + 209, y=y0_btn_ng)
    btn_undo.place(x=x0_btn_ud + 209, y=y0_btn_ud)
    btn_4x4.place(x=x0_btn_4x4 + 105, y=y0_btn_4x4 + 50)
    btn_6x6.place(x=x0_btn_6x6 + 105, y=y0_btn_6x6 + 50)
    start_game()


# function to switch to 4x4 mode
def init_4x4():
    global game, labels, grid_size
    win.geometry("800x650")
    grid_size = 4
    clear_labels()
    labels = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    game = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    label_title.place(x=x0_title, y=y0_title)
    label_timer.place(x=x0_timer, y=y0_timer)
    btn_newGame.place(x=x0_btn_ng, y=y0_btn_ng)
    btn_undo.place(x=x0_btn_ud, y=y0_btn_ud)
    btn_4x4.place(x=x0_btn_4x4, y=y0_btn_4x4)
    btn_6x6.place(x=x0_btn_6x6, y=y0_btn_6x6)
    start_game()


# function to clear the labels before a switch
def clear_labels():
    for col in labels:
        for label in col:
            if label :
                label.destroy()


# function to update the timer every second
def update_timer():
    global time_count
    time_count += 1
    hours = str(time_count // 3600).zfill(2)
    minutes = str((time_count % 3600) // 60).zfill(2)
    seconds = str(time_count % 60).zfill(2)
    label_timer.config(text=f"Timer : {hours}:{minutes}:{seconds}")
    # update the timer after every second
    win.after(1000, update_timer)


# function to check if the game is won
def win_check():
    global win_status
    for line in range(grid_size):
        for col in range(grid_size):
            # flag trigger the first time a tile reaches 2048
            if game[line][col] == 2048 and win_status == False:
                win_status = True
                win_player_input()


# messagebox if the game is won
def win_player_input():
    input = messagebox.askquestion(title=None, message="You won ! Do you want to keep playing ?")
    if input == "yes":
        pass
    if input == "no":
        start_game()


# function to check if the game is lost
def loss_check():
    # create a list with every empty tiles
    empty_tiles = []
    for line in range(grid_size):
        for col in range(grid_size):
            if game[line][col] == 0:
                empty_tiles.append([line, col])
    # if the board is full, check for adjacent identical tiles
    if len(empty_tiles) == 0:
        line_fusion=False
        col_fusion=False
        for line in range(grid_size-1):
            for col in range(grid_size):
                if game[line][col] == game[line+1][col] :
                    line_fusion=True
        for line in range(grid_size):
            for col in range(grid_size-1):
                if game[line][col] == game[line][col + 1]:
                     col_fusion=True
        # if there are no adjacent identical tiles, triggers loss_player_input
        if line_fusion==False and col_fusion==False:
            display()
            loss_player_input()


# messagebox if the game is lost
def loss_player_input():
    input = messagebox.askquestion(title=None, message="You lost ! Do you want to start a new game ?")
    if input == "yes":
        start_game()
    if input == "no":
        quit()


# function to pack a set of values downward and return the total amount of moves that occurred
def move_down():
    total_move = 0
    global score
    for col in range(grid_size):
        [game[5][col], game[4][col], game[3][col], game[2][col], game[1][col], game[0][col], nb_move, score] = pack4(game[5][col], game[4][col], game[3][col], game[2][col], game[1][col], game[0][col], score)
        total_move += nb_move
    return total_move


# function to pack a set of values upward and return the total amount of moves that occurred
def move_up():
    total_move = 0
    global score
    for col in range(grid_size):
        [game[0][col], game[1][col], game[2][col], game[3][col], game[4][col], game[5][col], nb_move, score] = pack4(game[0][col], game[1][col], game[2][col], game[3][col], game[4][col], game[5][col], score)
        total_move += nb_move
    return total_move


# function to pack a set of values leftward and return the total amount of moves that occurred
def move_left():
    total_move = 0
    global score
    for line in range(grid_size):
        [game[line][0], game[line][1], game[line][2], game[line][3], game[line][4], game[line][5], nb_move, score] = pack4(game[line][0], game[line][1], game[line][2], game[line][3], game[line][4], game[line][5], score)
        total_move += nb_move
    return total_move


# function to pack a set of values rightward and return the total amount of moves that occurred
def move_right():
    total_move = 0
    global score
    for line in range(grid_size):
        [game[line][5], game[line][4], game[line][3], game[line][2], game[line][1], game[line][0], nb_move, score] = pack4(game[line][5], game[line][4], game[line][3], game[line][2], game[line][1], game[line][0], score)
        total_move += nb_move
    return total_move


# function to handle key press events and trigger corresponding movements
def key_pressed(event) :
    global game_state
    total_move = 0
    # get the key symbol
    touche=event.keysym
    if (touche=="Right" or touche=="d" or touche=="D"):
        memorize_game_state()
        total_move = move_right()
    if (touche=="Left" or touche=="a" or touche=="A"):
        memorize_game_state()
        total_move = move_left()
    if (touche=="Up" or touche=="w" or touche=="W"):
        memorize_game_state()
        total_move = move_up()
    if (touche=="Down" or touche=="s" or touche=="S"):
        memorize_game_state()
        total_move = move_down()
    if (touche=="q" or touche=="Q"):
        quit()
    # if the tiles moved, generate a new random one
    if total_move > 0:
        gen_new_tile()
    win_check()


def gen_new_tile():
    # create a list with every empty tiles
    empty_tiles = []
    # create a list of new values with 80% of 2 and 20% of 4
    new_values = [2,2,2,2,2,2,2,2,4,4]
    for line in range(grid_size):
        for col in range(grid_size):
            if game[line][col] == 0:
                empty_tiles.append([line, col])
    print(empty_tiles)
    # select a random tile from the empty_tiles list and give it a value from the new_values list
    if len(empty_tiles) > 0:
        new_tile = random.choice(empty_tiles)
        print(new_tile)
        game[new_tile[0]][new_tile[1]] = random.choice(new_values)
    display()
    loss_check()


# function to memorize the state of the game
def memorize_game_state():
    global game_state
    game_state.clear()
    game_state.append(copy.deepcopy(game))
    game_state.append(score)
    game_state.append(win_status)


# function to roll back to the memorized game state
def undo():
    global game, score, win_status
    game = game_state[0]
    score = game_state[1]
    win_status = game_state[2]
    display()


# set the base grid size
grid_size = 4

# set the base values at 0
game = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# define base labels
labels = [[None for _ in range(grid_size)] for _ in range(grid_size)]

# set the base score at 0
score = 0

# set the default win status as false
win_status = False

# set the timer to 0
time_count = 0

# memory of the game state
game_state = []

# dictionary of colors
colors = {0:"#FFFFFF",
        2:"#D3D3D3",
        4:"#A9A9A9",
        8:"#808080",
        16:"#6D6D6D",
        32:"#595959",
        64:"#484848",
        128:"#3D3D3D",
        256:"#2E2E2E",
        512:"#C08D8D",
        1024:"#9E4A4A",
        2048:"#7A2828",
        4096:"#5C1010",
        8192:"#3E0000"}


# horizontal and vertical distance between labels
dx, dy = 104, 97

# horizontal and vertical beginning of the labels
x0_labels, y0_labels = 190, 200

# horizontal and vertical beginning of the title
x0_title, y0_title = 335, 30

# horizontal and vertical beginning of the score display
x0_score, y0_score = 191, 160

# horizontal and vertical beginning of the timer
x0_timer, y0_timer = 328, 600

# horizontal and vertical beginning of the new game button
x0_btn_ng, y0_btn_ng = 485, 150

# horizontal and vertical beginning of the undo button
x0_btn_ud, y0_btn_ud = 415, 150

#horizontal and vertical beginning of the 4x4 button
x0_btn_4x4, y0_btn_4x4 = 330, 100

# horizontal and vertical beginning of the 6x6 button
x0_btn_6x6, y0_btn_6x6 = 397, 100

# creating the window
win = tk.Tk()
win.geometry("800x625")

# image file
bg_image = PhotoImage(file=r"C:\\Dev\\Trimestre3\\MA20\\Projet_2048\\Prog_Projet2048\\2048_bg_image.png")

# background label
label_bg = Label(win, image=bg_image)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# title label
label_title = (Label(text="2048", width=5, height=1, font=("Arial", 30), bg="#2E2E2E", fg="#FFFFFF"))
label_title.place(x=x0_title, y=y0_title)

# score label
label_score = Label(text="Score : 0000", width= 15, height=1, font=("Arial", 15), bg="#2E2E2E", fg="#FFFFFF")
label_score.place(x=x0_score, y=y0_score)

# timer label
label_timer = Label(text="Timer : 0000", width= 15, height=1, font=("Arial", 12), bg="#2E2E2E", fg="#FFFFFF")
label_timer.place(x=x0_timer, y=y0_timer)

# button to start a new game
btn_newGame = tk.Button(win, text="New game", width=10, height=1, font=("Arial", 15), command=start_game, bg="#2E2E2E", fg="#FFFFFF")
btn_newGame.place(x=x0_btn_ng, y=y0_btn_ng)

# button to undo the last move
btn_undo = tk.Button(win, text="Undo", width=5, height=1, font=("Arial", 15), command=undo, bg="#2E2E2E", fg="#FFFFFF")
btn_undo.place(x=x0_btn_ud, y=y0_btn_ud)

# button to switch to 6x6 mode
btn_6x6 = tk.Button(win, text="6x6", width=5, height=1, font=("Arial", 15), command=init_6x6, bg="#2E2E2E", fg="#FFFFFF")
btn_6x6.place(x=x0_btn_6x6, y=y0_btn_6x6)

# button to switch to 4x4 mode
btn_4x4 = tk.Button(win, text="4x4", width=5, height=1, font=("Arial", 15), command=init_4x4, bg="#2E2E2E", fg="#FFFFFF")
btn_4x4.place(x=x0_btn_4x4, y=y0_btn_4x4)


# display game values
def display():
    global score
    for line in range(len(game)):
        for col in range(len(game[line])):
            if game[line][col]>0:
                labels[line][col].config(text=game[line][col], bg=colors[game[line][col]], fg="#000000")
            else:
                labels[line][col].config(text="", bg=colors[game[line][col]])
    # update the displayed score
    label_score.config(text="Score : " + str(score))


init_4x4()
update_timer()
win.bind('<Key>', key_pressed)
win.mainloop()