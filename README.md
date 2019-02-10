# Sårbare Servere

I dette projekt kan du lære om hacking, både angreb og forsvar, af servere. Formålet er
at du skal lære at skrive mere sikker serverkode, som andre har færre muligheder for at angribe.
Det er ikke meningen at du skal bruge det du har lært til at angribe andres servere! Det er nemligt ulovligt.
Men det er til gengæld lovligt at angribe sin egen server for at lære hvordan hacking fungerer. Det er vigtigt
at du lærer om hacking så du kan være med at sikre andre og dig selv imod det!

I dette projekt finder du en undermappe per emne du skal lære. Hvert emne har en tilhørende server, som
er gemt i sin egen mappe.

Her er en liste over alle de servere du finder i dette projekt:

- helloworld: opgaven går ud på at starte en server og åbne dens side i en browser.

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
