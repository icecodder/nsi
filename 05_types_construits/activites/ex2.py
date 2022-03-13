# Question 1
eleves_1 = [
  ("Martin", "Alice", 5, 15.5),
  ("Dupont", "Marie", 12, 14),
  ("Durand", "Pierre", 14, 16)
]

eleves_2 = [
  ["Martin", "Alice", 5, 15.5],
  ["Dupont", "Marie", 12, 14],
  ["Durand", "Pierre", 14, 16]
]
noms = ["Martin", "Dupont", "Durand"]
prenoms = ["Alice", "Marie", "Pierre"]
devoirs = [(5, 15.5), (12, 14), (14, 16)]
notes = [
  {"nom": "Martin", "prenom": "Alice", "devoirs": (5, 15.5)},
  {"nom": "Dupont", "prenom": "Marie", "devoirs": (12, 14)},
  {"nom": "Durand", "prenom": "Pierre", "devoirs": (14, 16)}
]

# Question 2

def afficher_notes(devoirs):
  for devoir in devoirs:
    for i in devoir:
      print(i)

afficher_notes(devoirs)
