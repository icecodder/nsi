let randomNb = Math.floor(Math.random() * 10);
console.log(randomNb);

let reponse;

function lancer() {
    do {                           
        reponse = prompt("Saisir un nombre compris entre 0 et 10.");
    } while (randomNb != reponse)
    
    console.log("Vous avez gagné");
}
