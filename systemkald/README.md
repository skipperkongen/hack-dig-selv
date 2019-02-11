# Mission: Systemkald!

**ADVARSEL**: Denne server er helt vildt usikker! Start den ikke på en maskine som du holder af eller som indeholder noget vigtigt, fordi der er en meget stor sandsynlighed for at den bliver reduceret til et rygende hul i jorden!

Missioner:
1. Start server (`./startserver.sh`)
1. Åben kalendersiden http://{IP ADDRESSE}:8082
1. Print kalender for år 2020
1. Hack siden til at skrive en fil på serveren der hedder KILROY i samme mappe hvor server koden ligger
1. Hack siden til at vise filerne i den mappe og check at du har skrevet filen
1. Hack siden til at slette filen der hedder KILROY igen
1. Undersøg serverkoden og find ud af hvorfor den er så usikker og hvordan du kan rette det.

## Hints

Du kan bruge følgende Unix kommandoer til at løse hacking opgaverne:
- `curl` til at kalde en server direkte (`-X POST` sender et post request, `-F 'key=value'` sender form data)
- `touch` til at oprette en tom fil med et navn du vælger, f.eks. KILROY.
- `ls` til at vise alle synlige filer i en mappe
- `rm` til at slette en fil
- `kommando 1 && kommando 2` udfører kommando 2 hvis kommando 1 gik godt.
