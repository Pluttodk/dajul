start,close = "{","}"

questions = [
["1", "", "", "Ord i mellem", "Find ordet der kan stå mellem de to listede ord og danne to nye ord", "eksempel: <br> JÆVN … FLUE. <br> Svaret er DØGN (JÆVNDØGN, DØGNFLUE)", "JULE … GAVE"],
["2", "", "", "Ord før/efter", "Find ordet der kan stå enten før de tre listede ord og danne 3 nye ord", "eksempel: <br> … PALME <br> … FLUE <br> … KAGE. <br> Svaret er BANAN (BANANPALME, BANANFLUE, BANANKAGE)", "… POST <br> … KALENDER <br> … REJSE"],
["5", "", "https://wordleplay.com/da/?tour=ZW5nZWw=", "Wordle", "Find det hemmelige ord i 6 forsøg i bedste Mastermind stil. Klik på info-knappen til højre i linket for hjælp.", "", ""],
["6", "", "", "Anagram", "Byt om på bogstaverne så de danner nye ord", "eksempel: <br> NUKLEAR LEJDE --> JULEKALENDER", "NØJSOM BASUNER"],
["7", "", "", "Skjulte ord", "Noget er skjult ved at bogstaverne i ordene er sat i alfabetisk ordning. Find sætningen ved hjælp af hintet", "eksempel: <br> ABDEGJKLLNÆ--> BJÆLDEKLANG", "Filmtitel: AACELLLOTUVY"],
["8", "", "", "Ord før/efter", "Find ordet der kan stå enten efter de tre listede ord og danne 3 nye ord", "eksempel: <br> TENNIS … <br> HOPPE … <br> FOD... <br> Svaret er BOLD  (TENNISBOLD, HOPPEBOLD, FODBOLD)", "KAMP ...  <br> SVANE … <br> MORGEN …"],
["9", "", "", "Ord i mellem", "Find ordet der kan stå mellem de to listede ord og danne to nye ord", "eksempel: <br> JÆVN … FLUE. <br> Svaret er DØGN (JÆVNDØGN, DØGNFLUE)", "SNE … VEJR"],
["12", "", "https://wordleplay.com/da/?tour=bXlycmE=", "Wordle", "Find det hemmelige ord i 6 forsøg i bedste Mastermind stil. Klik på info-knappen til højre i linket for hjælp.", "", ""],
["13", "", "", "Anagram", "Byt om på bogstaverne så de danner nye ord", "eksempel: <br> NUKLEAR LEJDE --> JULEKALENDER", "STÆVNEDE MIDER. Hint: Optræder i det nye testamente og møder Jesus"],
["14", "", "", "Ord før/efter", "Find ordet der kan stå enten før de tre listede ord og danne 3 nye ord", "eksempel: <br> … PALME <br> … FLUE <br> … KAGE. <br> Svaret er BANAN (BANANPALME, BANANFLUE, BANANKAGE)", "… TID  <br> … LOV  <br> … PENGE"],
["15", "", "", "Skjulte ord", "Noget er skjult ved at bogstaverne i ordene er sat i alfabetisk ordning. Find sætningen ved hjælp af hintet", "eksempel: <br> ABDEGJKLLNÆ--> BJÆLDEKLANG", "Julekalender: BEEFGJLLPRRUUYÆ"],
["16", "", "https://wordleplay.com/da/?tour=bmlzc2U=", "Wordle", "Find det hemmelige ord i 6 forsøg i bedste Mastermind stil. Klik på info-knappen til højre i linket for hjælp.", "", ""],
["19", "", "", "Ord i mellem", "Find ordet der kan stå mellem de to listede ord og danne to nye ord", "eksempel: <br> JÆVN … FLUE. <br> Svaret er DØGN (JÆVNDØGN, DØGNFLUE)", "STJERNE … LYS"],
["20", "", "", "Ord før/efter", "Find ordet der kan stå enten efter de tre listede ord og danne 3 nye ord", "eksempel: <br> TENNIS … <br> HOPPE … <br> FOD... <br> Svaret er BOLD  (TENNISBOLD, HOPPEBOLD, FODBOLD)", "EFTER ...  <br> FOR … <br> FEST …"],
["21", "", "https://wordleplay.com/da/?tour=c2FsbWU=", "Wordle", "Find det hemmelige ord i 6 forsøg i bedste Mastermind stil. Klik på info-knappen til højre i linket for hjælp.", "", ""],
["22", "", "", "Skjulte ord", "Noget er skjult ved at bogstaverne i ordene er sat i alfabetisk ordning. Find sætningen ved hjælp af hintet", "eksempel: <br> ABDEGJKLLNÆ--> BJÆLDEKLANG", "Filmcitat (engelsk): ACEEEEFHIIKKMOPPRRTUYYY"],
["23", "", "", "Anagram", "Byt om på bogstaverne så de danner nye ord", "eksempel: <br> NUKLEAR LEJDE --> JULEKALENDER", "ORANGUTANGERNE. Hint: Karakter fra en julekalender og animationsfilm"]
]
for question in questions:
    
    dag = question[0]
    if question[2] == "":
        one = question[3]
    else:
        one = f"""
            <a href="{question[2]}" style="color: #9c163f;">{question[3]}</a>
        """
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
    <meta name="twitter:description" property="twitter:description" content="D&A glædelige jule quiz">
    <meta name="twitter:title" property="twitter:title" content="DA jul'en kom til ATP">
    <meta name="og:description" property="og:description" content="D&A glædelige jule quiz">
    <meta name="og:title" property="og:title" content="DA jul'en kom til ATP">
    <meta name="og:type" property="og:type" content="website">
    <meta name="description" content="D&A glædelige jule quiz">
    <link rel="icon" type="image/png" href="./assets/favicon-32x32.png" sizes="32x32" />
    <link rel="icon" type="image/png" href="./assets/favicon-16x16.png" sizes="16x16" />
    <link rel="stylesheet" href="styles.css"> 
    </head>
    <body onload="set_gates()">

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
    <script>
    function set_gates() {start}
      var date = new Date();
      var day = date.getDate();
      var month = date.getMonth()+1;

    if ((day < {dag} && month == 12) || (month != 12)) {start}
        var role = document.getElementsByClassName('question')[0];
        role.innerHTML = '<h1><span class=\"title-1\">Den er ikke klar endnu!</span></h1>';
    {close}
    {close}                
    </script>
    </html>
    """

    with open(f"day{dag}.html", "w", encoding="utf-8") as f:
        f.writelines(s)

    # print(f'<div class="title-container"><a href="day{dag}.html" target="_blank" title="{dag} December">{dag} December</a>')

    print(f"""
        if ((day < {dag} && month == 12) || (month != 12)) {start}
            var role = document.getElementsByClassName('day-{dag}')[0];
            role.style.visibility = 'hidden';
        {close}
    """)