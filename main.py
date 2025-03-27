import tkinter as tk  # Importer la bibliothèque tkinter pour créer l'interface graphique
from tkinter import messagebox  # Importer messagebox pour afficher des messages
import random  # Importer random pour générer des nombres aléatoires
from PIL import Image, ImageTk  # Importer PIL pour la gestion des images

# Dictionnaire pour définir les couleurs des tuiles en fonction de leurs valeurs
tile_colors = {
    0: "white",  # Couleur pour les tuiles vides
    2: "#4D79FF",  # Couleur pour la tuile avec la valeur 2
    4: "#FFF58D",  # Couleur pour la tuile avec la valeur 4
    8: "#FFA64D",  # Couleur pour la tuile avec la valeur 8
    16: "#998000",  # Couleur pour la tuile avec la valeur 16
    32: "#3366CC",  # Couleur pour la tuile avec la valeur 32
    64: "#66CC33",  # Couleur pour la tuile avec la valeur 64
    128: "#00994D",  # Couleur pour la tuile avec la valeur 128
    256: "#000066",  # Couleur pour la tuile avec la valeur 256
    512: "#3366CC",  # Couleur pour la tuile avec la valeur 512
    1024: "#CC3300",  # Couleur pour la tuile avec la valeur 1024
    2048: "#9966CC",  # Couleur pour la tuile avec la valeur 2048
    4096: "#330066",  # Couleur pour la tuile avec la valeur 4096
    8192: "#009933",  # Couleur pour la tuile avec la valeur 8192
}

# Initialiser la grille de jeu et les variables de score
grid_values = [[0, 0, 0, 0] for _ in range(4)]  # Créer une grille 4x4 initialisée à zéro
tile = [[None] * 4 for _ in range(4)]  # Créer une liste pour contenir les objets de tuile
move_count = 0  # Initialiser le compteur de mouvements
score = 0  # Initialiser le score actuel
best_score = 0  # Initialiser le meilleur score

def display_grid():
    """Le label de score est appelé après chaque mouvement pour réactualiser l'affichage des scores.

       Si un joueur fusionne des tuiles, son score augmente, donc l'affichage doit être mis à jour immédiatement."""
    for i in range(4):
        for j in range(4):
            text = "" if grid_values[i][j] == 0 else grid_values[i][j]  # Définir le texte comme vide si la tuile est 0
            tile[i][j].config(text=text, bg=tile_colors[grid_values[i][j]])  # Mettre à jour l'affichage de la tuile
    score_label.config(text=f"Score: {score}")  # .config(text=f"Score: {score}") change son texte pour refléter la valeur actuelle de score, f"Score: {score}" est une f-string, qui insère la valeur actuelle de score dans la chaîne de caractères
    top_score_label.config(text=f"Top : {best_score}")  # .config(text=f"Top : {best_score}") met à jour ce label avec la valeur actuelle de best_score

def pack4(a, b, c, d):
    """Fusionner les tuiles dans une ligne ou une colonne."""
    global score  # Accéder à la variable de score globale
    nm = 0  # Initialiser le compteur de mouvements
    # Déplacer les tuiles vers la droite et fusionner si nécessaire
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
        score += 2 * a  # Mettre à jour le score
        a = 2 * a
        b = c
        c = d
        d = 0
        nm += 1
    if b == c and b > 0:
        score += 2 * b  # Mettre à jour le score
        b = 2 * b
        c = d
        d = 0
        nm += 1
    if c == d and c > 0:
        score += 2 * c  # Mettre à jour le score
        c = 2 * c
        d = 0
        nm += 1
    return (a, b, c, d), nm  # Retourner les nouvelles valeurs et le nombre de mouvements

def add_random_tile():
    """Ajouter une tuile aléatoire (2 ou 4) à une position vide dans la grille."""
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if grid_values[i][j] == 0]  # Trouver les tuiles vides
    if empty_tiles:  # S'il y a des tuiles vides
        i, j = random.choice(empty_tiles)  # Choisir une tuile vide aléatoire
        grid_values[i][j] = random.choice([2, 4])  # Ajouter une tuile avec la valeur 2 ou 4

def start():
    """Démarrer une nouvelle partie en réinitialisant la grille et le score."""
    global grid_values, move_count, score, best_score
    grid_values = [[0, 0, 0, 0] for _ in range(4)]  # Réinitialiser la grille
    move_count = 0  # Réinitialiser le compteur de mouvements
    score = 0  # Réinitialiser le score
    add_random_tile()  # Ajouter deux tuiles aléatoires
    add_random_tile()
    display_grid()  # Afficher la grille mise à jour
    root.bind('<Key>', key_pressed)  # Lier les pressions de touches aux actions

def right():
    """Déplacer les tuiles vers la droite."""
    global move_count
    move_count = 0  # Réinitialiser le compteur de mouvements
    for line in range(4):
        (grid_values[line][3], grid_values[line][2], grid_values[line][1], grid_values[line][0]), nm = pack4(
            grid_values[line][3], grid_values[line][2], grid_values[line][1], grid_values[line][0])  # Appliquer pack4
        move_count += nm  # Mettre à jour le compteur de mouvements
    if move_count > 0:  # Si des mouvements ont été effectués
        add_random_tile()  # Ajouter une tuile aléatoire
    display_grid()  # Afficher la grille mise à jour
    check_win_loss()  # Vérifier les conditions de victoire/perte

def left():
    """Déplacer les tuiles vers la gauche."""
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
    """Déplacer les tuiles vers le haut."""
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
    """Déplacer les tuiles vers le bas."""
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
    """Vérifier si le joueur a gagné ou perdu."""
    global best_score  # Accéder à la variable du meilleur score global
    if score > best_score:
        best_score = score  # Chaque fois que check_win_loss() est appelée (après un mouvement), on vérifie si le score actuel est supérieur à best_score
    if any(2048 in row for row in grid_values):  # Vérifiez si le joueur a atteint 2048
        game_over("Vous avez gagné!", "Félicitations, vous avez atteint 2048!")  # Afficher le message de victoire
    elif not any(0 in row for row in grid_values) and not any_valid_move():  # Vérifiez si la partie est perdue
        game_over("Fin de partie", "Plus de mouvements possibles !")  # Afficher le message de fin de partie

def any_valid_move():
    """Vérifier s'il reste des mouvements valides."""
    for i in range(4):
        for j in range(4):
            if i < 3 and grid_values[i][j] == grid_values[i + 1][j]:  # Vérifier les mouvements verticaux
                return True
            if j < 3 and grid_values[i][j] == grid_values[i][j + 1]:  # Vérifier les mouvements horizontaux
                return True
    return False  # Aucun mouvement valide trouvé

def game_over(title, message):
    """Afficher un message de fin de jeu et désactiver l'entrée au clavier."""
    root.unbind('<Key>')  # Désactiver la saisie au clavier
    messagebox.showinfo(title, message)  # Afficher la boîte de message avec le titre et le message

def key_pressed(event):
    """Gérer l'entrée du clavier pour déplacer les tuiles."""
    touche = event.keysym  # Récupérer la touche enfoncée
    if touche == "Right" or touche == "d" or touche == "D":
        right()  # Déplacer à droite
    if touche == "Left" or touche == "a" or touche == "A":
        left()  # Déplacer à gauche
    if touche == "Up" or touche == "w" or touche == "W":
        moveup()  # Déplacer vers le haut
    if touche == "Down" or touche == "s" or touche == "S":
        movedown()  # Déplacer vers le bas
    if touche == "Q" or touche == "q":  # Quitter le jeu
        result = messagebox.askokcancel("Confirmation", "Vraiment quitter ?")  # Demander confirmation
        if result:
            print(f"Fin de partie ! T'as fait {move_count} mouvement.")  # Afficher le nombre de mouvements
            quit()  # Quitter le programme

root = tk.Tk()  # Créer la fenêtre principale
root.title("2048")  # Définir le titre de la fenêtre
root.geometry("700x700")  # Définir la taille de la fenêtre

# Fonction pour mettre à jour l'image de fond
def update_background():
    global background_image_tk
    background_image_resized = background_image.resize((root.winfo_width(), root.winfo_height()), Image.Resampling.LANCZOS)  # Redimensionner l'image de fond
    background_image_tk = ImageTk.PhotoImage(background_image_resized)  # Convertir l'image redimensionnée au format Tkinter
    background_label.config(image=background_image_tk)  # Mettre à jour le label de fond avec la nouvelle image

background_image = Image.open("background.png")  # Charger l'image de fond
background_label = tk.Label(root)  # Créer un label pour le fond
background_label.place(relwidth=1, relheight=1)  # Définir le label pour couvrir toute la fenêtre

# Mettre à jour le fond chaque fois que la fenêtre est redimensionnée
root.bind('<Configure>', lambda event: update_background())  # Lier l'événement de redimensionnement pour mettre à jour le fond

title_label = tk.Label(
    root,
    text="2048",  # Titre du jeu
    font=("Arial", 40, "bold"),  # Style de police pour le titre
    fg="red"  # Couleur du titre
)
title_label.pack(anchor="nw", padx=10, pady=10)  # Placer le label du titre dans la fenêtre

# Ajouter un label pour le meilleur score
top_score_label = tk.Label(
    root,
    text="Meilleur Score: 0",  # Affichage initial du meilleur score
    font=("Arial", 20),  # Style de police pour le meilleur score
    fg="black"  # Couleur pour le meilleur score
)
top_score_label.pack(anchor="ne", padx=10, pady=(0, 5))  # Placer le label du meilleur score dans la fenêtre

# Label de score
score_label = tk.Label(
    root,
    text="Score: 0",  # Affichage initial du score
    font=("Arial", 20),  # Style de police pour le score
    fg="black"  # Couleur pour le score
)
score_label.pack(anchor="ne", padx=10, pady=(0, 10))  # Placer le label de score dans la fenêtre

# Bouton pour démarrer une nouvelle partie
new_game_button = tk.Button(
    root,
    text="Nouvelle Partie",  # Texte du bouton
    font=("Arial", 20, "bold"),  # Style de police pour le bouton
    width=15,  # Largeur du bouton
    height=2,  # Hauteur du bouton
    command=start,  # Commande pour démarrer une nouvelle partie
    bg="#4CAF50",  # Couleur de fond du bouton
    fg="white",  # Couleur du texte du bouton
    relief="solid",  # Style de relief du bouton
    bd=5  # Largeur de la bordure du bouton
)
new_game_button.pack(side="bottom", pady=20)  # Placer le bouton en bas de la fenêtre

frame = tk.Frame(root, bg="black", padx=5, pady=5)  # Créer un cadre pour les tuiles
frame.pack()  # Pack le cadre
frame.place(relx=0.5, rely=0.4, anchor="center")  # Centrer le cadre dans la fenêtre

# Créer les tuiles dans la grille
for i in range(4):
    for j in range(4):
        tile[i][j] = tk.Label(
            frame,
            text="",  # Texte initial pour la tuile
            bg="white",  # Couleur de fond initiale pour la tuile
            fg="white",  # Couleur de texte initiale pour la tuile
            font=("Arial", 24, "bold"),  # Style de police pour la tuile
            width=4,  # Largeur de la tuile
            height=2,  # Hauteur de la tuile
            borderwidth=1,  # Largeur de la bordure de la tuile
            relief="solid",  # Style de relief de la tuile
        )
        tile[i][j].grid(row=i, column=j, padx=5, pady=5)  # Placer la tuile dans la grille

root.bind('<Key>', key_pressed)  # Lier les pressions de touches à la fonction key_pressed

start()  # Démarrer le jeu
display_grid()  # Afficher la grille initiale

root.mainloop()  # Démarrer la boucle d'événements Tkinter