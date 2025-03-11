import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

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

grid_values = [[0, 0, 0, 0] for _ in range(4)]
tile = [[None] * 4 for _ in range(4)]
move_count = 0

def display_grid():
    for i in range(4):
        for j in range(4):
            text = "" if grid_values[i][j] == 0 else grid_values[i][j]
            tile[i][j].config(text=text, bg=tile_colors[grid_values[i][j]])

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

def add_random_tile():
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if grid_values[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        grid_values[i][j] = random.choice([2, 4])

def start():
    global grid_values, move_count
    grid_values = [[0, 0, 0, 0] for _ in range(4)]
    move_count = 0
    add_random_tile()
    add_random_tile()
    display_grid()
    root.bind('<Key>', key_pressed)

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

def check_win_loss():
    if any(2048 in row for row in grid_values):
        game_over("You won!", "Félicitations, vous avez atteint 2048!")
    elif not any(0 in row for row in grid_values) and not any_valid_move():
        game_over("Game Over", "Plus de mouvements possibles !")

def any_valid_move():
    for i in range(4):
        for j in range(4):
            if i < 3 and grid_values[i][j] == grid_values[i + 1][j]:
                return True
            if j < 3 and grid_values[i][j] == grid_values[i][j + 1]:
                return True
    return False

def game_over(title, message):
    root.unbind('<Key>')
    messagebox.showinfo(title, message)

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

root = tk.Tk()
root.title("2048")
root.geometry("700x700")

# Adding background image resizing functionality
def update_background():
    global background_image_tk
    background_image_resized = background_image.resize((root.winfo_width(), root.winfo_height()), Image.Resampling.LANCZOS)
    background_image_tk = ImageTk.PhotoImage(background_image_resized)
    background_label.config(image=background_image_tk)

background_image = Image.open("background.png")
background_label = tk.Label(root)
background_label.place(relwidth=1, relheight=1)

# Update background whenever window is resized
root.bind('<Configure>', lambda event: update_background())

title_label = tk.Label(
    root,
    text="2048",
    font=("Arial", 40, "bold"),
    fg="red"
)
title_label.pack(anchor="nw", padx=10, pady=10)

new_game_button = tk.Button(
    root,
    text="Nouvelle Partie",
    font=("Arial", 20, "bold"),
    width=15,
    height=2,
    command=start,
    bg="#4CAF50",
    fg="white",
    relief="solid",
    bd=5
)

new_game_button.pack(side="bottom", pady=20)

frame = tk.Frame(root, bg="black", padx=5, pady=5)
frame.pack()
frame.place(relx=0.5, rely=0.4, anchor="center")

for i in range(4):
    for j in range(4):
        tile[i][j] = tk.Label(
            frame,
            text="",
            bg="white",
            fg="white",
            font=("Arial", 24, "bold"),
            width=4,
            height=2,
            borderwidth=1,
            relief="solid",
        )
        tile[i][j].grid(row=i, column=j, padx=5, pady=5)

root.bind('<Key>', key_pressed)

start()
display_grid()

root.mainloop()
