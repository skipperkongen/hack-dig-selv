# Operation: Systemkald!

![Old Computer](https://upload.wikimedia.org/wikipedia/commons/9/9e/CoCo3system.jpg)

**ADVARSEL**: Den server du nu vil møde er helt vildt usikker! Den stoler blind på beskeder, som den modtager fra vildt fremmede mennesker. Den udfører meget farlige kommandoer uden at undersøge dem først. Stol aldrig på en maskine, som blindt stoler på hvem som helst.

## Mission 1: Udskriv kalender

Serveren har et program til at udskrive kalendere.

- Åben serverens hjemmeside [http://{IP ADRESSE}:8082](http://{IP ADRESSE}:8082) i din browser. Spørg din lærer om serverens IP adresse hvis du ikke allerede kender den.
- Brug siden til at udskrive kalenderen for år 2019.

Du kan se i svaret fra serveren at den har kørt unix-kommandoen `cal 2019` for at udskrive kalenderen for 2019.

Problemet er, at serveren blindt stoler på, at du har sendt den et årstal, f.eks. 2019. Men hvad nu hvis du sender noget andet eller mere? F.eks. et årstal og en besked om at serveren skal hacke sig selv?

Serveren kombinerer hvad den formoder er et årstal og med kommandoen `cal`, hvilket giver kommandoen `cal <ÅRSTAL>`. Om lidt vil du se hvorfor det er et meget stort problem!

# Mission 2: Lær hvordan siden fungerer

Undersøg hvilket HTTP request browseren sender til serveren når du vælger et årstal og derefter trykker på submit knappen. Hyper-text Transfer Protokol (HTTP) er det sprog, som browsere og servere taler med hinanden for at sende beskeder til hinanden over internettet. F.eks. sender din browser et HTTP `GET` request når den indlæser siden og typisk et HTTP `POST` request hvis den vil sende data til serveren.

- Brug din browsers udviklerværktøj til at se kildekoden til siden.
- Find afsnittet som indeholder en `form`.
- Undersøg formen og find ud af om browseren sender data til serveren med et GET request eller et POST request når du trykker submit? Dette bestemmes af `method` attributen på form-tagget.
- Årstallet bliver sendt til serveren i en variabel. Hvilket variabel-navn bruger formen til at gemme årstallet? Du kan se denne oplysning i select-taggets `name` attribut.

# Mission 3: Send beskeder til serveren

Nu har du lært lidt om hvordan siden fungerer. Åben nu et terminal vindue for at fortsætte.

- Brug unix-kommandoen `curl` til at sende et HTTP request til serveren. Vi starter med at sende den samme besked til serveren som browseren sender.
- Skriv `curl http://{IP ADRESSE}:8082/`. Hvad ser du?
- Prøv at ændre kommandoen til `curl -X POST -F 'year=2018' http://{IP ADRESSE}:8082/`. Hvad ser du nu?

# Mission 4: Hack serveren

Nu skal vi prøve noget sjovt. I stedet for kun at sende et årstal til serveren, vil vi sende et årstal plus lidt mere.

- Skriv `curl -X POST -F 'year=2018 && echo hej' http://{IP ADRESSE}:8082/`. Hvad ser du nu?
- Serveren forventer et årstal, som den vil sætte ind efter `cal` kommandoen, f.eks `cal 2018`. Denne gang sendte vi et årstal efterfulgt af `&&echo hej` hvilket resulterer i at kommandoen `cal 2018 && echo hej` bliver udført på serveren, hvilket er to kommandoer i stedet for én! Først kører den `cal 2018` og bagefter kører den `echo hej`, hvilket udskriver beskeden "hej". I Unix kan du skrive `&&` mellem to unix-kommandoer for at udføre dem efter hinanden (hvis kommando 1 ikke fejler).

Vi har nu snydt serveren til at udføre en ekstra kommando, fordi den blindt stolede på at vi kun sendte et årstal. Vi har altså fundet ud af at serveren har en kæmpe svaghed. Nu vil vi prøve at efterlade en lille besked (en fil ved navn KILROY) på serveren, som bevis på at den er blevet hacket.

- I stedet for at udføre kommandoen `cal 2018 && echo hej` vil vi nu udføre `cal 2018 && touch KILROY`.  Dette opretter en tom fil på serveren ved navn `KILROY`. Unix kommandoen `touch` kan nemlig bruges til at oprette en tom fil med et navn du selv vælger, f.eks. `touch KILROY`. Modificer `curl` kommandoen fra før så du sender en ny besked, som udfører kommandoen `cal 2018 && touch KILROY` på serveren.

Hvis det lykkes vil du se at siden er blevet hacket når du genindlæser den i browseren. Prøv om du kan fjerne filen `KILROY` igen ved at sende en ny besked til serveren med `curl`.

- Modificer `curl` kommandoen endnu en gang, så du sender en `rm` kommando, der sletter filen. Vi vil altså gerne udføre kommandoen `cal 2018 && rm KILROY` på serveren.

# Mission 5: Forstå og ret fejlen

Hvis du har mod på det, så undersøg serverkoden og find ud af hvorfor den er så usikker og hvordan du kan rette det.

## Unix kommandoer for denne mission

Her er de unix kommandoer, som du har brugt på denne mission:

- Brug `curl` til at sende en HTTP besked til en server (`-X POST` for at sende et POST request, `-F 'key=value'` for at sende form data).
- Brug `touch` til at oprette en tom fil med et navn du vælger, f.eks. `touch MIN_FIL.txt`.
- Brug `echo` til at printe en besked.
- Brug `ls` til at udskrive alle synlige filer i en mappe.
- Brug `&&` mellem to kommandoer for at udføre kommando 2 hvis kommando 1 gik godt, f.eks. `touch MIN_FIL.txt && ls`.
