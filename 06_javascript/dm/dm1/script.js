function lancer() {
    let montant = document.getElementById("montant").value;
    let annuite = document.getElementById("annuite").value;
    let t = document.getElementById("taux").value;
    
    let tableau = [
      [
        "Période",
        "Montant",
        "Annuité",
        "Intérêts",
        "Capital",
        "Restant dû"
      ]
    ];
    
    let periode = 1;
    let reste = 1;
    
    while (reste > 0) {
      let interets = montant * t;
      let capital = annuite - interets;
      reste = montant - capital;
    
      interets = parseFloat(interets.toFixed(2));
      capital = parseFloat(capital.toFixed(2));
      reste = parseFloat(reste.toFixed(2));
      
      tableau.push([periode, montant, annuite, interets, capital, reste]);
    
      montant = reste;
      periode++;
    }
    
    console.log(tableau);

    html = "<table>\n";
    html += "<tr>\n";
    for (let i = 0; i < tableau[0].length; i++) {
        html += `<td>${tableau[0][i]}</td>\n`;
        
    }
    html += "</tr>\n";
    
    for (let i = 1; i < tableau.length; i++) {
        html += "<tr>\n";

        for (let j = 0; j < tableau[i].length; j++) {
            html += `<td>${tableau[i][j]}</td>\n`;
            
        }
        html += "</tr>\n";
    }

    html += "</table>"

    document.getElementById("tableau").innerHTML = html;
}
