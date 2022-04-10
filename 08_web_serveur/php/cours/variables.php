<?php session_start(); ?>
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <title>Afficher des variables</title>
</head>
<body>
    <h2>Quelques variables d'environnement du serveur</h2>
    <p>
        <?php
            $tableau = $_SERVER;
            foreach ($tableau as $cle => $valeur) {
                echo "<b>" . $cle . "</b> : " . $valeur . "<br />" . "\n";
            }
        ?>
    </p>
</body>
