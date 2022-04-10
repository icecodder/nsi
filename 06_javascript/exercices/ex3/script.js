function lancer() {
    let nom = "";
    let tableau = [];
    let index = 0;

    do {
        nom = prompt("Saisir un nom");

        if (nom !== "" && nom !== null) {
            tableau.push(nom);
            console.log(tableau);
            index++;

            let randomNb = Math.floor(Math.random() * index);
            console.log(randomNb);

            console.log(`Le nom est ${tableau[randomNb]}`);
        }
    } while (nom !== null)
}
