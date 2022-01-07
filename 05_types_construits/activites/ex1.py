import math

# Question 1
a = (-3, 2, "Triange", "rouge")
b = (-4, -2, "Croix", "rouge")
c = (2, 2, "Cercle", "bleu")
d = (5, -1, "Triange", "bleu")
i = (2, -1, "Cercle", "bleu")
m = (-3.5, 0, "Cercle", "rouge")
points = [a, b, c, d, i, m]
abscisses = [-3, -4, 2, 5, 2, -3.5]
ordonnees = [2, -2, 2, -1, -1, 0]
coordonnees = [(-3, 2), (-4, -2), (2, 2), (5, -1), (2, -1), (-3.5, 0)]

# Question 2
point_a = {"nom": "A", "abscisse": -3, "ordonnees": 2, "symbole": "Triangle", "couleur": "Rouge"}
point_b = {"nom": "B", "abscisse": -4, "ordonnees": -2, "symbole": "Croix", "couleur": "Rouge"}
point_c = {"nom": "C", "abscisse": 2, "ordonnees": 2, "symbole": "Cercle", "couleur": "Bleu"}
point_d = {"nom": "D", "abscisse": 5, "ordonnees": -1, "symbole": "Triangle", "couleur": "Bleu"}
point_i = {"nom": "I", "abscisse": 2, "ordonnees": -1, "symbole": "Cercle", "couleur": "Bleu"}
point_m = {"nom": "M", "abscisse": -3.5, "ordonnees": 0, "symbole": "Cercle", "couleur": "Rouge"}

points_figure = [point_a, point_b, point_c, point_d, point_i, point_m]

# Question 3

def distance_entre_points(point_a, point_b):
  point_a_x = point_a[0]
  point_a_y = point_a[1]

  point_b_x = point_b[0]
  point_b_y = point_b[1]
  
  return math.sqrt((point_a_y - point_a_x) ^ 2 + (point_b_y - point_b_x) ^ 2)

print(distance_entre_points(a, c))

# Question 5

def obtenir_coordonnees(liste_abscisses, liste_ordonnees):
  coordonnees = [(liste_abscisses[i], liste_ordonnees[i]) for i in range(len(liste_abscisses))]
  
  return coordonnees

print(obtenir_coordonnees(abscisses, ordonnees))
