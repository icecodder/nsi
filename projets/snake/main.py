import tkinter as tk
import random
from tkinter.constants import BOTTOM, END, TOP

# =============================================================================
# Gestion de la fenetre
# =============================================================================

# Dimension de la fenetre
height, width = 500, 500

# Creation de la fenetre avec titre et dimensions
window = tk.Tk()
window.title("Python Snake")
window.geometry(f"{width}x{height + 20}")

# =============================================================================
# Gestion du plateau et des cases
# =============================================================================

# Création du plateau de jeu
plateau = tk.Canvas(window, width=width, height=height, bg="white")
plateau.pack(side=BOTTOM)

# Nombre de cases et taille d'une case
nb_cases = 20
case_height = height / nb_cases
case_width = width / nb_cases

# Case aléatoire
def random_case():
  x = random.randint(0, nb_cases - 1)
  y = random.randint(0, nb_cases - 1)
  return x, y

# Coloration de la case
def fill_case(x, y, color):
  x0 = x * case_width
  y0 = y * case_height
  x1 = x0 + case_width
  y1 = y0 + case_height
  plateau.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)

# =============================================================================
# Gestion du serpent
# =============================================================================

# Vérification de si on est dans le snake
def is_in_snake(case):
  if case in SNAKE:
    return True
  else:
    return False

# Placement du serpent
def draw_snake(snake):
  for x, y in snake:
    fill_case(x, y, "green")

# Mise à jour du serpent
def update_snake():
  global APPLE

  # Récupération de la position du serpent (tete)
  (head_x, head_y) = SNAKE[0]
  # Récupération du mouvement
  mov_x, mov_y = MOV
  
  # Calcul de la nouvelle position du serpent (tete)
  new_head = (head_x + mov_x, head_y + mov_y)

  # Vérification de si on est mort
  death_snake(new_head)

  # Ajout de la nouvelle position au serpent (tete)
  SNAKE.insert(0, new_head)

  # Si on mange une pomme
  if new_head == APPLE:
    # Nouvelle pomme
    APPLE = random_apple()

    # Mise à jour du score
    update_score()
  else:
    # Enleve le dernier element du serpent, on ne grandit pas
    SNAKE.pop()

# Ajout des collisions
def death_snake(new_head):
  global LOSE

  # Coordonnées de la tete du serpent
  head_x, head_y = new_head

  # Si on sort du plateau ou si on mange lui meme, on meurt
  if (is_in_snake(new_head) and MOV != (0, 0) or head_x < 0 or head_y < 0 or head_x >= nb_cases or head_y >= nb_cases):
    LOSE = True

# =============================================================================
# Gestion de la pomme
# =============================================================================

# Pomme aléatoire
def random_apple():
  apple = random_case()
  while is_in_snake(apple):
    apple = random_case()
  return apple

# Placement de la pomme
def draw_apple():
  x, y = APPLE
  fill_case(x, y, "red")

# =============================================================================
# Gestion du clavier
# =============================================================================

# Fonction pour le déplacement du serpent
def left(event):
  global MOV

  if MOV == (1, 0):
    return

  MOV = (-1, 0)
def right(event):
  global MOV

  if MOV == (-1, 0):
    return

  MOV = (1, 0)
def up(event):
  global MOV

  if MOV == (0, 1):
    return

  MOV = (0, -1)
def down(event):
  global MOV

  if MOV == (0, -1):
    return

  MOV = (0, 1)

# On ajoute ces fontions au clavier
window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)

# =============================================================================
# Gestion du score
# =============================================================================

score = tk.Text(window, height=1, width=30)
score.pack(side=TOP)
score.insert(END, "Score: 0")

# Mise à jour du score
def update_score():
  global SCORE

  SCORE += 1
  score.delete(1.0, END)
  score.insert(END, f"Score: {SCORE}")

# =============================================================================

def reset():
  global SNAKE, APPLE, MOV, SCORE, LOSE

  SNAKE = [random_case()] # Serpent initial
  APPLE = random_apple() # Pomme inital
  MOV = (0, 0) # Mouvemement initial, 0 = aucun mouvement
  SCORE = 0 # Score initial
  LOSE = False

# Variable globale
SNAKE = [random_case()] # Serpent initial
APPLE = random_apple() # Pomme inital
MOV = (0, 0) # Mouvemement initial, 0 = aucun mouvement
SCORE = 0 # Score initial
LOSE = False

# Fonction principale
def main():
  # Mise à jour de la fenetre et des événements du clavier
  window.update()
  window.update_idletasks()

  # Mise à jour du serpent
  update_snake()

  # Suppression de tous les elements du plateau
  plateau.delete("all")

  # Ajout des grilles
  size = 500 / nb_cases
  grid_x = 0
  while grid_x <= nb_cases:
    plateau.create_line(0, size * grid_x, width, size * grid_x, fill="#DCDCDC")
    grid_x += 1

  grid_y = 0
  while grid_y <= nb_cases:
    plateau.create_line(size * grid_y, 0, size * grid_y, height, fill="#DCDCDC")
    grid_y += 1

  # Place la pomme sur le plateau
  draw_apple()
  # Place le serpent sur le plateau
  draw_snake(SNAKE)

  if LOSE:
    # Mis à jour du score
    score.delete(1.0, END)
    score.insert(END, f"Perdu avec un score de: {SCORE}")

    # Réinitialisation du jeu
    reset()

    # Rappel de la fonction principale
    window.after(0, main)
  else:
    # Rappel de la fonction principale
    window.after(100, main)

# Appel de la fonction principale au lancement de la fenetre
window.after(0, main)

# Boucle qui affiche la fenetre
window.mainloop()
