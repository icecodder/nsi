"""
Créer une page html avec une table
DS HTML/CSS - Partie B : Exercice 3
Nom: CHARRIER
Prénom: Max
Classe: 1G2
"""

# Début de la page html
html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Tableau dynamique</title>

  <style>
    table, td {
      border: 1px solid black;
      border-collapse: collapse;
    }
    td {
      padding: 5px;
      text-align: center;
    }
  </style>
</head>
<body>"""

# Début du tableau
html += """
  <table>
"""

# Partie dynamique de la page html
n = 10

for i in range(n + 1):
  html += f"    <tr>\n      <td>{i}</td>\n    </tr>\n"

# Fin du tableau
html += """  </table>"""

# Fin de la page html
html += """
</body>
</html>
"""

try:
  with open("pageWeb.html", "w") as fichier:
    fichier.write(html)
except:
  print("Erreur lors de la création du fichier")
  exit(1)
