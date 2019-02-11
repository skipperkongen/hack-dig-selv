# Hack dig selv

> Dette projekt er udviklet af frivillige hos Coding Pirates på ITU. Ansvarlig for projektet er Pimin Konstantin Kefaloukos så alle spørgsmål angående projektet skal stilles til ham.

![Logo](https://codingpirates.dk/wp-content/uploads/2016/09/Forside-Logo.png)

I dette projekt vil du lære om hacking. At lære at hacke er lidt ligesom at gå til karate. Det er ikke meningen at du skal bruge det du har
lært til at slå andre oven i hovedet. Du vil køre forskellige serverprogrammer, som du bagefter selv skal prøve hacke. På den måde lærer du hvad der gør en server sårbar og hvordan du kan forbedre den så den bliver sværere at hacke. Du vil lære at servere tit er sårbare fordi dem der har skrevet koden til dem ikke har tænkt sig ordentligt om!!

Som sagt er det ikke meningen, at du skal bruge det du lærer her til at angribe andres servere! Det er nemligt ulovligt. Derimod er det helt lovligt at angribe din egen server lige så tosset du vil. Du kan også aftale med en ven at i angriber hinandens servere, men husk altid at spørge om lov først! Bare tænk på hvor irriteret du ville blive hvis nogen hackede dig. At hacke sig selv er måske den bedste måde at lære om hvordan hacking fungerer og den bedste måde at lære hvordan du undgår at blive hacket! Vi synes at det er vigtigt at vi allesammen lærer om hacking, så vi kan hjælpe med at beskytte hinanden!

## Hvad betyder hacking?

Forskellige mennesker mener forskellige ting når de siger hacking. Her er hvad vi mener når vi siger hacking:

- Hacking er at lære hvordan ting er bygget, forstå hvilken rolle hver bestanddel spiller og hvordan de fungerer som en helhed
- Hacking er at pille ting fra hinanden og sætte dem sammen igen på nye og bedre måder
- Hacking er at bruge ting på sjove måder, som de egentligt ikke er designet til

## Struktur

I dette projekt er der er en undermappe for hvert mission du kan løse. Til hver mission hører der en server. Du kan starte og derefter løse en eller flere opgaver, som er beskrevet i README.md, som ligger i samme mappe som serverkoden. Her er en oversigt over de filer du finder i alle missionerne

```
└── <Missionens mappe>
    ├── README.md
    ├── server.py
    └── startserver.sh
```

Udover disse tre filer kan der godt være flere afhængigt af missionen. Scriptet `startserver.sh` kan bruges til at starte missionens server, som du bagefter kan prøve at hacke.


## Forudsætninger

Projektet er designet til at køre på en billig Raspberry Pi computer. Den stakkels computer skal stå mål for lidt
af hvert, men den kan til gengæld let nulstilles igen. Raspberry Pi kører operativsystemet Linux og du kan faktisk bruge en hvilken som helst Linux computer til at følge dette projekt. Hvis du følger dette projekt på ITU så stiller vi en Raspberry Pi computer til rådighed for dig, men du kan også selv købe en Raspberry Pi eller installere Linux på en gammel computer du har derhjemme.

Du undrer dig måske over hvorfor vi bruger Linux og ikke f.eks. Windows eller Mac OS X, som du måske kender bedre. Årsagen er at langt de fleste servere i verden kører Linux. Selv ting du ikke tænker på som en computer kan være en computer der kører Linux, f.eks. et web camera, et køleskab eller en smart lyspære. Den slags computere der er indbygget i dagligdags ting hedder Internet of Things og det er en af årsagerne til at hacker selvforsvar bliver mere og mere vigtigt. I gamle dage kunne du måske ikke hacke en lyspære så nemt, men det kan du i dag!

## Sådan gør du

Her er en walkthrough til helloworld missionen. Start med at åbne server-mappen:

```
cd helloworld
```

Læs om missionen ved at åbne opgave-filen med f.eks. `cat` eller `less` kommandoen.

```
cat README.md
# eller
less README.md
```

Når du har læst opgaven skal du starte serveren. Det gør du ved at køre et shellscript ved navn `./startserver.sh`, som ligger i samme mappe som opgaveteksten. Kør shellscriptet ved at skrive `./` foran scriptets filnavn i terminalen, hvilket fortæller terminalen at det program du forsøger at køre ligger i samme mappe hvor du lige befinder dig i.

> Hint: brug `pwd` og `ls` kommandoerne til at se hvor du befinder dig og hvilke filer der er i den mappe, som du befinder dig i.

```
# Start serveren
./startserver.sh
```

Nu har du startet serveren. Se om du kan åbne dens hjemmeside i en browser. Hvis du har startet serveren på en anden maskine end din egen skal du først finde ud af hvilken IP adresse serveren har. Derefter skal du finde ud af hvilken port serveren "lytter" på. Kombiner de to oplysninger og åben følgende side i din browser:

> Hint: du kan bruge kommandoen `ifconfig` til at se hvilken IP address din server har. Du kan bruge kommandoen `lsof -Pnl +M -i4 | grep -i python` til at se hvilken port serveren lytter på (serveren er skrevet i Python).

```
http://{den IP addresse du har fundet frem til}/{den port du har fundet frem til}
```

Hvis alt er gået godt vil du se teksten 'Hej hacker!' i din browser.
