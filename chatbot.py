# chatbot.py

# ========== FILE READ/WRITE FOR NAME ==========

def lagre_navn(navn):
    with open("navn.txt", "w") as fil:
        fil.write(navn)

def les_navn():
    try:
        with open("navn.txt", "r") as fil:
            return fil.read().strip()
    except FileNotFoundError:
        return None

# ========== THEMES (TOPICS) ==========

temaer = [
    {
        "navn": "Kantine",
        "keywords": [
            "åpningstider", "kantine", "kantina", "åpen", "åpner", "stenger", "når", "når åpner", "når stenger",
            "tider", "mat", "lunsj", "åpent kantine", "spisested", "matpause", "food",
            "kafeteria", "er det åpent", "når lukker kantina", "når åpner kantina", "serverer",
            "kantinens åpningstider", "spisetid", "spisetider", "maten", "spise", "pausemat",
            "storefri", "mellommåltid", "servering", "tidspunkt for mat", "kantinelunsj",
            "frokost", "sulten", "mattilbud", "når er det mat", "lunsjtid",
        ],
        "svar": "Kantina er åpen fra 08:00 til 15:00 på hverdager."
    },
    {
        "navn": "Timeplan",
        "keywords": [
            "når starter", "timeplan", "når er", "time", "klasse", "undervisning", "skoletid",
            "skoletimer", "visma", "fag", "timeplanen", "timer", "starttid", "skolestart",
            "skoleslutt", "timeoversikt", "time tabell", "når begynner neste time",
            "oppsett for timer", "skolen begynner", "skolen slutter", "skoledag",
            "åpningstider skole", "undervisningstid", "fagtimer", "fagoversikt", "timetable"
        ],
        "svar": "Sjekk Visma InSchool for å finne ut når timene dine starter."
    },
    {
        "navn": "Wi-Fi",
        "keywords": [
            "wifi", "wi-fi", "nett", "internett", "nettverk", "passord", "nettpassord", "tilkobling",
            "nettet", "logg på nettet", "wifi-pass", "internett-passord",
            "trådløst nett", "trådløs tilkobling", "hvordan koble til nettet", "internett-tilgang",
            "internet connection", "wifi-tilkobling", "wifi problem", "internett problem",
            "hva er wifi-passordet", "kobling til internett", "network", "pc-nett",
            "skolenett", "trådløst passord", "wireless",
        ],
        "svar": "For å koble deg til nettet, koble til 'ikt-agder-intern'. Logg på med ditt skolebrukernavn og passord."
    },
    {
        "navn": "Hjelp generelt",
        "keywords": [
            "hjelp", "hjelpe", "hva", "gjør", "hva kan du", "spørsmål", "hjelpe meg", "hvordan fungerer",
            "assistent", "bot", "info", "hjelp plz", "hjelp meg bro",
            "trenger hjelp", "kan du hjelpe", "hjelp ønskes", "veiledning", "veiviser", "guide",
            "hva slags spørsmål", "hvordan spørre", "hva kan jeg spørre om", "er du der", "bot info",
            "skolebot", "informasjon", "spør chat", "spør assistent", "hjelp nå",
        ],
        "svar": "Jeg kan svare på spørsmål om åpningstider, Wi-Fi og mer. Bare spør meg!"
    },
    {
        "navn": "PC/IT-avdeling",
        "keywords": [
            "pc", "datamaskin", "tekniske problemer", "service", "it avdeling", "pc feil",
            "datafeil", "komme i kontakt med it", "datanett", "hjelp pc", "it support",
            "teknisk hjelp", "maskinfeil", "hvordan fikser jeg pc", "support av pc", "feil på laptop",
            "dataproblemer", "reparasjon", "pc-service", "hardwarefeil", "programvarefeil",
            "brukerstøtte", "skjermproblemer", "treg pc", "nettfeil", "pcn funker ikke",
        ],
        "svar": "Hvis du har problemer med PCen, vennligst kontakt skolens IT-avdeling."
    },
    {
        "navn": "Bibliotek",
        "keywords": [
            "bibliotek", "bøker", "lån", "bok", "biblioteket", "book",
            "lånekort", "bibliotekkort", "boklån", "boksøk", "innlevering", "åpningstider bibliotek",
            "fagbøker", "roman", "lydbøker", "lesesal", "studieplass", "bibliotekar", "bib",
            "arkiv", "hylleplass", "tilgjengelige bøker",
        ],
        "svar": "Skolebiblioteket er åpent hver dag fra kl. 08:00 til 15:00. Husk å ta med lånekortet ditt."
    },
    {
        "navn": "Karakterer",
        "keywords": [
            "karakter", "karakterer", "vurdering", "vurderinger",
            "poeng", "karakterkort", "fått karakter", "hvordan sjekke karakter", "karakteroppgjør",
            "karaktersystem", "betyg", "karakterutskrift", "vurderingsgrunnlag", "vurderingskriterier",
            "karakterinnlevering", "hva er karakteren min", "resultat",
        ],
        "svar": "Karakterene dine finner du i Visma InSchool. Ta kontakt med læreren din for spørsmål om vurdering."
    },
    {
        "navn": "Klasserom",
        "keywords": [
            "klasserom", "rom", "hvor er", "finn rom", "romnummer",
            "lokale", "hvordan finner jeg klasserom", "hvilket rom er jeg i", "rombooking",
            "romplan", "romoversikt", "klasserom plassering", "klasseværelse", "room finder",
            "fysisk rom", "kart over skolen", "hvilket rom har jeg time i",
        ],
        "svar": "Du kan finne klasserommet ditt ved å sjekke timeplanen i Visma InSchool. Romnumrene står der."
    },
    {
        "navn": "Kontakt administrasjon",
        "keywords": [
            "kontakt", "rektor", "inspektør", "administrasjon", "kontoret",
            "skoleledelsen", "administrativ avdeling", "hvem er rektor", "hvordan kontakte rektor",
            "skolesekretær", "inspektor", "ledelsen", "adm-avdelingen",
            "skolens hovedkontor", "ledelseskontor", "kontortid", "kontortelefon", "sekretariat",
        ],
        "svar": "For å kontakte administrasjonen, kan du ringe skolens kontor eller stikke innom i åpningstiden (08:00 - 15:00)."
    },
    {
        "navn": "Helsesykepleier / skolehelsetjeneste",
        "keywords": [
            "helse", "skolehelsetjeneste", "helsesykepleier", "sykepleier", "helsestasjon", "helseteam",
            "helsesøster", "psykisk helse", "skolehelse", "lege", "time hos helsesykepleier",
            "helsehjelp", "helsesamtale", "helseråd", "helsepersonell", "hvor er helsesykepleier",
            "kontortid helsesykepleier", "timebestilling helsesykepleier",
        ],
        "svar": "Skolehelsetjenesten har kontor ved siden av rådgiverkontoret. De er tilgjengelige kl. 09:00 - 14:00."
    },
    {
        "navn": "Rådgiver",
        "keywords": [
            "rådgiver", "studieveileder", "veiledning", "veileder",
            "rådgivning", "karriereveileder", "karrièreveiledning", "studieretning", "studieinfo",
            "fagvalg", "veiledertime", "bestille rådgivning", "studieråd", "studieveiledning",
            "hvem er rådgiver", "trenger råd", "samtale med rådgiver",
        ],
        "svar": "Du kan bestille time hos rådgiver eller studieveileder ved å sende e-post eller stikke innom kontoret."
    },
    {
        "navn": "Eksamen",
        "keywords": [
            "eksamen", "eksamensdato", "eksamener", "eksamensplan",
            "eksamensoversikt", "eksamenstid", "eksamensdatoer", "når er eksamen", "skriftlig eksamen",
            "muntlig eksamen", "eksamensinformasjon", "trekkfag", "trekk til eksamen", "eksamensregler",
            "eksamenslokale", "eksamensforberedelse", "eksamensdato liste", "eksamen i visma",
        ],
        "svar": "Eksamenstidspunkter finner du i eksamensplanen på skolens nettside. Sørg for å møte forberedt."
    },
    {
        "navn": "Ferie og fridager",
        "keywords": [
            "ferie", "fridager", "ferieplan", "skoleferie", "feriekalender",
            "ferieoversikt", "feriedatoer", "høstferie", "vinterferie", "påskeferie", "sommerferie",
            "fridag", "skolerute", "ferieinformasjon", "ferie og fri", "hvordan sjekke feriedager",
            "når er det fri", "kalender for fridager", "skoleruta",
        ],
        "svar": "Oversikt over ferie og fridager finnes i skoleruta som er publisert på kommunens nettsider."
    },
    {
        "navn": "Skoleskyss",
        "keywords": [
            "skoleskyss", "buss", "busskort", "skyss", "transport",
            "reisekort", "bussrute", "bussruter", "kollektivtransport", "bussbillett", "buss til skolen",
            "skolebuss", "reisestøtte", "reisehjelp", "transportskjema", "busstilbud",
            "hvordan søke skoleskyss", "skoleskyss ordning", "buss reise",
        ],
        "svar": "For å søke om skoleskyss, se på skolens hjemmeside under 'Transport'. Du trenger vanligvis et gyldig busskort."
    }
]

DEFAULT_SVAR = "Beklager, jeg forstod ikke. Prøv igjen med et enklere spørsmål."

# ========== HELPER FUNCTION TO FIND THEMES ==========

def finn_mulige_temaer(tekst):
    """
    Returnerer en liste over alle temaer der minst ett nøkkelord finnes i teksten.
    """
    tekst = tekst.lower()
    aktuelle_temaer = []

    for t in temaer:
        for nøkkelord in t["keywords"]:
            if nøkkelord in tekst:
                aktuelle_temaer.append(t)
                break  # Gå videre til neste tema for å unngå duplikater

    return aktuelle_temaer

# ========== MAIN CHATBOT RESPONSE FUNCTION ==========

def get_chatbot_response(user_input):
    """
    Tar imot en brukermelding (user_input) og returnerer (answer_string, multiple_themes).
    
    - If only 1 match => (answer_string, None)
    - If multiple matches => (None, [list of matching themes])
    - If none => (DEFAULT_SVAR, None)
    """
    user_input = user_input.strip().lower()

    # 1) Check for "mitt navn er" => store name
    if user_input.startswith("mitt navn er"):
        nytt_navn = user_input.replace("mitt navn er", "").strip()
        if nytt_navn:
            lagre_navn(nytt_navn)
            return (f"Hyggelig å møte deg, {nytt_navn}!", None)

    # 2) Check for "hva heter jeg"
    if "hva heter jeg" in user_input:
        navn = les_navn()
        if navn:
            return (f"Du heter {navn}.", None)
        else:
            return ("Jeg vet dessverre ikke navnet ditt enda. Skriv: 'Mitt navn er ...' for å lagre det.", None)

    # 3) If user typed "exit" (just as an example):
    if user_input == "exit":
        return ("Ha en fin dag!", None)

    # 4) Find any matching themes
    mulige_temaer = finn_mulige_temaer(user_input)

    if len(mulige_temaer) == 0:
        # No match. Check if user asked for "hjelp"
        if "hjelp" in user_input:
            return ("Jeg kan for eksempel svare på spørsmål om kantina, timeplan, eksamen m.m.", None)
        else:
            return (DEFAULT_SVAR, None)
    elif len(mulige_temaer) == 1:
        # Only one match
        return (mulige_temaer[0]["svar"], None)
    else:
        # Multiple possible themes:
        # Return them in a list so that the user can choose
        return (None, mulige_temaer)
