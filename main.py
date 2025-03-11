import tkinter as tk  # Importation de la bibliothèque tkinter pour l'interface graphique
from tkinter import messagebox  # Importation de la boîte de message pour afficher les alertes
import random  # Importation de la bibliothèque random pour générer des valeurs aléatoires

# Définition des couleurs pour les nombres basées sur l'image
tile_colors = {
    0: "white",  # Couleur pour les cases vides
    2: "#4D79FF",  # Couleur pour la tuile 2
    4: "#FFF58D",  # Couleur pour la tuile 4
    8: "#FFA64D",  # Couleur pour la tuile 8
    16: "#998000",  # Couleur pour la tuile 16
    32: "#3366CC",  # Couleur pour la tuile 32
    64: "#66CC33",  # Couleur pour la tuile 64
    128: "#00994D",  # Couleur pour la tuile 128
    256: "#000066",  # Couleur pour la tuile 256
    512: "#3366CC",  # Couleur pour la tuile 512
    1024: "#CC3300",  # Couleur pour la tuile 1024
    2048: "#9966CC",  # Couleur pour la tuile 2048
    4096: "#330066",  # Couleur pour la tuile 4096
    8192: "#009933",  # Couleur pour la tuile 8192
}

# Valeurs initiales de la grille
grid_values = [[0, 0, 0, 0] for _ in range(4)]
tile = [[None] * 4 for _ in range(4)]
move_count = 0

# Fonction pour rafraîchir l'affichage de la grille
def display_grid():
    for i in range(4):
        for j in range(4):
            text = "" if grid_values[i][j] == 0 else grid_values[i][j]
            tile[i][j].config(text=text, bg=tile_colors[grid_values[i][j]])

# Fonction pour empiler les tuiles et vérifier si des fusions sont possibles
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

# Ajouter une tuile aléatoire (2 ou 4) dans une case vide
def add_random_tile():
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if grid_values[i][j] == 0]
    if empty_tiles:
        i, j = random.choice(empty_tiles)
        grid_values[i][j] = random.choice([2, 4])

# Démarrer le jeu en ajoutant deux tuiles aléatoires
def start():
    global grid_values, move_count
    grid_values = [[0, 0, 0, 0] for _ in range(4)]
    move_count = 0
    add_random_tile()
    add_random_tile()
    display_grid()
    root.bind('<Key>', key_pressed)  # Rebind the key events

# Définir les mouvements vers la droite
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

# Définir les mouvements vers la gauche
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

# Définir les mouvements vers le haut
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

# Définir les mouvements vers le bas
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

# Vérifier si le jeu est gagné ou perdu
def check_win_loss():
    if any(2048 in row for row in grid_values):
        game_over("You won!", "Félicitations, vous avez atteint 2048!")
    elif not any(0 in row for row in grid_values) and not any_valid_move():
        game_over("Game Over", "Plus de mouvements possibles !")

# Vérifier s'il existe un mouvement valide
def any_valid_move():
    for i in range(4):
        for j in range(4):
            if i < 3 and grid_values[i][j] == grid_values[i + 1][j]:
                return True
            if j < 3 and grid_values[i][j] == grid_values[i][j + 1]:
                return True
    return False

# Afficher la fenêtre de fin de jeu
def game_over(title, message):
    root.unbind('<Key>')  # Désactiver les touches du clavier pendant la fin de jeu
    messagebox.showinfo(title, message)  # Afficher un message de fin de jeu

# Gérer les événements de pression des touches
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

# Créer une instance de la fenêtre principale Tkinter
root = tk.Tk()
root.title("2048")
root.geometry("700x700")

# Ajouter l'image comme background
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Ajouter le titre à la fenêtre
title_label = tk.Label(
    root,
    text="2048",  # Texte du titre
    font=("Arial", 40, "bold"),  # Police du titre
    fg="red" # Couleur du texte (rouge)
)
title_label.pack(anchor="nw", padx=10, pady=10)  # Afficher le titre dans le coin supérieur gauche

# Ajouter le bouton "Nouvelle Partie"
new_game_button = tk.Button(
    root,
    text="Nouvelle Partie",  # Texte du bouton
    font=("Arial", 20, "bold"),  # Police plus grande
    width=15,  # Largeur du bouton
    height=2,  # Hauteur du bouton
    command=start,  # Fonction appelée lors du clic sur le bouton
    bg="#4CAF50",  # Couleur de fond (vert)
    fg="white",  # Couleur du texte
    relief="solid",  # Bordure du bouton
    bd=5  # Épaisseur de la bordure
)

# Placer le bouton "Nouvelle Partie" au bas de la fenêtre
new_game_button.pack(side="bottom", pady=20)  # Utilisation de "side='bottom'" pour le placer en bas avec un peu de marge

# Créer le cadre noir pour la grille
frame = tk.Frame(root, bg="black", padx=5, pady=5)  # Créer un cadre noir pour la grille
frame.pack()  # Placer le cadre dans la fenêtre
frame.place(relx=0.5, rely=0.4, anchor="center")  # Centrer le cadre dans la fenêtre, ajuster la position si nécessaire

# Créer les labels de la grille
for i in range(4):  # Pour chaque ligne
    for j in range(4):  # Pour chaque colonne
        tile[i][j] = tk.Label(
            frame,
            text="",  # Afficher la valeur ou rien si la case est vide
            bg="white",  # Couleur de fond de la tuile
            fg="white",  # Couleur du texte (blanc)
            font=("Arial", 24, "bold"),  # Police du texte
            width=4,  # Largeur du label
            height=2,  # Hauteur du label
            borderwidth=1,  # Largeur du bord
            relief="solid",  # Type de bord
        )
        tile[i][j].grid(row=i, column=j, padx=5, pady=5)  # Placer chaque tuile dans la grille

# Associer les événements de pression de touche à la fonction key_pressed
root.bind('<Key>', key_pressed)

# Démarrer la partie
start()
display_grid()  # Afficher la grille initiale

# Lancer la boucle principale de Tkinter
root.mainloop()  # Exécuter la fenêtre Tkinter