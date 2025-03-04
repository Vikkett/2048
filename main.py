# C:\Users\px75qgn\Desktop\2048-right-version
# -*- coding: utf-8 -*-

#--------1---------2---------3---------4---------5---------6---------7---------8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
"""
Nom : 2048.py
Author: Viktoriia Varennyk
Date : 28.01.2025
Version : 0.0.1
Purpose : affichage d'un exemple du jeu 2048
"""

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

# Valeurs initiales de la grille mais les casses sont vides pour afficher random chiffres
grid_values = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Initialisation des variables pour chaque tuile de la grille
tile = [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]

# Compteur de mouvements
move_count = 0

# Fonction pour rafraîchir l'affichage de la grille
def display_grid():
    for i in range(4):  # Pour chaque ligne de la grille
        for j in range(4):  # Pour chaque colonne de la grille
            if grid_values[i][j] == 0:  # Si la case est vide
                text = ""  # Afficher rien (case vide)
            else:
                text = grid_values[i][j]  # Sinon, afficher la valeur de la case
            tile[i][j].config(text=text, bg=tile_colors[grid_values[i][j]])  # Mettre à jour l'affichage de la tuile

# Fonction pour empiler les tuiles et vérifier si des fusions sont possibles
def pack4(a, b, c, d):
    nm = 0  # Initialisation du nombre de mouvements
    if c == 0 and d != 0:  # Si la case c est vide et d n'est pas vide
        c = d  # Déplacer d à la place de c
        d = 0  # Rendre d vide
        nm += 1  # Augmenter le compteur de mouvements
    if b == 0 and c != 0:  # Si la case b est vide et c n'est pas vide
        b, c, d = c, d, 0  # Déplacer c à la place de b et d à la place de c
        nm += 1  # Augmenter le compteur de mouvements
    if a == 0 and b != 0:  # Si la case a est vide et b n'est pas vide
        a, b, c, d = b, c, d, 0  # Déplacer b à la place de a et déplacer c, d vers la droite
        nm += 1  # Augmenter le compteur de mouvements
    if a == b and a != 0:  # Si a et b sont égaux et non nuls
        a = 2 * a  # Fusionner a et b (doubler a)
        b = c  # Déplacer c à la place de b
        c = d  # Déplacer d à la place de c
        d = 0  # Rendre d vide
        nm += 1  # Augmenter le compteur de mouvements
    if b == c and b > 0:  # Si b et c sont égaux et non nuls
        b = 2 * b  # Fusionner b et c (doubler b)
        c = d  # Déplacer d à la place de c
        d = 0  # Rendre d vide
        nm += 1  # Augmenter le compteur de mouvements
    if c == d and c > 0:  # Si c et d sont égaux et non nuls
        c = 2 * c  # Fusionner c et d (doubler c)
        d = 0  # Rendre d vide
        nm += 1  # Augmenter le compteur de mouvements
    return (a, b, c, d), nm  # Retourner les nouvelles valeurs et le nombre de mouvements

# Ajouter une tuile aléatoire (2 ou 4) dans une case vide
def add_random_tile():
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if grid_values[i][j] == 0]  # Trouver les cases vides
    if empty_tiles:  # S'il y a des cases vides
        i, j = random.choice(empty_tiles)  # Choisir une case vide aléatoire
        grid_values[i][j] = random.choice([2, 4])  # Placer une tuile 2 ou 4 dans la case

# Démarrer le jeu en ajoutant deux tuiles aléatoires
def start():
    global grid_values  # Déclarer grid_values comme global
    global move_count  # Déclarer move_count comme global
    grid_values = [  # Réinitialiser la grille
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    move_count = 0  # Réinitialiser le compteur de mouvements
    add_random_tile()  # Ajouter une tuile aléatoire
    add_random_tile()  # Ajouter une autre tuile aléatoire

#pour verifier si fenetre de ganger est marche
    grid_values[0][0] = 1024
    grid_values[0][1] = 1024


    display_grid()  # Afficher la grille mise à jour

# Définir les mouvements vers la droite
def right():
    move_count = 0  # Réinitialiser le compteur de mouvements
    for line in range(4):  # Pour chaque ligne de la grille
        (grid_values[line][3], grid_values[line][2], grid_values[line][1], grid_values[line][0]), nm = pack4(
            grid_values[line][3], grid_values[line][2], grid_values[line][1], grid_values[line][0])  # Appliquer pack4
        move_count += nm  # Ajouter le nombre de mouvements effectués
    if move_count > 0:  # Si des mouvements ont eu lieu
        add_random_tile()  # Ajouter une nouvelle tuile
    display_grid()  # Rafraîchir l'affichage de la grille
    check_win_loss()  # Vérifier si le jeu est gagné ou perdu

# Définir les mouvements vers la gauche
def left():
    move_count = 0  # Réinitialiser le compteur de mouvements
    for line in range(4):  # Pour chaque ligne de la grille
        (grid_values[line][0], grid_values[line][1], grid_values[line][2], grid_values[line][3]), nm = pack4(
            grid_values[line][0], grid_values[line][1], grid_values[line][2], grid_values[line][3])  # Appliquer pack4
        move_count += nm  # Ajouter le nombre de mouvements effectués
    if move_count > 0:  # Si des mouvements ont eu lieu
        add_random_tile()  # Ajouter une nouvelle tuile
    display_grid()  # Rafraîchir l'affichage de la grille
    check_win_loss()  # Vérifier si le jeu est gagné ou perdu

# Définir les mouvements vers le haut
def moveup():
    move_count = 0  # Réinitialiser le compteur de mouvements
    for col in range(4):  # Pour chaque colonne de la grille
        (grid_values[0][col], grid_values[1][col], grid_values[2][col], grid_values[3][col]), nm = pack4(
            grid_values[0][col], grid_values[1][col], grid_values[2][col], grid_values[3][col])  # Appliquer pack4
        move_count += nm  # Ajouter le nombre de mouvements effectués
    if move_count > 0:  # Si des mouvements ont eu lieu
        add_random_tile()  # Ajouter une nouvelle tuile
    display_grid()  # Rafraîchir l'affichage de la grille
    check_win_loss()  # Vérifier si le jeu est gagné ou perdu

# Définir les mouvements vers le bas
def movedown():
    move_count = 0  # Réinitialiser le compteur de mouvements
    for col in range(4):  # Pour chaque colonne de la grille
        (grid_values[3][col], grid_values[2][col], grid_values[1][col], grid_values[0][col]), nm = pack4(
            grid_values[3][col], grid_values[2][col], grid_values[1][col], grid_values[0][col])  # Appliquer pack4
        move_count += nm  # Ajouter le nombre de mouvements effectues
    if move_count > 0:  # Si des mouvements ont eu lieu
        add_random_tile()  # Ajouter une nouvelle tuile
    display_grid()  # Rafraîchir l'affichage de la grille
    check_win_loss()  # Vérifier si le jeu est gagné ou perdu

# Vérifier si le jeu est gagné ou perdu
def check_win_loss():
    if any(2048 in row for row in grid_values):  # Si une tuile 2048 est présente
        game_over("You won!", "Félicitations, vous avez atteint 2048!")  # Afficher un message de victoire
    elif not any(0 in row for row in grid_values) and not any_valid_move():  # Si aucune case vide et pas de mouvement valide
        game_over("Game Over", "Plus de mouvements possibles !")  # Afficher un message de défaite

# Vérifier s'il existe un mouvement valide
def any_valid_move():
    for i in range(4):  # Pour chaque ligne
        for j in range(4):  # Pour chaque colonne
            if i < 3 and grid_values[i][j] == grid_values[i + 1][j]:  # Vérifier si des fusions verticales sont possibles
                return True
            if j < 3 and grid_values[i][j] == grid_values[i][j + 1]:  # Vérifier si des fusions horizontales sont possibles
                return True
            if grid_values[i][j] == 0:  # Vérifier si la case est vide
                return True
    return False  # Si aucune fusion n'est possible

# Afficher la fenêtre de fin de jeu
def game_over(title, message):
    root.unbind('<Key>')  # Désactiver les touches du clavier pendant la fin de jeu
    result = messagebox.showinfo(title, message)  # Afficher un message de fin de jeu

# Gérer les événements de pression des touches
def key_pressed(event):
    touche = event.keysym  # Récupérer la touche pressée
    if touche == "Right" or touche == "d" or touche == "D":  # Si la touche est "Right", "d" ou "D"
        right()  # Effectuer le mouvement vers la droite
    if touche == "Left" or touche == "a" or touche == "A":  # Si la touche est "Left", "a" ou "A"
        left()  # Effectuer le mouvement vers la gauche
    if touche == "Up" or touche == "w" or touche == "W":  # Si la touche est "Up", "w" ou "W"
        moveup()  # Effectuer le mouvement vers le haut
    if touche == "Down" or touche == "s" or touche == "S":  # Si la touche est "Down", "s" ou "S"
        movedown()  # Effectuer le mouvement vers le bas
    if touche == "Q" or touche == "q":  # Si la touche est "Q" ou "q"
        result = messagebox.askokcancel("Confirmation", "Vraiment quitter ?")  # Demander si on veut quitter
        if result:  # Si la réponse est "Oui"
            print(f"Game Over! T'as fait {move_count} mouvement.")  # Afficher le nombre de mouvements
            quit()  # Quitter le jeu

# Associer les événements de pression de touche à la fonction key_pressed
root = tk.Tk()  # Créer une instance de la fenêtre principale Tkinter
root.title("2048")  # Définir le titre de la fenêtre
root.geometry("700x700")  # Définir la taille de la fenêtre
root.configure(bg="beige")  # Définir la couleur de fond de la fenêtre

# Ajouter le titre à la fenêtre
title_label = tk.Label(
    root,
    text="2048",  # Texte du titre
    font=("Arial", 40, "bold"),  # Police du titre
    bg="beige"  # Couleur de fond du titre
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
        value = grid_values[i][j]  # Récupérer la valeur de la case
        color = tile_colors.get(value, "white")  # Récupérer la couleur de la tuile en fonction de la valeur
        tile[i][j] = tk.Label(
            frame,
            text=str(value) if value != 0 else "",  # Afficher la valeur ou rien si la case est vide
            bg=color,  # Couleur de fond de la tuile
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
