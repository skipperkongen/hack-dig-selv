# Mission: Systemkald!

**ADVARSEL**: Denne server er helt vildt usikker! Start den ikke på en maskine som du holder af eller som indeholder noget vigtigt, fordi der er en meget stor sandsynlighed for at den bliver reduceret til et rygende hul i jorden!

Missioner:
1. Start server (`./startserver.sh`) på en maskine som gerne må dø
1. Åben kalendersiden http://{IP ADDRESSE}:8082
1. Brug kalendersiden til at udskrive kalenderen for år 2020
1. Hack siden til at skrive en fil på serveren der hedder KILROY i samme mappe hvor server koden ligger
1. Hack siden til at vise filerne i den mappe og check at du har skrevet filen
1. Hack siden til at slette filen der hedder KILROY igen
1. Undersøg serverkoden og find ud af hvorfor den er så usikker og hvordan du kan rette det.

## Hints

Hvilken besked bliver sendt til serveren når du vælger et årstal og derefter trykker på submit knappen?
> Du kan se hele beskeden der bliver sendt ved at åbne din browsers udviklerværktøj før du trykker på submit

Hvordan kan du sende en anden besked til serveren end et af årstallene fra menuen?
> Du kan bruge unix-kommandoen `curl` til at sende en skræddersyet besked til en HTTP server


Forklaring af unix-kommandoer:
- `curl` til at kalde en server direkte (`-X POST` sender et POST request, `-F 'key=value'` sender form data)
- `touch` til at oprette en tom fil med et navn du vælger, f.eks. KILROY.
- `ls` til at vise alle synlige filer i en mappe
- `rm` til at slette en fil
- `kommando 1 && kommando 2` udfører kommando 2 hvis kommando 1 gik godt.
