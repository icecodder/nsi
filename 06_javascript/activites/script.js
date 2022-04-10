let randomNb = Math.floor(Math.random() * 10);
console.log(randomNb);

let tentativeNb = 0;

const envoyer = () => {
    let userNb = document.getElementById("nombre").value;
    
    if (randomNb == userNb) {
        document.getElementById("cadre2").innerHTML = `Vous avez gagné avec ${tentativeNb} tentatives. 😀`;
        document.getElementById("cadre2").style.fontWeight = "bold";
        document.getElementById("cadre2").style.color = "#FF0000";
    } else {
        if (userNb < randomNb) {
            document.getElementById("cadre2").innerHTML = "C'est plus grand.";
        } else {
			document.getElementById("cadre2").innerHTML = "C'est plus petit.";
        }

        tentativeNb += 1
    }
}
