/**
 * Programme JavaScript
 * Objet : - programme de base
 * 
 * - Exercice 6 : distances de parcours à vélo
 * - Afficher un tableau des distances parcourues chaque semaine
 *  - La distance dépend de l'indice de la semaine et du taux d'augmentation
 */

tabImages = ["velo_1_640.jpg", "velo_2_640.jpg", "velo_3_640.jpg", "velo_4_640.jpg"];
idImg = 0;

function creerEnteteTableau(nbSemaines) {
    let codeHTML = "<tr>\n";
    codeHTML += "<td>taux\\semaine</td>\n";

    for (let n = 0; n < nbSemaines; n++) {
        codeHTML += `<td>${n}</td>\n`;
    }

    codeHTML += "</tr>\n";

    return codeHTML;
}

function creerLignesTableau(nbSemaines, nbLignes, taux, d0) {
    let codeHTML = "";
    let t = 0;

    for (let ligne = 0; ligne < nbLignes; ligne++) {
        codeHTML += "<tr>\n";
        codeHTML += `<td>${ligne}</td>\n`;

        for (let n = 0; n < nbSemaines; n++) {
            let d = d0 * Math.pow((1 + t / 100), n);
            d = Math.round(d, 2);

            codeHTML += `<td>${d}</td>\n`;
        }

        codeHTML += "</tr>\n";
        t += taux;
    }
    
    return codeHTML;
}

function calculerDistances() {
    let nbSemaines = parseInt(document.getElementById("nbSemaines").value);
    let nbLignes = parseInt(document.getElementById("nbLignes").value);
    let taux = parseFloat(document.getElementById("taux").value);
    let d0 = parseFloat(document.getElementById("dInit").value);
    
    let codeHTML = "<table>\n";
    codeHTML += creerEnteteTableau(nbSemaines);
    //console.log(codeHTML);
    codeHTML += creerLignesTableau(nbSemaines, nbLignes, taux, d0);
    //console.log(codeHTML);
    codeHTML += "</table>";
    document.getElementById("cadreTableau").innerHTML = codeHTML;
}

function cacherTableau() {
    document.getElementById("cacher1").style.display = "none";
    document.getElementById("montrer1").style.display = "block";
    document.getElementById("cadreTableau").style.display = "none";
    document.getElementById("saisieTableau").style.display = "none";
}

function montrerTableau() {
    document.getElementById("cacher1").style.display = "block";
    document.getElementById("montrer1").style.display = "none";
    document.getElementById("cadreTableau").style.display = "block";
    document.getElementById("saisieTableau").style.display = "block";
}

function cacherImage() {
    document.getElementById("cacher2").style.display = "none";
    document.getElementById("montrer2").style.display = "block";
    document.getElementById("cadreVelos").style.display = "none";
 
}

function montrerImage() {
    document.getElementById("cacher2").style.display = "block";
    document.getElementById("montrer2").style.display = "none";
    document.getElementById("cadreVelos").style.display = "block";
}

/*
function changerImage() {
    idImg++

    if (idImg >= ...) {
        idImg = ...;
    }

    document.getElementById("cadreImageVelo").src = "";
    console.log(idImg, tabImages[idImg]);
}
*/
