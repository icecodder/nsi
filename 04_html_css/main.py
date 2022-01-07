import math

a = 0
b = 50

html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Page dynamique avec Python - Tableau dynamique</title>

  <link rel="stylesheet" type="text/css" href="./style.css">
</head>
"""

html += """
<body>
  <p>Je suis une page dynamique</p>
  <p>Le tableau est produit par une boucle dans le code Python</p>
"""

html += """
  <table id="t01">
    <tr id="name">
      <th>x</th>
      <th>sin(x)</th>
      <th>cos(x)</th>
    </tr>
"""

for x in range(a, b + 1):
  html += "\n"

  if (x % 2 == 0):
    html += "<tr class=\"paire\">\n"
  else:
    html += "<tr class=\"impaire\">\n"

  html += f"<td class=\"col\">{str(x)}</td>\n"
  html += f"<td>{str(math.sin(x))}</td>\n"
  html += f"<td>{str(math.cos(x))}</td>\n"
  html += "</tr>\n"

html += """
  </table>
</body>
</html>
"""

try:
  with open("page4.html", "w") as file:
    file.write(html)
except:
  print("Erreur lros de la création du fichier")
  exit(1)
