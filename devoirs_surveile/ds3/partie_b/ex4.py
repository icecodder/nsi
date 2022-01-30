"""
Créer une page html avec une table
DS HTML/CSS - Partie B : Exercice 4
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
    <tr>
"""

# Partie dynamique de la page html
n = 10
u = 1

for _ in range(1, n + 1):
  html += f"      <td>{u}</td>\n"
  u = u * 2

# Fin du tableau
html += """
    </tr>
  </table>
"""

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
