# Hack Dig Selv

> Dette projekt er udviklet af frivillige hos Coding Pirates på ITU. Ansvarlig for projektet er Pimin Konstantin Kefaloukos så alle spørgsmål angående projektet skal stilles til ham.

![Logo](https://codingpirates.dk/wp-content/uploads/2016/09/Forside-Logo.png)

I dette projekt vil du lære om hacking. At lære at hacke er lidt ligesom at gå til karate: du skal ikke bruge det du har
lært her til at slå andre oven i hovedet (hacke dem). I stedet kunne du hjælpe dem så de ikke bliver hacket! Med andre ord: det er ulovligt at angribe andres servere uden tilladelse og det er noget vi tager meget alvorligt i Coding Pirates! Derimod er det helt lovligt at hacke din egen server lige så tosset du vil. Du kan også aftale med en ven at i hacker hinandens servere, men husk *altid* at spørge om lov først! Bare tænk på hvor irriteret du ville blive hvis nogen hackede dig! At hacke sig selv er måske den bedste måde at lære om hvordan hacking fungerer og den bedste måde at lære hvordan du undgår at blive hacket!

Hack Dig Selv består af en række missioner, som du kan udføre for at lære om hacking. På hver mission starter du et nyt serverprogram, som du bagefter skal prøve at hacke eller måske skal du løse nogle andre opgaver. Du lærer hurtigt en masse om hvad der gør en server sårbar og også hvordan du kan forbedre serverens kode så den bliver sværere at hacke i fremtiden. Du lærer at servere tit er sårbare fordi dem, der har skrevet koden til dem, har glemt at tænkte sig ordentligt om!! På en af missionerne skal du bryde en hemmelig kode. Det er en form for hacking, der kaldes for "dekryptering".

## Missioner

Projektet indeholder følgende missioner, som du kan løse for at lære om hacking og IT sikkerhed:

- I [Hej Hacker!](https://github.com/skipperkongen/hack-dig-selv/tree/master/hejhacker) lærer du at starte en webserver og forbinde til den med en browser.
- I [Operation: Systemkald](https://github.com/skipperkongen/hack-dig-selv/tree/master/systemkald) vil du udføre dit første hack af en server, som stoler lidt for meget på de beskeder den modtager fra sine brugere. Du vil lære at man altid skal tjekke de beskeder man modtager fra brugere, specielt hvis man bruger dem som input til andre programmer.
- I [Dødelig Indsprøjtning](https://github.com/skipperkongen/hack-dig-selv/tree/master/indsproejtning) (kommer snart) vil du lære om SQL injection. Du lærer endnu engang at man altid skal tjekke beskeder fra brugere hvis de skal bruges til at indsætte information i en database. I værste fald kan en bruger slette hele din database hvis du ikke passer på.
- I [Sort Snak](https://github.com/skipperkongen/hack-dig-selv/tree/master/sortsnak) (kommer snart) stifter du bekendtskab med hemmelige beskeder. Du vil lære hvordan du kan knække koden for nogle simple kryptografiske metoder, som blev benyttet i mange tusind år af herskere til at modtage hemmelige beskeder fra deres spioner.

## Hvad betyder hacking?

Vi hører tit om hacking i nyhederne, men forskellige mennesker mener tit noget forskelligt når de bruger ordet hacking. Her er hvad vi mener med hacking:

- Hacking er at lære hvordan ting er bygget, forstå hvilken rolle hver bestanddel spiller og hvordan de fungerer som en helhed
- Hacking er at pille ting fra hinanden og sætte dem sammen igen på nye og bedre måder
- Hacking er at bruge ting på sjove måder, som de egentligt ikke er designet til

Her er et billede af nogen der hacker:

![Hackere](https://upload.wikimedia.org/wikipedia/commons/4/41/Solder_workshop_at_FIXME_Hackerspace%2C_Renens%2C_Lausanne_%282015-05-23_06.25.46_by_Mitch_Altman%29.jpg)

## Struktur for missioner

I dette projekt er der er en undermappe for hvert mission du kan løse. Til hver mission hører der en server. Du starte serveren og derefter kan du løse en eller flere opgaver, som er beskrevet i README.md filen i samme mappe som serverkoden. Her er en oversigt over de filer du finder i alle missionerne

```
└── <Missionens mappe>
    ├── README.md
    ├── server.py
    └── startserver.sh
```

Udover disse tre filer kan der godt være flere afhængigt af missionen. Scriptet `startserver.sh` kan bruges til at starte missionens server, som du bagefter kan prøve at hacke.


## Forudsætninger

Projektet er designet til at køre på en billig Raspberry Pi computer. Den stakkels computer skal stå mål for lidt
af hvert, men den kan til gengæld let nulstilles igen. Raspberry Pi kan køre operativsystemet Linux og du kan faktisk bruge en hvilken som helst Linux computer til at følge dette projekt. Hvis du følger dette projekt på ITU så stiller vi en Raspberry Pi computer til rådighed for dig, men du kan også selv købe en Raspberry Pi eller installere Linux på en gammel computer du har derhjemme.

Du undrer dig måske over hvorfor vi bruger Linux og ikke f.eks. Windows eller Mac OS X, som du måske kender bedre. Årsagen er at langt de fleste servere i verden kører Linux. Selv ting du ikke tænker på som en computer kan være en computer der kører Linux, f.eks. et web camera, et køleskab eller en smart lyspære. Den slags computere der er indbygget i dagligdags ting hedder Internet of Things og det er en af årsagerne til at hacker selvforsvar bliver mere og mere vigtigt. I gamle dage kunne du måske ikke hacke en lyspære så nemt, men det kan du i dag!

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
