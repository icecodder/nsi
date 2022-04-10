<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire</title>
</head>
<body>
    <table style="width: 50%">
        <caption>Interprétation de la saisie du formulaire</caption>

        <thead>
            <tr>
                <th>Variable</th>
                <th>Valeur</th>
            </tr>
        </thead>

        <?php
            echo "Page dynamique générée par PHP";

            $nom = $_POST["nom"];
            $prenom = $_POST["prenom"];
            $age = $_POST["age"];
            $message = $_POST["message"];
            $sexe = $_POST["sexe"];
            $redouble = $_POST["redouble"];

            if (isset($_POST["francais"])) {
                $francais = "Oui";
            } else {
                $francais = "Non";
            }

            if (isset($_POST["anglais"])) {
                $anglais = "Oui";
            } else {
                $anglais = "Non";
            }

            $nom = strtoupper($nom);
            $prenom = strtoupper($prenom);
            $age = intval($age);

            echo "<tr><td>Nom : </td><td>" . $nom . "</td></tr>";
            echo "<tr><td>Prénom : </td><td>" . $prenom . "</td></tr>";
            echo "<tr><td>Age : </td><td>" . $age . "</td></tr>";
            echo "<tr><td>Message : </td><td>" . $message . "</td></tr>";
            echo "<tr><td>Français : </td><td>" . $francais . "</td></tr>";
            echo "<tr><td>Anglais : </td><td>" . $anglais . "</td></tr>";
            echo "<tr><td>Sexe : </td><td>" . $sexe . "</td></tr>";
            echo "<tr><td>Redouble : </td><td>" . $redouble . "</td></tr>";
        ?>
    </table>
</body>
</html>
