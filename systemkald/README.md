# Mission: Systemkald!

![Old Computer](https://upload.wikimedia.org/wikipedia/commons/9/9e/CoCo3system.jpg)

**ADVARSEL**: Denne server er helt vildt usikker! Start den ikke på en maskine som du holder af eller som indeholder noget vigtigt, fordi der er en meget stor sandsynlighed for at den bliver reduceret til et rygende hul i jorden!

Missioner:
1. Start server (`./startserver.sh`) på en maskine som gerne må dø
1. Åben kalendersiden http://{IP ADRESSE}:8082
1. Brug kalendersiden til at udskrive kalenderen for år 2020
1. Hack siden til at skrive en fil på serveren der hedder KILROY i samme mappe hvor server koden ligger. Hvis det lykkes vil du se at siden er blevet hacket hvis du genindlæser den.
1. Hack siden for at slette filen der hedder KILROY igen
1. Undersøg serverkoden og find ud af hvorfor den er så usikker og hvordan du kan rette det.

## Hints

Undersøg hvilken besked, der bliver sendt til serveren når du vælger et årstal og derefter trykker på submit knappen

- *Hint*: Du kan se hele beskeden der bliver sendt ved at åbne din browsers udviklerværktøj før du trykker på submit

Undersøg hvordan du kan sende en anden besked til serveren end bare et årstal fra menuen?

- *Hint*: Du kan bruge unix-kommandoen `curl` til at sende en skræddersyet besked til en HTTP server
- *Hint*: prøv at bruge unix-kommandoen: `curl -X POST -F 'year=2018' http://{IP ADRESSE}:8082/` og se hvad du får tilbage.
- *Hint*: prøv nu at bruge unix-kommandoen: `curl -X POST -F 'year=2018&&ls' http://{IP ADRESSE}:8082/` og se hvad du får tilbage.
- *Hint*: Se en oversigt over nogle unix-kommandoer herunder og vælg en der kan bruges til opgaven

Unix kommandoer:

- Brug `curl` til at kalde en server direkte (`-X POST` sender et POST request, `-F 'key=value'` sender form data)
- Brug `touch` til at oprette en tom fil med et navn du vælger, f.eks. `touch MIN_FIL.txt`
- Brug `ls` til at vise alle synlige filer i en mappe
- Brug `rm` til at slette en fil
- Brug `&&` mellem to kommandoer for at udføre kommando 2 hvis kommando 1 gik godt, f.eks. `touch MIN_FIL.txt && ls`
