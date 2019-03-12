# Hack Dig Selv

> Dette projekt er udviklet af Pimin Konstantin Kefaloukos til børn som vil lære om hacking på en ansvarlig måde

I dette projekt kan du lære om hacking. At lære at hacke er lidt ligesom at gå til karate: du skal ikke bruge det du har
lært her til at hacke andre uden deres tilladelse. Det er ulovligt at hacke andres servere uden tilladelse, men du må godt hacke dig selv! Du kan også aftale med en ven at i hacker hinanden, men husk *altid* at spørge om lov først! Tænk på hvis nogen hackede dig uden at spørge om lov! Det ville være meget irriterende, ikke? Lær at hacke ved at hacke dig selv. Det er den bedste måde.

Hack Dig Selv består af en række missioner, som du kan udføre for at lære om hacking. I hver mission starter du et nyt serverprogram, som du bagefter kan prøve at hacke eller løse andre opgaver. Du lærer hurtigt en masse om hvad der gør en server sårbar og også hvordan du kan forbedre serverens kode så den bliver sværere at hacke i fremtiden. Du lærer at servere tit er sårbare fordi dem, der har skrevet koden til dem, har glemt at tænkte sig ordentligt om!! På en af missionerne skal du bryde en hemmelig kode. Det er en form for hacking, der kaldes for "dekryptering".

## Missioner

Projektet indeholder følgende missioner, som du kan løse for at lære om hacking og IT sikkerhed:

- I [Hej Hacker!](https://github.com/skipperkongen/hack-dig-selv/tree/master/hejhacker) lærer du at starte en webserver og forbinde til den med en browser.
- I [Command Injection](https://github.com/skipperkongen/hack-dig-selv/tree/master/command-injection) vil du udføre dit første hack af en server, som stoler lidt for meget på de beskeder den modtager fra sine brugere. Serveren er sårbar overfor såkaldt command injection (også kaldet shell injection). Du vil lære at man aldrig skal stole blindt på beskeder man modtager fra en bruger, specielt hvis man bruger beskederne som input til andre programmer.
- I [SQL Injection](https://github.com/skipperkongen/hack-dig-selv/tree/master/sql-injection) (kommer snart) vil du lære om SQL injection. Du lærer endnu engang at man altid skal tjekke beskeder fra brugere hvis de skal bruges til at indsætte information i en database. I værste fald kan en bruger slette hele din database hvis du ikke passer på.
- I [Sort Snak](https://github.com/skipperkongen/hack-dig-selv/tree/master/sortsnak) (kommer snart) stifter du bekendtskab med hemmelige beskeder. Du vil lære hvordan du kan knække koden for nogle simple kryptografiske metoder, som blev benyttet i mange tusind år af herskere til at modtage hemmelige beskeder fra deres spioner.

## Hvad betyder hacking?

Vi hører tit om hacking i nyhederne, men forskellige mennesker mener tit noget forskelligt når de bruger ordet hacking. Her er hvad vi mener med hacking:

- Hacking er at lære hvordan ting er bygget og fungerer
- Hacking er at pille ting fra hinanden og sætte dem sammen igen på nye og bedre måder
- Hacking er at bruge ting på sjove måder, som de egentligt ikke er designet til

Her er et billede af nogen der hacker:

![Hackere](https://upload.wikimedia.org/wikipedia/commons/4/41/Solder_workshop_at_FIXME_Hackerspace%2C_Renens%2C_Lausanne_%282015-05-23_06.25.46_by_Mitch_Altman%29.jpg)

## Struktur for missioner

I dette projekt er der er en undermappe for hvert mission du kan løse. Til hver mission er der en server, som du kan hacke. Du starter serveren og derefter kan du løse en eller flere opgaver, som er beskrevet i README.md filen i samme mappe som serverkoden. Her er en oversigt over de filer du finder i alle missionerne

```
└── <Missionens mappe>
    ├── README.md
    ├── server.py
    └── startserver.sh
```

Scriptet `startserver.sh` kan bruges til at starte missionens server, som du bagefter kan prøve at hacke.


## Forudsætninger

Projektet er designet til at køre på en billig Raspberry Pi computer. Den stakkels computer skal stå mål for lidt
af hvert. Det gør heldigvis ikke noget, for den kan til gengæld let nulstilles igen. Raspberry Pi kan køre operativsystemet Linux og du kan faktisk bruge en hvilken som helst Linux computer til at følge dette projekt. Hvis du følger dette projekt på ITU så stiller vi en Raspberry Pi computer til rådighed for dig. Du kan selvfølgeligt selv købe en Raspberry Pi eller installere Linux på en gammel computer du har derhjemme.

Du undrer dig måske over hvorfor vi bruger Linux i stedet for Windows eller Mac OS X, som du måske kender bedre. Årsagen er at langt de fleste servere i verden kører Linux. Selv ting du ikke tænker på som en computer, kan være en computer der kører Linux, f.eks. et kamera, et køleskab eller en lyspære. Den slags computere der er indbygget i dagligdags ting hedder Internet of Things og det er en af årsagerne til at hacker selvforsvar bliver mere og mere vigtigt. I gamle dage kunne du måske ikke hacke en lyspære så nemt, men det kan du i dag!

## Walkthrough til Mission: Hej Hacker!

Start med at hente dette projekt ned på den computer som du vil bruge som "offer", f.eks. en Raspberry Pi eller en gammel computer. Åben terminalen og skriv:

```
wget https://github.com/skipperkongen/hack-dig-selv/archive/master.zip
```

Pak filen ud ved at unzippe den:

```
unzip master.zip
```


Start med at åbne server-mappen:

```
cd hack-dig-selv-master/hejhacker
```

Læs om missionen ved at åbne opgave-filen README.md, f.eks. med `cat` eller `less` kommandoen.

```
cat README.md
# eller
less README.md
```

Når du har læst opgaven kan du starte serveren. Det gør du ved at køre et shellscript ved navn `./startserver.sh`, som ligger i samme mappe som opgaveteksten. Et shellscript er et lille program; typisk bruger vi shellscripts til at automatisere ting vi vil gøre, f.eks. at starte en server på en bestemt måde. Kør shellscriptet ved at skrive `./` foran scriptets filnavn i terminalen, hvilket fortæller terminalen at det program du forsøger at køre ligger i samme mappe hvor du lige befinder dig i.

```
# Start serveren
./startserver.sh
```

Nu har du forhåbentligt startet serveren. Se om du kan åbne dens hjemmeside i en browser. Hvis du har startet serveren på en anden maskine end din egen skal du først finde ud af hvilken IP adresse serveren har. Derefter skal du finde ud af hvilken port serveren "lytter" på. Kombiner de to oplysninger og åben følgende side i din browser:

> Hint: du kan bruge kommandoen `ifconfig` til at se hvilken IP address din server har. Du kan bruge kommandoen `lsof -Pnl +M -i4 | grep -i python` til at se hvilken port serveren lytter på (serveren er skrevet i Python).

```
http://{den IP addresse du har fundet frem til}/{den port du har fundet frem til}
```

Hvis alt er gået godt vil du se en hemmelig besked. Hvad er den?
