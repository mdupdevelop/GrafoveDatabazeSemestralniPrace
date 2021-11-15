# Seminární práce pro 4IZ553 Graph Databases and Graph Data Visualization

## Účel programu

Program umožňuje transformáciu dát zo spravodajského portálu [iDnes](https://www.iDnes.cz/) do grafovej podoby do databáze neo4j. Transformácií podlehiajú:

- nadpis
- autor
- související články
- témata

Výsledkom je naloadovaná grafová databáze v neo4j, ktorá obsahujé jednotlivé uzly vyjmenované vyššie a vzťahy medzi nimi.
![image](https://user-images.githubusercontent.com/61296627/141763100-cf484c53-e69c-4706-a550-3e3d147d08d5.png)

## Požiadavky na spustenie

Nainštalovanie potrebných packagov: pip install -r /path/to/requirements.txt

Program funguje ako 2 nezávislé python skripty v zložke bin. 
1) **scraper.py**\

Pred spustením potrebné nastaviť súbor **conf_scrape.yaml**\
url: url na článok\
pages_to_scrape: počet strániek na zoscrapovanie (do grafu sa dostanú spolu\
dir_name: názov zložky do ktorej sa články uložia v podobe json súborov\

2) **graphtransfer.py**\

Pred spustením potrebné nastaviť súbor **conf_graph.yaml** a mať pripravený neo4j server\
server: bolt://localhost:7687\
username: neo4j\
password: password\
dir_name: názov zložky s json súbormi pre vloženie do grafovej databáze\
