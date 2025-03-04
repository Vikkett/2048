# C:\Users\px75qgn\Desktop\2048-right-version
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Nom : 2048.py
Date : 28.01.2025
Version : 0.0.1
Purpose : le jeu 2048
author : Varennyk Viktoriia
"""

import tkinter as tk
from tkinter import messagebox
import random

# Define the colors for the numbers based on the image
tile_colors = {
    0: "white",
    2: "#4D79FF",
    4: "#FFF58D",
    8: "#FFA64D",
    16: "#998000",
    32: "#3366CC",
    64: "#66CC33",
    128: "#00994D",
    256: "#000066",
    512: "#3366CC",
    1024: "#CC3300",
    2048: "#9966CC",
    4096: "#330066",
    8192: "#009933",
}

# Initial grid values
grid_values = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

tile = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

# Initialize move counter
move_count = 0


# Refresh the grid display
def display_grid():
    for i in range(4):
        for j in range(4):
            if grid_values[i][j] == 0:
                text = ""
            else:
                text = grid_values[i][j]
            tile[i][j].config(text=text, bg=tile_colors[grid_values[i][j]])


# Function to pack the tiles and check if merges are possible
def pack4(a, b, c, d):
    nm = 0
    if c == 0 and d != 0:
        c = d
        d = 0
        nm += 1
    if b == 0 and c != 0:
        b, c, d = c, d, 0
        nm += 1
    if a == 0 and b != 0:
        a, b, c, d = b, c, d, 0
        nm += 1
    if a == b and a != 0:
        a = 2 * a
        b = c
        c = d
        d = 0
        nm += 1
    if b == c and b > 0:
        b = 2 * b
        c = d
        d = 0
        nm += 1
    if c == d and c > 0:
        c = 2 * c
        d = 0
        nm += 1
    return (a, b, c, d), nm


# Add a random tile (2 or 4) in an empty spot
def add_random_tile():
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if grid_values[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        grid_values[i][j] = random.choice([2, 4])


# Start the game by adding two random tiles
def start():
    global grid_values
    global move_count
    grid_values = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    move_count = 0
    add_random_tile()
    add_random_tile()
    display_grid()


# Move right
def right():
    global move_count
    move_count = 0
    for line in range(4):
        (grid_values[line][3], grid_values[line][2], grid_values[line][1], grid_values[line][0]), nm = pack4(
            grid_values[line][3], grid_values[line][2], grid_values[line][1], grid_values[line][0])
        move_count += nm
    if move_count > 0:
        add_random_tile()
    display_grid()
    check_win_loss()


# Move left
def left():
    global move_count
    move_count = 0
    for line in range(4):
        (grid_values[line][0], grid_values[line][1], grid_values[line][2], grid_values[line][3]), nm = pack4(
            grid_values[line][0], grid_values[line][1], grid_values[line][2], grid_values[line][3])
        move_count += nm
    if move_count > 0:
        add_random_tile()
    display_grid()
    check_win_loss()


# Move up
def moveup():
    global move_count
    move_count = 0
    for col in range(4):
        (grid_values[0][col], grid_values[1][col], grid_values[2][col], grid_values[3][col]), nm = pack4(
            grid_values[0][col], grid_values[1][col], grid_values[2][col], grid_values[3][col])
        move_count += nm
    if move_count > 0:
        add_random_tile()
    display_grid()
    check_win_loss()


# Move down
def movedown():
    global move_count
    move_count = 0
    for col in range(4):
        (grid_values[3][col], grid_values[2][col], grid_values[1][col], grid_values[0][col]), nm = pack4(
            grid_values[3][col], grid_values[2][col], grid_values[1][col], grid_values[0][col])
        move_count += nm
    if move_count > 0:
        add_random_tile()
    display_grid()
    check_win_loss()


# Check for win condition (2048 reached)
def check_win_loss():
    # Check for win
    if any(2048 in row for row in grid_values):
        game_over("You won!", "Congratulations, you reached 2048!")
    # Check for loss (no valid moves left)
    elif not any(0 in row for row in grid_values) and not any_valid_move():
        game_over("Game Over", "No valid moves left!")


# Check if any valid moves are possible
def any_valid_move():
    for i in range(4):
        for j in range(4):
            if i < 3 and grid_values[i][j] == grid_values[i + 1][j]:  # Check vertical merges
                return True
            if j < 3 and grid_values[i][j] == grid_values[i][j + 1]:  # Check horizontal merges
                return True
            if grid_values[i][j] == 0:  # Check if there's any empty space
                return True
    return False


# Show game over window
def game_over(title, message):
    # Disable the movement keys while game is over
    root.unbind('<Key>')
    result = messagebox.showinfo(title, message)


# Handle key press events
def key_pressed(event):
    touche = event.keysym
    if touche == "Right" or touche == "d" or touche == "D":
        right()
    if touche == "Left" or touche == "a" or touche == "A":
        left()
    if touche == "Up" or touche == "w" or touche == "W":
        moveup()
    if touche == "Down" or touche == "s" or touche == "S":
        movedown()
    if touche == "Q" or touche == "q":
        result = messagebox.askokcancel("Confirmation", "Vraiment quitter ?")
        if result:
            print(f"Game Over! T'as fait {move_count} mouvement.")
            quit()


# Bind key presses to the key_pressed function
root = tk.Tk()
root.title("2048")
root.geometry("700x700")
root.configure(bg="beige")

# Add title and score labels
title_label = tk.Label(
    root,
    text="2048",
    font=("Arial", 40, "bold"),
    bg="beige"
)
title_label.pack(anchor="nw", padx=10, pady=10)

# Add New Game button with image background
button_image = tk.PhotoImage(file="")
new_game_button = tk.Button(root, image=button_image, command=start)
new_game_button.image = button_image  # Keep a reference to the image
new_game_button.pack(pady=20)  # You can adjust the padding

frame = tk.Frame(root, bg="black", padx=5, pady=5)
frame.pack()
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create the grid labels
for i in range(4):
    for j in range(4):
        value = grid_values[i][j]
        color = tile_colors.get(value, "white")
        tile[i][j] = tk.Label(
            frame,
            text=str(value) if value != 0 else "",
            bg=color,
            fg="white",
            font=("Arial", 24, "bold"),
            width=4,
            height=2,
            borderwidth=1,
            relief="solid",
        )
        tile[i][j].grid(row=i, column=j, padx=5, pady=5)

# Bind the key press event to the game functions
root.bind('<Key>', key_pressed)

# Start the game
start()
display_grid()

# Run the Tkinter main loop
root.mainloop()
