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
            tile[i][j].config(text=grid_values[i][j] if grid_values[i][j] != 0 else "",bg=tile_colors[grid_values[i][j]])


# création fenêtre
root=tk.Tk()
root.title("2048")
root.geometry("700x700")
root.configure(bg="beige")

title_label = tk.Label(
    root,
    text="2048",
    font=("Arial", 40, "bold"),
)
title_label.pack(anchor="nw", padx=10, pady=10)



score = tk.Frame(root, bg="beige")
score.pack(anchor="center", padx=10, pady=5)

score_label = tk.Label(
    score,
    text="Score: 0",
    font=("Arial", 14)
)
score_label.pack(side="left", padx=5)

top_label = tk.Label(
    score,
    text="Top: 0",
    font=("Arial", 14)
)
top_label.pack(side="left", padx=5)



frame = tk.Frame(root, bg="black", padx=5, pady=5)
frame.pack()
frame.place(relx=0.5, rely=0.5, anchor="center")

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

display_grid()
root.mainloop()

#if __name__ == "__main__":
    #create_2048_grid()

