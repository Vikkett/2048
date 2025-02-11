# C:\Users\px75qgn\Desktop\pythonn\2048.py
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Nom : 2048.py
Date : 28.01.2025
Version : 0.0.1
Purpose : affichage d'un exemple du jeu 2048
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

# Initial grid values from the image
grid_values = [
    [1024, 8, 0, 256],
    [2, 0, 32, 0],
    [2048, 4, 64, 4096],
    [16, 128, 512, 8192]
]

tile=[[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]

# rafraichit toute la grille
def display_grid():
    for i in range(4):
        for j in range(4):
            if grid_values[i][j]==0:
                text=""
            else :
                text=grid_values[i][j]
            tile[i][j].config(text=text,bg=tile_colors[grid_values[i][j]])



def pack4(a,b,c,d):
    nm=0
    if c==0 and d != 0:
        c = d
        d = 0
        nm+=1
    if b == 0 and c != 0:
        b,c,d = c,d,0
        nm+=1
    if a == 0 and b != 0:
        a, b, c, d = b, c, d, 0
        nm += 1
    if a == b and a != 0:
        a = 2 * a
        b = c
        c = d
        d = 0
        nm+=1
    if b == c and b > 0:
        b = 2 * b
        c = d
        d = 0
        nm+=1
    if c == d and c > 0:
        c = 2 * c
        d = 0
        nm+=1
    return(a,b,c,d), nm

print(pack4(2,2,4,0 ))
# création fenêtre
root=tk.Tk()

frame = tk.Frame(root, bg="black", padx=5, pady=5)
frame.pack()

for i in range(4):
    for j in range(4):
        value = grid_values[i][j]
        color = tile_colors.get(value, "white")  # Default to white if value not found

        tile[i][j] = tk.Label(
            frame,
            text=str(value) if value != 0 else "",
            bg=color,
            fg="white" if value > 0 else "black",
            font=("Arial", 24, "bold"),
            width=4,
            height=2,
            borderwidth=1,
            relief="solid",
        )
        tile[i][j].grid(row=i, column=j, padx=5, pady=5)

def right():
    print("right")
    for line in range(4):
        (grid_values[line][3],grid_values[line][2],grid_values[line][1],grid_values[line][0]),nm = pack4(grid_values[line][3],grid_values[line][2],grid_values[line][1],grid_values[line][0])
    display_grid()

def left():
    print("left")
    for line in range(4):
        (grid_values[line][0], grid_values[line][1], grid_values[line][2], grid_values[line][3]), nm = pack4(grid_values[line][0],grid_values[line][1],grid_values[line][2],grid_values[line][3])
        display_grid()

def moveup():
    print("up")
    for col in range(4):
        (grid_values[0][col], grid_values[1][col], grid_values[2][col], grid_values[3][col]), nm = pack4(grid_values[0][col], grid_values[1][col], grid_values[2][col], grid_values[3][col])
        display_grid()


def movedown():
    print("down")
    for col in range(4):
        (grid_values[3][col], grid_values[2][col], grid_values[1][col], grid_values[0][col]), nm = pack4(grid_values[3][col], grid_values[2][col], grid_values[1][col], grid_values[0][col])
        display_grid()


def key_pressed(event) :
    touche=event.keysym #récupérer le symbole de la touche
    if (touche=="Right" or touche=="d" or touche=="D"):
       right()
    if (touche=="Left" or touche=="a" or touche=="A"):
        left()
    if (touche == "Up" or touche == "w" or touche == "W"):
        moveup()
    if (touche == "Down" or touche == "s" or touche == "S"):
        movedown()
    if (touche=="Q" or touche=="q"):
        result=messagebox.askokcancel("Confirmation", "vraiment quitter ?")
        if result:
            quit()

root.bind('<Key>', key_pressed) #on traite les touches clavier



display_grid()
root.mainloop()