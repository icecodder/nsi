<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8" />
    <title>Exercice PHP</title>

    <link rel="stylesheet" href="style.css"/>

    <script src="script.js"> </script>
</head>
<body>
    <div id="container">
        <h2 id="title">Exercice : PHP</h2>
        
        <ul>
            <li>Créer une liste sous la forme d'un tableau sur une ligne</li>
            <li>Un lien crée une liste de 5 valeurs</li>
            <li>Un lien crée une liste de 10 valeurs</li>
            <li>On peut modifier l'url pour obtenir une liste de n valeurs</li>
            <li>Avec 1 <= n <=20</li>
        </ul>

        <form action="exercice1_post.php" method="post">
            <fieldset>
                <legend>Créer une liste de n valeurs</legend>
                <p>Saisir n tel que : 1 <= n <= 20</p>
                <label for="nombre">Nombre de valeurs : </label>
                <input type="number" name="nombre" id="nombre" min="1" max="20" value="5" />
                <input type="submit" value="Créer" />
            </fieldset>
        </form>

        <?php
        if(isset($_POST['nombre'])) {
            $nombre = $_POST['nombre'];

            if ($nombre <1 || $nombre>20) {
                echo '<p>Attention : 1  <= nombre <=20 </p>';
            } else {
                echo "<h2> Liste des valeurs</h2>\n";
                echo "<table>\n";

                for ($i = 1; $i <= $nombre; $i++) {
                    echo "<tr>\n";

                    for ($j = 1; $j <= $nombre; $j++) {
                        $s = $i + $j;

                        echo "<td style='border: 3px solid #1C6EA4;'>" . $s . "</td>\n";
                    }

                    echo "</tr>\n";
                }

                echo "</table>\n";
            }
        }
        ?>
    </div>
</body>
</html>
