questions = [
["1", "", "", "Ord i mellem", "Find ordet der kan stå mellem de to listede ord og danne to nye ord", "JÆVN … FLUE. Svaret er DØGN (JÆVNDØGN, DØGNFLUE)", "JULE … GAVE. Find ordet i mellem"],
["2", "", "", "Ord i mellem", "Find ordet der kan stå mellem de to listede ord og danne to nye ord", "JÆVN … FLUE. Svaret er DØGN (JÆVNDØGN, DØGNFLUE)", "STJERNE … LYS. Find ordet i mellem"],
["5", "", "", "Ord i mellem", "Find ordet der kan stå mellem de to listede ord og danne to nye ord", "JÆVN … FLUE. Svaret er DØGN (JÆVNDØGN, DØGNFLUE)", "SNE … VEJR. Find ordet i mellem"],
["6", "", "", "Ord før/efter", "Find ordet der kan stå enten før eller efter de tre listede ord og danne 3 nye ord", "… PALME \n … FLUE \n … KAGE. Svaret er BANAN (BANANPALME, BANANFLUE, BANANKAGE)", "… POST \n … KALENDER \n … REJSE"],
["7", "", "", "Ord før/efter", "Find ordet der kan stå enten før eller efter de tre listede ord og danne 3 nye ord", "… PALME \n … FLUE \n … KAGE. Svaret er BANAN (BANANPALME, BANANFLUE, BANANKAGE)", "… TID  \n … LOV  \n … PENGE"],
["8", "", "", "Ord før/efter", "Find ordet der kan stå enten før eller efter de tre listede ord og danne 3 nye ord", "", "KAMP ...  \n SVANE … \n MORGEN …"],
["9", "", "", "Ord før/efter", "Find ordet der kan stå enten før eller efter de tre listede ord og danne 3 nye ord", "", "EFTER ...  \n FOR … \n FEST …"],
["12", "", "", "Anagram", "Byt om på bogstaverne så de danner nye ord", "", "NUKLEAR LEJDE"],
["13", "", "", "Anagram", "Byt om på bogstaverne så de danner nye ord", "", "STÆVNEDE MIDER. Hint: Optræder i det nye testamente og møder Jesus"],
["14", "", "", "Anagram", "Byt om på bogstaverne så de danner nye ord", "", "ORANGUTANGERNE. Hint: Karakter fra en julekalender og animationsfilm"],
["15", "", "", "Skjulte ord", "Noget er skjult ved at bogstaverne i ordene er sat i alfabetisk ordning. Find sætningen ved hjælp af hintet", "", "Filmtitel: AACELLLOTUVY"],
["16", "", "", "Skjulte ord", "Noget er skjult ved at bogstaverne i ordene er sat i alfabetisk ordning. Find sætningen ved hjælp af hintet", "", "Julekalender: BEEFGJLLPRRUUYÆ"],
["19", "", "", "Skjulte ord", "Noget er skjult ved at bogstaverne i ordene er sat i alfabetisk ordning. Find sætningen ved hjælp af hintet", "", "Filmcitat (engelsk): ACEEEEFHIIKKMOPPRRTUYYY"],
["20", "", "", "Wordle", "", "", ""],
["21", "", "", "Wordle", "", "", ""],
["22", "", "", "Wordle", "", "", ""],
["23", "", "", "Wordle", "", "", ""]
]
for question in questions:
    dag = question[0]
    one = question[3]
    two = question[4]
    three = question[5]
    four = question[6]
    s = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dag} December</title>
    <meta name="twitter:image" property="twitter:image" content="https://csschristmascalendar.com/assets/og.jpg">
    <meta name="twitter:description" property="twitter:description" content="This page demonstrates that almost any design concept is achievable with only HTML + CSS. No Javascript, no graphics.">
    <meta name="twitter:title" property="twitter:title" content="CSS Christmas Calendar">
    <meta name="twitter:creator" property="twitter:creator" content="@FullStackMaker">
    <meta name="twitter:card" property="twitter:card" content="summary">
    <meta name="og:image" property="og:image" content="https://csschristmascalendar.com/assets/og.jpg">
    <meta name="og:description" property="og:description" content="This page demonstrates that almost any design concept is achievable with only HTML + CSS. No Javascript, no graphics.">
    <meta name="og:title" property="og:title" content="CSS Christmas Calendar">
    <meta name="og:type" property="og:type" content="website">
    <meta name="og:url" property="og:url" content="https://csschristmascalendar.com">
    <meta name="image" content="https://csschristmascalendar.com/assets/og.jpg">
    <meta name="description" content="This page demonstrates that almost any design concept is achievable with only HTML + CSS. No Javascript, no graphics.">
    <link rel="icon" type="image/png" href="./assets/favicon-32x32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="./assets/favicon-16x16.png" sizes="16x16" />
    <link rel="stylesheet" href="styles.css"> 

    <script defer data-domain="csschristmascalendar.com" src="https://plausible.io/js/plausible.js"></script>
    </head>
    <body>

    <div class="question">
        <h1><span class="title-1">{one}</span></h1>
        <h1><span class="title-2">{two}</span></h1>
        <h1><span class="title-3">{four}</span></h1>
        <h3><span class="title-1">{three}</span></h3>
    </div>
    <footer>
        <div><span class="footer-info">i</span>
        <div>Lavet af CLU@ATP.dk</div>
        </div>
    </footer>
    </body>
    </html>
    """

    with open(f"day{dag}.html", "w", encoding="utf-8") as f:
        f.writelines(s)

    print(f'<div class="title-container"><a href="day{dag}.html" target="_blank" title="{dag} December">{dag} December</a>')