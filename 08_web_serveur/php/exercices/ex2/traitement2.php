<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire</title>
</head>
<body>
    <?php
        $classe = $_POST["classe"];
        $nom = $_POST["nom"];
        $prenom = $_POST["prenom"];
        $age = $_POST["age"];
        $q1 = $_POST["q1"];

        if (isset($_POST["q2rep1"])) {
            $q2rep1 = 1;
        } else {
            $q2rep1 = 0;
        }
        
        if (isset($_POST["q2rep2"])) {
            $q2rep2 = 1;
        } else {
            $q2rep2 = 0;
        }
        
        if (isset($_POST["q2rep3"])) {
            $q2rep3 = 1;
        } else {
            $q2rep3 = 0;
        }
        
        if (isset($_POST["q2rep4"])) {
            $q2rep4 = 1;
        } else {
            $q2rep4 = 0;
        }

        echo "<p>" . $classe . " - " . $nom . " - " . $prenom . " - " . $age . "</p><br>\n";

        if ($q1 == "rep3") {
            echo "<p>Question 1 : bonne réponse</p>";
        } else {
            echo "<p>Question 1 : mauvaise réponse</p>";
        }

        if ($q2rep1 == 0 && $q2rep2 == 1 && $q2rep3 == 1 && $q2rep4 == 0) {
            echo "<p>Question 2 : bonne réponse</p>";
        } else {
            echo "<p>Question 2 : mauvaise réponse</p>";
        }
    ?>

    <p><a href="index.html">Répondre de nouveau au QCM</a></p>
</body>
</html>
