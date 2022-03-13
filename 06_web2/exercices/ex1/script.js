function lancer() {
    multipleConsole(7);
    multiplePage(7);
};

function multipleConsole(n) {
    for (let i = 1; i <= 20; i++) {
        console.log(i * n);
    }
};

function multiplePage(n) {
    codeHtml = "<p>";

    for (let i = 1; i <= 20; i++) {
        codeHtml += `${i * n}<br>`;
    }

    codeHtml += "</p>"

    document.getElementById("affichage").innerHTML = codeHtml;
    console.log(codeHtml)
};
