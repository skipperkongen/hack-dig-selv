# Sårbare Servere

Der er en undermappe per server i dette projekt. Her er en
liste over de servere der p.t. er implementeret med tilhørende opgaver:

- helloworld

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
