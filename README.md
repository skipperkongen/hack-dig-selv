# Sårbare Servere

I dette projekt kan du lære om hacking, både angreb og forsvar. Specifikt vil du lære hvordan man angriber en sårbar server og hvordan du forsvarer dig mod angreb hvis serveren er din egen. Du vil lære at forstå hvad det vil sige at en server er sårbar, nemlig at dem der har skrevet koden til den ikke har tænkt sig ordentligt om!!

Formålet er ikke at du skal bruge det du har lært til at angribe andres servere! Det er nemligt ulovligt. Det er meningen at du skal lære at skrive kode, som onde hackere har færre muligheder for at angribe. Det er lovligt at angribe din egen server lige så tosset du vil. Du kan også aftale med en ven at i angriber hinandens servere, men husk altid at spørge om lov først! At hacke selv er måske den bedste måde at lære om hvordan hacking fungerer, så du kan forsvare dig selv og andre mod hackerangreb. Vi synes at det er vigtigt at vi allesammen lærer om hacking, så vi kan hjælpe hinanden!

# Struktur

Der er en undermappe for hvert emne du kan lære i dette projekt. Hvert emne har en tilhørende server, som
er gemt i sin egen mappe og der er også mere information om hvad det går ud på.

Her er en liste over alle de servere du finder i dette projekt:

- helloworld: lær at starte en server og åbne den i en browser.

# Sådan gør du

Her vil du lære hvordan du kan starte og bruge en server i dette projekt.
Vi bruger helloworld serveren som eksempel.

Der er følgende filer i undermappen til helloworld. Det er de samme filer du vil
finde i alle undermapperne.

```
└── helloworld
    ├── opgave.txt
    ├── server.py
    └── startserver.sh
```

Start med at åbne server-mappen:

```
cd helloworld
```


Du kan læse om den opgave der hører til serveren ved at bruge `cat` eller `less` kommandoen.

```
cat opgave.txt
# eller
less opgave.txt
```

Når du har forstået opgaven kan du starte serveren.

```
# Start serveren
./startserver.sh
# Åben din browser på http://localhost:5000/ og se om du kan løse opgaven.
```
