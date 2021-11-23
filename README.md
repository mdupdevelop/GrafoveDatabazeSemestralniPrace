# Seminární práce pro 4IZ553 Graph Databases and Graph Data Visualization

## Účel programu

Program umožňuje transformáciu dát zo spravodajského portálu [iDnes](https://www.iDnes.cz/) do grafovej podoby do databáze neo4j. Transformácií podlehiajú:

- nadpis
- autor
- související články
- témata

Výsledkom je naloadovaná grafová databáze v neo4j, ktorá obsahujé jednotlivé uzly vyjmenované vyššie a vzťahy medzi nimi.
![image](https://user-images.githubusercontent.com/61296627/141763100-cf484c53-e69c-4706-a550-3e3d147d08d5.png)

## Spustenie a používanie

### Požiadavky
Python3, najlepšie 3.9+ vyvýjané na python 3.9.8.

Nainštalované potrebné package: pip install -r /path/to/requirements.txt

Program sa spustí spustením main.py: python3 bin/main.py
(![image](https://user-images.githubusercontent.com/61296627/142956519-2039b77a-2bee-4c59-af31-ee06c46f0e50.png)


## Fungovanie programu, popis kódu

Main.py používa obsahuje 3 moduly v zložke bin/lib. 

1) **yaml_editor.py**
Modul koriguje úpravu yaml súborov v /conf. Na tieto súbory sa odkazujú ostatné skripty, pri scrapovaní alebo pracovaní s neo4j databázou.

Jedná sa o 
    1) conf_scrape.yaml
    url: url na článok\
    pages_to_scrape: počet strániek na zoscrapovanie (do grafu sa dostanú spolu\
    dir_name: názov zložky do ktorej sa články uložia v podobe json súborov
    2) conf_graph.yaml
    server: bolt://localhost:7687\
    username: neo4j\
    password: password\
    dir_name: názov zložky s json súbormi pre vloženie do grafovej databáze
    
2) **scraper.py**


3) **graphtransfer.py**


