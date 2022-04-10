const verbs = [
    {
      "Infinitive": "arise",
      "Simple Past": "arose",
      "Past Participle": "arisen",
      "French": "Survenir | Se lever"
    },
    {
      "Infinitive": "awake",
      "Simple Past": "awakened / awoke",
      "Past Participle": "awakened / awoken",
      "French": "S'éveiller | Éveiller"
    },
    {
      "Infinitive": "backslide",
      "Past Participle": "backslidden / backslid",
      "Simple Past": "backslid",
      "French": "Revenir | Retomber | Récidiver"
    },
    {
      "Infinitive": "be",
      "Simple Past": "was, were",
      "Past Participle": "been",
      "French": "Être"
    },
    {
      "Infinitive": "bear",
      "Simple Past": "bore",
      "Past Participle": "born / borne",
      "French": "Porter | Supporter"
    },
    {
      "Infinitive": "beat",
      "Simple Past": "beat",
      "Past Participle": "beaten / beat",
      "French": "Battre"
    },
    {
      "Infinitive": "become",
      "Simple Past": "became",
      "Past Participle": "become",
      "French": "Devenir"
    },
    {
      "Infinitive": "begin",
      "Simple Past": "began",
      "Past Participle": "begun",
      "French": "Commencer"
    },
    {
      "Infinitive": "bend",
      "Simple Past": "bent",
      "Past Participle": "bent",
      "French": "Plier | Tordre"
    },
    {
      "Infinitive": "bid",
      "Simple Past": "bid",
      "French": "Parier | Faire une enchère"
    },
    {
      "Infinitive": "bind",
      "Simple Past": "bound",
      "Past Participle": "bound",
      "French": "Lier | Attacher"
    },
    {
      "Infinitive": "bite",
      "Simple Past": "bit",
      "Past Participle": "bitten",
      "French": "Mordre"
    },
    {
      "Infinitive": "bleed",
      "Simple Past": "bled",
      "Past Participle": "bled",
      "French": "Saigner"
    },
    {
      "Infinitive": "blow",
      "Simple Past": "blew",
      "Past Participle": "blown",
      "French": "Souffler"
    },
    {
      "Infinitive": "break",
      "Simple Past": "broke",
      "Past Participle": "broken",
      "French": "Casser | Briser"
    },
    {
      "Infinitive": "breed",
      "Simple Past": "bred",
      "Past Participle": "bred",
      "French": "Élever"
    },
    {
      "Infinitive": "bring",
      "Simple Past": "brought",
      "Past Participle": "brought",
      "French": "Apporter"
    },
    {
      "Infinitive": "broadcast",
      "Simple Past": "broadcast / broadcasted",
      "Past Participle": "broadcast / broadcasted",
      "French": "Diffuser | Émettre"
    },
    {
      "Infinitive": "browbeat",
      "Simple Past": "browbeat",
      "Past Participle": "browbeaten / browbeat",
      "French": "Intimider"
    },
    {
      "Infinitive": "build",
      "Simple Past": "built",
      "Past Participle": "built",
      "French": "Construire"
    },
    {
      "Infinitive": "burst",
      "Simple Past": "burst",
      "Past Participle": "burst",
      "French": "Éclater"
    },
    {
      "Infinitive": "bust",
      "Simple Past": "busted / bust",
      "Past Participle": "busted / bust",
      "French": "Péter"
    },
    {
      "Infinitive": "buy",
      "Simple Past": "bought",
      "Past Participle": "bought",
      "French": "Acheter"
    },
    {
      "Infinitive": "cast",
      "Simple Past": "cast",
      "Past Participle": "cast",
      "French": "Jeter (un sort) | Mouler (un métal)"
    },
    {
      "Infinitive": "catch",
      "Simple Past": "caught",
      "Past Participle": "caught",
      "French": "Attraper"
    },
    {
      "Infinitive": "choose",
      "Simple Past": "chose",
      "Past Participle": "chosen",
      "French": "Choisir"
    },
    {
      "Infinitive": "cling",
      "Simple Past": "clung",
      "Past Participle": "clung",
      "French": "S'accrocher"
    },
    {
      "Infinitive": "come",
      "Simple Past": "came",
      "Past Participle": "come",
      "French": "Venir"
    },
    {
      "Infinitive": "cost",
      "Simple Past": "cost",
      "Past Participle": "cost",
      "French": "Coûter"
    },
    {
      "Infinitive": "creep",
      "Simple Past": "crept",
      "Past Participle": "crept",
      "French": "Ramper | Fluer"
    },
    {
      "Infinitive": "crossbreed",
      "Simple Past": "crossbred",
      "Past Participle": "crossbred",
      "French": "Croiser (génétiquement)"
    },
    {
      "Infinitive": "cut",
      "Simple Past": "cut",
      "Past Participle": "cut",
      "French": "Couper"
    },
    {
      "Infinitive": "deal",
      "Simple Past": "dealt ",
      "Past Participle": "dealt",
      "French": "Gérer"
    },
    {
      "Infinitive": "dig",
      "Simple Past": "dug",
      "Past Participle": "dug",
      "French": "Creuser"
    },
    {
      "Infinitive": "disprove",
      "Simple Past": "disproved",
      "Past Participle": "disproved / disproven",
      "French": "Réfuter"
    },
    {
      "Infinitive": "dive",
      "Simple Past": "dove / dived",
      "Past Participle": "dived",
      "Subtext": "jump head-first",
      "French": "Plonger"
    },
    {
      "Infinitive": "dive",
      "Simple Past": "dived / dove",
      "Past Participle": "dived",
      "Subtext": "scuba diving",
      "French": "Plonger"
    },
    {
      "Infinitive": "do",
      "Simple Past": "did",
      "Past Participle": "done",
      "French": "Faire"
    },
    {
      "Infinitive": "draw",
      "Simple Past": "drew",
      "Past Participle": "drawn",
      "French": "Dessiner"
    },
    {
      "Infinitive": "drink",
      "Simple Past": "drank",
      "Past Participle": "drunk",
      "French": "Boire"
    },
    {
      "Infinitive": "drive",
      "Simple Past": "drove",
      "Past Participle": "driven",
      "French": "Conduire"
    },
    {
      "Infinitive": "eat",
      "Simple Past": "ate",
      "Past Participle": "eaten",
      "French": "Manger"
    },
    {
      "Infinitive": "fall",
      "Simple Past": "fell",
      "Past Participle": "fallen",
      "French": "Tomber"
    },
    {
      "Infinitive": "feed",
      "Simple Past": "fed",
      "Past Participle": "fed",
      "French": "Nourrir"
    },
    {
      "Infinitive": "feel",
      "Simple Past": "felt",
      "Past Participle": "felt",
      "French": "Se sentir | Ressentir"
    },
    {
      "Infinitive": "fight",
      "Simple Past": "fought",
      "Past Participle": "fought",
      "French": "Se battre"
    },
    {
      "Infinitive": "find",
      "Simple Past": "found",
      "Past Participle": "found",
      "French": "Trouver"
    },
    {
      "Infinitive": "flee",
      "Simple Past": "fled",
      "Past Participle": "fled",
      "French": "Fuir"
    },
    {
      "Infinitive": "fling",
      "Simple Past": "flung",
      "Past Participle": "flung",
      "French": "Lancer | Jeter"
    },
    {
      "Infinitive": "fly",
      "Simple Past": "flew",
      "Past Participle": "flown",
      "French": "Voler"
    },
    {
      "Infinitive": "forbid",
      "Simple Past": "forbade",
      "Past Participle": "forbidden",
      "French": "Interdir"
    },
    {
      "Infinitive": "forecast",
      "Simple Past": "forecast",
      "Past Participle": "forecast",
      "French": "Prévoir"
    },
    {
      "Infinitive": "forego",
      "Simple Past": "forewent",
      "Past Participle": "foregone",
      "French": "Sacrifier"
    },
    {
      "Infinitive": "foresee",
      "Simple Past": "foresaw",
      "Past Participle": "foreseen",
      "French": "Imaginer | Voir à l'avance"
    },
    {
      "Infinitive": "foretell",
      "Simple Past": "foretold",
      "Past Participle": "foretold",
      "French": "Prédire"
    },
    {
      "Infinitive": "forgive",
      "Simple Past": "forgave",
      "Past Participle": "forgiven",
      "French": "Pardonner"
    },
    {
      "Infinitive": "forsake",
      "Simple Past": "forsook",
      "Past Participle": "forsaken",
      "French": "Renoncer à"
    },
    {
      "Infinitive": "freeze",
      "Simple Past": "froze",
      "Past Participle": "frozen",
      "French": "Geler"
    },
    {
      "Infinitive": "frostbite",
      "Simple Past": "frostbit",
      "Past Participle": "frostbitten",
      "French": "Gelure"
    },
    {
      "Infinitive": "give",
      "Simple Past": "gave",
      "Past Participle": "given",
      "French": "Donner"
    },
    {
      "Infinitive": "go",
      "Simple Past": "went",
      "Past Participle": "gone",
      "French": "Aller"
    },
    {
      "Infinitive": "grind",
      "Simple Past": "ground",
      "Past Participle": "ground",
      "French": "Broyer"
    },
    {
      "Infinitive": "grow",
      "Simple Past": "grew",
      "Past Participle": "grown",
      "French": "Grandir"
    },
    {
      "Infinitive": "hand-feed",
      "Simple Past": "hand-fed",
      "Past Participle": "hand-fed",
      "French": "Nourrir à la main"
    },
    {
      "Infinitive": "handwrite",
      "Simple Past": "handwrote",
      "Past Participle": "handwritten",
      "French": "Écrire à la main"
    },
    {
      "Infinitive": "hang",
      "Simple Past": "hung",
      "Past Participle": "hung",
      "French": "Suspendre"
    },
    {
      "Infinitive": "have",
      "Simple Past": "had",
      "Past Participle": "had",
      "French": "Avoir"
    },
    {
      "Infinitive": "hear",
      "Simple Past": "heard",
      "Past Participle": "heard",
      "French": "Entendre"
    },
    {
      "Infinitive": "hew",
      "Simple Past": "hewed",
      "Past Participle": "hewn / hewed",
      "French": "Tailler (du bois)"
    },
    {
      "Infinitive": "hide",
      "Simple Past": "hid",
      "Past Participle": "hidden",
      "French": "Cacher"
    },
    {
      "Infinitive": "hit",
      "Simple Past": "hit",
      "Past Participle": "hit",
      "French": "Frapper"
    },
    {
      "Infinitive": "hold",
      "Simple Past": "held",
      "Past Participle": "held",
      "French": "Tenir"
    },
    {
      "Infinitive": "hurt",
      "Simple Past": "hurt",
      "Past Participle": "hurt",
      "French": "Blesser"
    },
    {
      "Infinitive": "inlay",
      "Simple Past": "inlaid",
      "Past Participle": "inlaid",
      "French": "Incruster"
    },
    {
      "Infinitive": "input",
      "Simple Past": "input / inputted",
      "Past Participle": "input / inputted",
      "Subtext": "data into a database",
      "French": "Entrer"
    },
    {
      "Infinitive": "interweave",
      "Simple Past": "interwove / interweaved",
      "Past Participle": "interwoven / interweaved",
      "French": "S'entremêler"
    },
    {
      "Infinitive": "keep",
      "Simple Past": "kept",
      "Past Participle": "kept",
      "French": "Garder"
    },
    {
      "Infinitive": "kneel",
      "Simple Past": "knelt / kneeled",
      "Past Participle": "knelt / kneeled",
      "French": "S'agenouiller"
    },
    {
      "Infinitive": "knit",
      "Simple Past": "knitted / knit",
      "Past Participle": "knitted / knit",
      "French": "Tricoter"
    },
    {
      "Infinitive": "know",
      "Simple Past": "knew",
      "Past Participle": "known",
      "French": "Savoir"
    },
    {
      "Infinitive": "lay",
      "Simple Past": "laid",
      "Past Participle": "laid",
      "French": "Poser"
    },
    {
      "Infinitive": "lead",
      "Simple Past": "led",
      "Past Participle": "led",
      "French": "Diriger"
    },
    {
      "Infinitive": "leave",
      "Simple Past": "left",
      "Past Participle": "left",
      "French": "Quitter"
    },
    {
      "Infinitive": "lend",
      "Simple Past": "lent",
      "Past Participle": "lent",
      "French": "Prêter"
    },
    {
      "Infinitive": "let",
      "Simple Past": "let",
      "Past Participle": "let",
      "French": "Laisser"
    },
    {
      "Infinitive": "lie",
      "Simple Past": "lay",
      "Past Participle": "lain",
      "French": "Mentir"
    },
    {
      "Infinitive": "light",
      "Simple Past": "lit / lighted",
      "Past Participle": "lit / lighted",
      "French": "Éclairer"
    },
    {
      "Infinitive": "lip-read",
      "Simple Past": "lip-read",
      "Past Participle": "lip-read",
      "French": "Lire sur les lèvres"
    },
    {
      "Infinitive": "lose",
      "Simple Past": "lost",
      "Past Participle": "lost",
      "French": "Perdre"
    },
    {
      "Infinitive": "make",
      "Simple Past": "made",
      "Past Participle": "made",
      "French": "Faire | Produire"
    },
    {
      "Infinitive": "mean",
      "Simple Past": "meant",
      "Past Participle": "meant",
      "French": "Signifier"
    },
    {
      "Infinitive": "meet",
      "Simple Past": "met",
      "Past Participle": "met",
      "French": "Rencontrer"
    },
    {
      "Infinitive": "mislead",
      "Simple Past": "misled",
      "Past Participle": "misled",
      "French": "Duper"
    },
    {
      "Infinitive": "misunderstand",
      "Simple Past": "misunderstood",
      "Past Participle": "misunderstood",
      "French": "Mal comprendre"
    },
    {
      "Infinitive": "mow",
      "Simple Past": "mowed",
      "Past Participle": "mowed / mown",
      "French": "Faucher"
    },
    {
      "Infinitive": "offset",
      "Simple Past": "offset",
      "Past Participle": "offset",
      "French": "Compenser"
    },
    {
      "Infinitive": "outbid",
      "Simple Past": "outbid",
      "Past Participle": "outbid",
      "French": "Surenchérir"
    },
    {
      "Infinitive": "outdo",
      "Simple Past": "outdid",
      "Past Participle": "outdone",
      "French": "Surpasser"
    },
    {
      "Infinitive": "overlay",
      "Simple Past": "overlaid",
      "Past Participle": "overlaid",
      "French": "Recouvrir"
    },
    {
      "Infinitive": "overpay",
      "Simple Past": "overpaid",
      "Past Participle": "overpaid",
      "French": "Surpayer"
    },
    {
      "Infinitive": "override",
      "Simple Past": "overrode",
      "Past Participle": "overridden",
      "French": "Outrepasser"
    },
    {
      "Infinitive": "overtake",
      "Simple Past": "overtook",
      "Past Participle": "overtaken",
      "French": "Dépasser"
    },
    {
      "Infinitive": "overthink",
      "Simple Past": "overthought",
      "Past Participle": "overthought",
      "French": "Trop réfléchir"
    },
    {
      "Infinitive": "overthrow",
      "Simple Past": "overthrew",
      "Past Participle": "overthrown",
      "French": "Renverser (un gouvernement)"
    },
    {
      "Infinitive": "partake",
      "Simple Past": "partook",
      "Past Participle": "partaken",
      "French": "Participer"
    },
    {
      "Infinitive": "pay",
      "Simple Past": "paid",
      "Past Participle": "paid",
      "French": "Payer"
    },
    {
      "Infinitive": "plead",
      "Simple Past": "pleaded / pled",
      "Past Participle": "pleaded / pled",
      "French": "Plaider"
    },
    {
      "Infinitive": "proofread",
      "Simple Past": "proofread",
      "Past Participle": "proofread",
      "French": "Relire"
    },
    {
      "Infinitive": "prove",
      "Simple Past": "proved",
      "Past Participle": "proven / proved",
      "French": "Prouver"
    },
    {
      "Infinitive": "put",
      "Simple Past": "put",
      "Past Participle": "put",
      "French": "Mettre"
    },
    {
      "Infinitive": "read",
      "Simple Past": "read",
      "Past Participle": "read",
      "French": "Lire"
    },
    {
      "Infinitive": "relay",
      "Simple Past": "relaid",
      "Past Participle": "relaid",
      "French": "Relayer"
    },
    {
      "Infinitive": "remake",
      "Simple Past": "remade",
      "Past Participle": "remade",
      "French": "Rééditer"
    },
    {
      "Infinitive": "repay",
      "Simple Past": "repaid",
      "Past Participle": "repaid",
      "French": "Repayer"
    },
    {
      "Infinitive": "reset",
      "Simple Past": "reset",
      "Past Participle": "reset",
      "French": "Réinitialiser"
    },
    {
      "Infinitive": "rethink",
      "Simple Past": "rethought",
      "Past Participle": "rethought",
      "French": "Reconsidérer"
    },
    {
      "Infinitive": "rewind",
      "Simple Past": "rewound",
      "Past Participle": "rewound",
      "French": "Rembobiner"
    },
    {
      "Infinitive": "rid",
      "Simple Past": "rid",
      "Past Participle": "rid",
      "French": "Débarasser"
    },
    {
      "Infinitive": "ride",
      "Simple Past": "rode",
      "Past Participle": "ridden",
      "French": "Conduire | Monter"
    },
    {
      "Infinitive": "ring",
      "Simple Past": "rang",
      "Past Participle": "rung",
      "French": "Sonner"
    },
    {
      "Infinitive": "rise",
      "Simple Past": "rose",
      "Past Participle": "risen",
      "French": "Monter | Se lever"
    },
    {
      "Infinitive": "run",
      "Simple Past": "ran",
      "Past Participle": "run",
      "French": "Courir"
    },
    {
      "Infinitive": "saw",
      "Simple Past": "sawed",
      "Past Participle": "sawed / sawn",
      "French": "Scier"
    },
    {
      "Infinitive": "say",
      "Simple Past": "said",
      "Past Participle": "said",
      "French": "Dire"
    },
    {
      "Infinitive": "see",
      "Simple Past": "saw",
      "Past Participle": "seen",
      "French": "Voir"
    },
    {
      "Infinitive": "seek",
      "Simple Past": "sought",
      "Past Participle": "sought",
      "French": "Chercher"
    },
    {
      "Infinitive": "sell",
      "Simple Past": "sold",
      "Past Participle": "sold",
      "French": "Vendre"
    },
    {
      "Infinitive": "send",
      "Simple Past": "sent",
      "Past Participle": "sent",
      "French": "Envoyer"
    },
    {
      "Infinitive": "set",
      "Simple Past": "set",
      "Past Participle": "set",
      "French": "Fixer | Mettre | Placer"
    },
    {
      "Infinitive": "sew",
      "Simple Past": "sewed",
      "Past Participle": "sewn / sewed",
      "French": "Coudre"
    },
    {
      "Infinitive": "shake",
      "Simple Past": "shook",
      "Past Participle": "shaken",
      "French": "Secouer"
    },
    {
      "Infinitive": "shave",
      "Simple Past": "shaved",
      "Past Participle": "shaved / shaven",
      "French": "Raser"
    },
    {
      "Infinitive": "shear",
      "Simple Past": "sheared",
      "Past Participle": "sheared / shorn",
      "French": "Cisailler"
    },
    {
      "Infinitive": "shed",
      "Simple Past": "shed",
      "Past Participle": "shed",
      "French": "Verser (une larme)"
    },
    {
      "Infinitive": "shit",
      "Simple Past": "shit / shat",
      "Past Participle": "shit / shitted",
      "French": "Chier"
    },
    {
      "Infinitive": "shoot",
      "Simple Past": "shot",
      "Past Participle": "shot",
      "French": "Tirer (sur quelqu'un)"
    },
    {
      "Infinitive": "show",
      "Simple Past": "showed",
      "Past Participle": "shown / showed",
      "French": "Montrer"
    },
    {
      "Infinitive": "shrink",
      "Simple Past": "shrank / shrunk",
      "Past Participle": "shrunk",
      "French": "Retrécir"
    },
    {
      "Infinitive": "shut",
      "Simple Past": "shut",
      "Past Participle": "shut",
      "French": "Fermer (sa bouche, une porte...)"
    },
    {
      "Infinitive": "sight-read",
      "Simple Past": "sight-read",
      "Past Participle": "sight-read",
      "French": "Lire à vue (une partition)"
    },
    {
      "Infinitive": "sing",
      "Simple Past": "sang",
      "Past Participle": "sung",
      "French": "Chanter"
    },
    {
      "Infinitive": "sink",
      "Simple Past": "sank / sunk",
      "Past Participle": "sunk",
      "French": "Couler"
    },
    {
      "Infinitive": "sit",
      "Simple Past": "sat",
      "Past Participle": "sat",
      "French": "S'assoir"
    },
    {
      "Infinitive": "slay",
      "Simple Past": "slew / slayed",
      "Past Participle": "slain / slayed",
      "Subtext": "kill",
      "French": "Tuer (avec une épée)"
    },
    {
      "Infinitive": "sleep",
      "Simple Past": "slept",
      "Past Participle": "slept",
      "French": "Dormir"
    },
    {
      "Infinitive": "slide",
      "Simple Past": "slid",
      "Past Participle": "slid",
      "French": "Glisser"
    },
    {
      "Infinitive": "sling",
      "Simple Past": "slung",
      "Past Participle": "slung",
      "French": "Lancer (des cailloux)"
    },
    {
      "Infinitive": "slit",
      "Simple Past": "slit",
      "Past Participle": "slit",
      "French": "Fendre"
    },
    {
      "Infinitive": "sneak",
      "Simple Past": "sneaked / snuck",
      "Past Participle": "sneaked / snuck",
      "French": "Se faufiler"
    },
    {
      "Infinitive": "sow",
      "Simple Past": "sowed",
      "Past Participle": "sown / sowed",
      "French": "Semer"
    },
    {
      "Infinitive": "speak",
      "Simple Past": "spoke",
      "Past Participle": "spoken",
      "French": "Parler"
    },
    {
      "Infinitive": "speed",
      "Simple Past": "sped / speeded",
      "Past Participle": "sped / speeded",
      "French": "Galoper"
    },
    {
      "Infinitive": "spend",
      "Simple Past": "spent",
      "Past Participle": "spent",
      "French": "Dépenser"
    },
    {
      "Infinitive": "spin",
      "Simple Past": "spun",
      "Past Participle": "spun",
      "French": "Tourner"
    },
    {
      "Infinitive": "spit",
      "Simple Past": "spit / spat",
      "Past Participle": "spit / spat",
      "French": "Cracher"
    },
    {
      "Infinitive": "split",
      "Simple Past": "split",
      "Past Participle": "split",
      "French": "Fractionner"
    },
    {
      "Infinitive": "spoon-feed",
      "Simple Past": "spoon-fed",
      "Past Participle": "spoon-fed",
      "French": "Nourrir à la cuillère"
    },
    {
      "Infinitive": "spread",
      "Simple Past": "spread",
      "Past Participle": "spread",
      "French": "Propager"
    },
    {
      "Infinitive": "spring",
      "Simple Past": "sprang / sprung",
      "Past Participle": "sprung",
      "French": "Bondir"
    },
    {
      "Infinitive": "stand",
      "Simple Past": "stood",
      "Past Participle": "stood",
      "French": "Se lever"
    },
    {
      "Infinitive": "steal",
      "Simple Past": "stole",
      "Past Participle": "stolen",
      "French": "Voler"
    },
    {
      "Infinitive": "stick",
      "Simple Past": "stuck",
      "Past Participle": "stuck",
      "French": "Coller"
    },
    {
      "Infinitive": "sting",
      "Simple Past": "stung",
      "Past Participle": "stung",
      "French": "Piquer"
    },
    {
      "Infinitive": "stink",
      "Simple Past": "stunk / stank",
      "Past Participle": "stunk",
      "French": "Puer"
    },
    {
      "Infinitive": "stride",
      "Simple Past": "strode",
      "Past Participle": "stridden",
      "French": "Marcher à grands pas"
    },
    {
      "Infinitive": "strike",
      "Simple Past": "struck",
      "Past Participle": "struck / stricken",
      "French": "Frapper"
    },
    {
      "Infinitive": "strive",
      "Simple Past": "strove / strived",
      "Past Participle": "striven / strived",
      "French": "Lutter | Aspirer"
    },
    {
      "Infinitive": "sublet",
      "Simple Past": "sublet",
      "Past Participle": "sublet",
      "French": "Sous-louer"
    },
    {
      "Infinitive": "swear",
      "Simple Past": "swore",
      "Past Participle": "sworn",
      "French": "Jurer"
    },
    {
      "Infinitive": "sweat",
      "Simple Past": "sweat / sweated",
      "Past Participle": "sweat / sweated",
      "French": "Transpirer"
    },
    {
      "Infinitive": "sweep",
      "Simple Past": "swept",
      "Past Participle": "swept",
      "French": "Balayer"
    },
    {
      "Infinitive": "swell",
      "Simple Past": "swelled",
      "Past Participle": "swollen / swelled",
      "French": "Gonfler"
    },
    {
      "Infinitive": "swim",
      "Simple Past": "swam",
      "Past Participle": "swum",
      "French": "Nager"
    },
    {
      "Infinitive": "swing",
      "Simple Past": "swung",
      "Past Participle": "swung",
      "French": "Balancer"
    },
    {
      "Infinitive": "take",
      "Simple Past": "took",
      "Past Participle": "taken",
      "French": "Prendre"
    },
    {
      "Infinitive": "teach",
      "Simple Past": "taught",
      "Past Participle": "taught",
      "French": "Enseigner"
    },
    {
      "Infinitive": "tear",
      "Simple Past": "tore",
      "Past Participle": "torn",
      "French": "User"
    },
    {
      "Infinitive": "tell",
      "Simple Past": "told",
      "Past Participle": "told",
      "French": "Dire | Raconter"
    },
    {
      "Infinitive": "test-drive",
      "Simple Past": "test-drove",
      "Past Participle": "test-driven",
      "French": "Tester un véhicule"
    },
    {
      "Infinitive": "think",
      "Simple Past": "thought",
      "Past Participle": "thought",
      "French": "Penser"
    },
    {
      "Infinitive": "throw",
      "Simple Past": "threw",
      "Past Participle": "thrown",
      "French": "Jeter"
    },
    {
      "Infinitive": "thrust",
      "Simple Past": "thrust",
      "Past Participle": "thrust",
      "French": "Pousser | Enfoncer"
    },
    {
      "Infinitive": "understand",
      "Simple Past": "understood",
      "Past Participle": "understood",
      "French": "Comprendre"
    },
    {
      "Infinitive": "undertake",
      "Simple Past": "undertook",
      "Past Participle": "undertaken",
      "French": "Entreprendre | Assumer"
    },
    {
      "Infinitive": "undo",
      "Simple Past": "undid",
      "Past Participle": "undone",
      "French": "Annuler | Défaire"
    },
    {
      "Infinitive": "unfreeze",
      "Simple Past": "unfroze",
      "Past Participle": "unfrozen",
      "French": "Dégeler"
    },
    {
      "Infinitive": "uphold",
      "Simple Past": "upheld",
      "Past Participle": "upheld",
      "French": "Maintenir (en place)"
    },
    {
      "Infinitive": "upset",
      "Simple Past": "upset",
      "Past Participle": "upset",
      "French": "Contrarier"
    },
    {
      "Infinitive": "wake",
      "Simple Past": "woke / waked",
      "Past Participle": "woken / waked",
      "French": "Réveiller"
    },
    {
      "Infinitive": "wear",
      "Simple Past": "wore",
      "Past Participle": "worn",
      "French": "Porter (un vêtement) | User (un pneu)"
    },
    {
      "Infinitive": "weave",
      "Simple Past": "wove / weaved",
      "Past Participle": "woven / weaved",
      "French": "Tisser"
    },
    {
      "Infinitive": "weep",
      "Simple Past": "wept",
      "Past Participle": "wept",
      "French": "Pleurer | Suinter"
    },
    {
      "Infinitive": "win",
      "Simple Past": "won",
      "Past Participle": "won",
      "French": "Gagner"
    },
    {
      "Infinitive": "wind",
      "Simple Past": "wound",
      "Past Participle": "wound",
      "French": "Enrouler"
    },
    {
      "Infinitive": "withdraw",
      "Simple Past": "withdrew",
      "Past Participle": "withdrawn",
      "French": "Retirer (de l'argent)"
    },
    {
      "Infinitive": "withhold",
      "Simple Past": "withheld",
      "Past Participle": "withheld",
      "French": "Retenir | Refuser"
    },
    {
      "Infinitive": "withstand",
      "Simple Past": "withstood",
      "Past Participle": "withstood",
      "French": "Résister"
    },
    {
      "Infinitive": "write",
      "Simple Past": "wrote",
      "Past Participle": "written",
      "French": "Écrire"
    }
  ]

let choixVerbe = "";
function lancer() {
    choixVerbe = Math.floor(Math.random() * verbs.length);
    console.log(choixVerbe);
    console.log(verbs[choixVerbe]);
    document.getElementById("cadre1").innerHTML = `Le verbe à l'infinitif en français est : <span id="verbe-francais">${verbs[choixVerbe]["French"]}</span>`;
}

let score = 0;
function valider() {
    let verbeInfinitif = document.getElementById("verbe-infinitif").value;
    let verbePreterit = document.getElementById("verbe-preterit").value;
    let verbeParticipe = document.getElementById("verbe-participe").value;
    console.log(verbeInfinitif);
    console.log(verbePreterit);
    console.log(verbeParticipe);

    let infinitif = "non";
    if (verbeInfinitif === verbs[choixVerbe]["Infinitive"]) {
        infinitif = "oui";
        score++;
    }

    let preterit = "non";
    if (verbePreterit === verbs[choixVerbe]["Simple Past"]) {
        preterit = "oui";
        score++;
    }

    let participe = "non";
    if (verbeParticipe === verbs[choixVerbe]["Past Participle"]) {
        participe = "oui";
        score++;
    }

    html = `<p>Infinitif : ${infinitif}</p>`;
    html += `<p>Prétérit : ${preterit}</p>`;
    html += `<p>Participe passé : ${participe}</p>`;
    html += `<p>Score : ${score}</p>`

    document.getElementById("cadre3").style.display = "block";
    document.getElementById("cadre3").innerHTML = html;
    document.getElementById("valider").disabled = "disabled";
    document.getElementById("recommencer").disabled = "";
}

function recommencer() {
    document.getElementById("cadre3").style.display = "none";
    lancer();
    document.getElementById("valider").disabled = "";
    document.getElementById("recommencer").disabled = "disabled";
}
